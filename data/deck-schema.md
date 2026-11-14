# Deck schema

Two files per deck. One is for Anki, one is for auditing. Keep them in sync.

```
data/decks/<deck-name>.tsv              # import this into Anki
data/decks/<deck-name>.manifest.json    # provenance + review state
```

## 1. The TSV (Anki import format)

Four columns, tab-separated, UTF-8 without BOM, no header row variation:

```
NoteType	Front	Back	Tags
```

Rules that actually break imports if you ignore them:

- Exactly one tab between columns. No tabs inside any field.
- No literal newlines inside a field. Use `<br>` for a line break.
- Escape `<` `>` `&` inside code as `&lt;` `&gt;` `&amp;`.
- Indent code with spaces, never tabs.
- MathJax: inline `\(...\)`, display `\[...\]`. Do not use `$...$`.

`NoteType` is one of `Basic`, `Basic (and reversed card)`, `Cloze`.

## 2. The manifest (the part agents need)

The TSV cannot carry provenance without polluting tags. So provenance lives
here, keyed by card index.

```json
{
  "deck": "dsa-basics",
  "created": "2026-11-14",
  "generator": "agent:deepseek-v4.1-flash",
  "source_docs": ["docs/07-cs-roadmap.md#phase-2"],
  "review": { "status": "spot-checked", "by": "human", "sample_size": 5 },
  "cards": [
    {
      "row": 1,
      "front_hash": "a1b2c3",
      "source_span": "docs/07-cs-roadmap.md:142-148",
      "confidence": "strong",
      "status": "accepted",
      "notes": ""
    }
  ]
}
```

Fields:

| Field | Why it exists |
| --- | --- |
| `source_span` | Lets a later agent re-read the exact paragraph instead of trusting the card |
| `front_hash` | Cheap duplicate detection across decks and regeneration runs |
| `confidence` | Inherited from the source claim's tag; a card cannot be more certain than its source |
| `status` | `accepted`, `rejected`, `needs-human` |
| `generator` | Which model produced it, so quality regressions are traceable |

## 3. Tags

Four axes, all lowercase, all `::`-separated. This is the minimum that stays
useful after a year.

```
domain::<subject>  tier::<importance>  lifecycle::<stability>  card::<type>
```

- `domain::` — `cs`, `dsa`, `math`, `os`, `network`, `database`, `lang-python`,
  `lang-cpp`, `web`, `english`, `tooling`
- `tier::` — `core` (will matter in 10 years), `standard` (industry baseline),
  `tooling` (versioned, will rot), `exam` (for a specific course or interview)
- `lifecycle::` — `evergreen`, `evolving` (re-check in 1-2 years),
  `ephemeral` (delete after the course)
- `card::` — `fact`, `cloze`, `code-recall`, `code-trace`, `compare`, `bug`

`lifecycle::ephemeral` is the most underused tag. A card about a framework
version pin is not knowledge, it is a note. Tag it honestly and delete it later.

## 4. Why not put everything in one giant deck

Subdecks cost nothing and let you suspend a whole rotting branch
(`tooling::nextjs`) without touching evergreen cards. One deck per domain,
subdecks only when a domain actually splits.
