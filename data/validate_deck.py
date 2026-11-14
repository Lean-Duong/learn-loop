#!/usr/bin/env python3
"""Validate a deck pair: <name>.tsv + <name>.manifest.json.

Structural checks only. It cannot tell you whether a card is *good* — that is
docs/04-anki-card-design.md and templates/card-quality-checklist.md. It catches
the mechanical failures that make a deck unimportable or unauditable.

Usage:
    python data/validate_deck.py                     # every deck in data/decks
    python data/validate_deck.py data/decks/x.tsv    # one deck
    python data/validate_deck.py --fix-hashes        # rewrite stale front_hash

Exit code 0 = no errors (warnings allowed), 1 = errors.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

NOTE_TYPES = {"Basic", "Basic (and reversed card)", "Cloze"}
CONFIDENCE = {"strong", "moderate", "practice"}
STATUS = {"accepted", "rejected", "needs-human"}
TIER = {"core", "standard", "tooling", "exam"}
LIFECYCLE = {"evergreen", "evolving", "ephemeral"}
CARD_TYPE = {"fact", "cloze", "code-recall", "code-trace", "compare", "bug"}
DOMAIN = {
    "cs", "dsa", "math", "os", "network", "database", "compiler", "distributed",
    "lang-python", "lang-cpp", "lang-java", "lang-rust", "lang-go", "web",
    "english", "tooling", "security", "ai",
}
HTML_TAGS = re.compile(
    r"</?(?:br|b|i|u|em|strong|code|pre|div|span|sub|sup|small|ul|ol|li|hr|img|a)\b[^>]*>",
    re.IGNORECASE,
)
TAG_RE = re.compile(r"<[^>]+>")


def normalize_front(front: str) -> str:
    """The canonical form used for hashing and duplicate detection.

    Strip markup, unescape the entities the schema requires, casefold, collapse
    whitespace, drop trailing punctuation. Two cards that differ only in
    formatting must collide.
    """
    text = front.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    text = TAG_RE.sub(" ", text)
    text = unicodedata.normalize("NFKC", text).casefold()
    text = re.sub(r"\s+", " ", text).strip()
    return text.rstrip(" .?!:;")


def front_hash(front: str) -> str:
    return hashlib.sha256(normalize_front(front).encode("utf-8")).hexdigest()[:8]


class Report:
    def __init__(self, deck: str) -> None:
        self.deck = deck
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def emit(self) -> None:
        head = f"[{self.deck}]"
        for m in self.errors:
            print(f"{head} ERROR  {m}")
        for m in self.warnings:
            print(f"{head} WARN   {m}")
        if not self.errors and not self.warnings:
            print(f"{head} ok")


def parse_tags(raw: str) -> dict[str, str]:
    axes: dict[str, str] = {}
    for token in raw.split():
        if "::" in token:
            k, _, v = token.partition("::")
            axes[k] = v
    return axes


def check_card(r: Report, row: int, note: str, front: str, back: str, tags: str) -> str:
    where = f"row {row}"

    if note not in NOTE_TYPES:
        r.err(f"{where}: NoteType {note!r} not in {sorted(NOTE_TYPES)}")
    if not front.strip():
        r.err(f"{where}: empty front")
    if not back.strip() and note != "Cloze":
        r.err(f"{where}: empty back")
    if "\r" in front or "\r" in back:
        r.err(f"{where}: carriage return inside field")

    axes = parse_tags(tags)
    for axis, allowed in (
        ("domain", DOMAIN),
        ("tier", TIER),
        ("lifecycle", LIFECYCLE),
        ("card", CARD_TYPE),
    ):
        if axis not in axes:
            r.err(f"{where}: missing tag axis '{axis}::'")
        elif axes[axis] not in allowed:
            r.warn(f"{where}: {axis}::{axes[axis]} not in the documented set")

    for field, value in (("front", front), ("back", back)):
        stripped = HTML_TAGS.sub("", value)
        if "<" in stripped:
            r.err(
                f"{where}: unescaped '<' in {field} — Anki will eat it as a tag "
                f"(use &lt;)"
            )
        if "[$]" in value or "[/$]" in value:
            r.err(f"{where}: [$]...[/$] needs a local LaTeX install and fails silently")
        if re.search(r"(?<!\\)\$[^$\n]+\$", value):
            r.warn(f"{where}: bare $...$ — use \\(...\\) for MathJax")

    if note == "Cloze" and not re.search(r"\{\{c\d+::", front + back):
        r.err(f"{where}: Cloze card has no {{{{c1::...}}}} marker")

    if note != "Cloze":
        words = len(re.sub(r"<[^>]+>", " ", back).split())
        if words > 15:
            r.warn(f"{where}: back is {words} words — probably more than one fact")

    return front_hash(front)


def load_tsv(path: Path, r: Report) -> list[tuple[str, str, str, str]]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        r.err("TSV has a UTF-8 BOM — Anki will mangle the first field")
        raw = raw[3:]
    text = raw.decode("utf-8")
    rows: list[tuple[str, str, str, str]] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) != 4:
            r.err(f"line {lineno}: {len(parts)} tab-separated columns, expected 4")
            continue
        rows.append(tuple(p.strip() for p in parts))  # type: ignore[arg-type]
    return rows


def validate(tsv: Path, fix_hashes: bool) -> Report:
    r = Report(tsv.stem)
    manifest_path = tsv.with_suffix(".manifest.json")

    if not manifest_path.exists():
        r.err(f"missing {manifest_path.name} — a deck without provenance is not auditable")
        return r

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        r.err(f"manifest is not valid JSON: {exc}")
        return r

    rows = load_tsv(tsv, r)
    if not rows:
        r.err("TSV has no cards")
        return r

    cards = manifest.get("cards", [])
    if len(cards) != len(rows):
        r.err(f"manifest has {len(cards)} cards, TSV has {len(rows)} rows")

    if manifest.get("deck") and manifest["deck"] != tsv.stem:
        r.warn(f"manifest.deck {manifest['deck']!r} != filename {tsv.stem!r}")

    hashes: dict[str, int] = {}
    changed = False

    for idx, (note, front, back, tags) in enumerate(rows):
        row_no = idx + 1
        computed = check_card(r, row_no, note, front, back, tags)

        if computed in hashes:
            r.err(
                f"row {row_no}: duplicate front of row {hashes[computed]} "
                f"after normalization"
            )
        else:
            hashes[computed] = row_no

        entry = cards[idx] if idx < len(cards) else None
        if entry is None:
            continue
        if entry.get("row") != row_no:
            r.err(f"row {row_no}: manifest row field is {entry.get('row')!r}")
        if entry.get("front_hash") != computed:
            if fix_hashes:
                entry["front_hash"] = computed
                changed = True
            else:
                r.err(
                    f"row {row_no}: front_hash {entry.get('front_hash')!r} != "
                    f"{computed!r} (run --fix-hashes)"
                )
        if entry.get("confidence") not in CONFIDENCE:
            r.err(f"row {row_no}: confidence {entry.get('confidence')!r} invalid")
        if entry.get("status") not in STATUS:
            r.err(f"row {row_no}: status {entry.get('status')!r} invalid")
        if entry.get("status") == "accepted" and not entry.get("source_span"):
            r.err(f"row {row_no}: accepted card has no source_span")

    if changed:
        manifest_path.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        print(f"[{tsv.stem}] fixed front_hash values in {manifest_path.name}")

    return r


def main(argv: list[str]) -> int:
    fix_hashes = "--fix-hashes" in argv
    args = [a for a in argv if not a.startswith("--")]
    root = Path(__file__).resolve().parent
    targets = [Path(a) for a in args] if args else sorted((root / "decks").glob("*.tsv"))

    if not targets:
        print("no decks found")
        return 1

    failed = False
    for tsv in targets:
        r = validate(tsv, fix_hashes)
        r.emit()
        failed = failed or bool(r.errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
