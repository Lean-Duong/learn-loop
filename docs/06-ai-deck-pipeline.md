# 06 — AI deck pipeline

Automating card creation is worth it for exactly one reason: writing good cards
is slow, and most of the slowness is mechanical. The judgment is not mechanical,
so the pipeline has to keep the human in the loop at the judgment step and
remove them from everything else.

What goes wrong without a pipeline: you ask an agent for 100 cards, get 100
plausible cards, import them, and spend six months memorizing four hallucinations
and ninety trivialities.

## What to automate, what not to

| Step | Automate? | Why |
| --- | --- | --- |
| Finding candidate facts in a source | Yes | Reading for extractable facts is mechanical |
| Deciding what is worth remembering | **No** | This is the entire skill. Delegate it and you learn nothing about your own learning |
| Drafting the question/answer text | Yes | Wording is mechanical once the fact is chosen |
| Atomicity check | Yes | Rule-based; an agent applies it well |
| Answer-leak check | Yes | Rule-based |
| Deduplication | Yes | Hashing and near-match |
| Factual verification | **Partly** | An agent can compare against the quoted source span; it cannot be trusted to verify against the world |
| Spot-check sampling | **No** | Human. Sample 10%, read them cold |

The division of labour: **agent proposes, human disposes, agent audits.**

## The pipeline

```
 source doc
    │
    ├─ 1. EXTRACT   agent lists candidate facts, each with a quoted source span
    │
    ├─ 2. SELECT    human keeps the ones worth remembering  ← the real step
    │
    ├─ 3. DRAFT     agent writes atomic cards from the selected facts
    │
    ├─ 4. AUDIT     agent applies the mechanical checklist (04 + checklist file)
    │
    ├─ 5. DEDUP     hash the fronts against existing decks + sample deck
    │
    ├─ 6. VERIFY    agent re-checks each card against its quoted span
    │
    ├─ 7. SAMPLE    human reads a random 10% cold and grades them
    │
    └─ 8. EXPORT    TSV + manifest  (data/deck-schema.md)
```

Steps 1, 3, 4, 5, 6 can run unattended. Steps 2 and 7 cannot.

### Two checks people skip

**The render check.** A card that looks fine in JSON can render as garbage in
Anki, silently. Before export, assert mechanically:

- HTML tags balanced; every literal `<`, `>`, `&` in code escaped as `&lt;`,
  `&gt;`, `&amp;` (an unescaped `<T>` is parsed as a tag and vanishes).
- Math uses `\(...\)` or `\[...\]` only. If the string contains `[$]`, the card
  will try to render a LaTeX image, which is disabled by default and **fails
  silently** — the card just shows nothing.
- Cloze note ids are contiguous from `c1`, and no cloze body contains `}}`.
- No `::` inside a cloze answer without escaping (`std::variant` becomes a
  cloze hint; write `std:<!-- -->:variant`).
- Referenced media files exist.

**The one-breath judge.** Show a second model *only the front* and ask: "Could a
competent student answer this in one breath, without seeing anything else?
Score 1–5." Reject below 4. This catches the failure the rule-based checks
cannot: a card that is atomic, leak-free, and still unanswerable because it is
ambiguous or missing context. Rule checks verify form; this verifies
answerability.

### Why source spans are mandatory

Every candidate fact must carry the exact quote it came from — **at most ~40
words, and the quote must contain the answer, not merely the topic.** A span
that says "PostgreSQL uses MVCC" does not support a card asking for the
isolation-level name.

This does three things at once:

1. It makes hallucination detectable — a card with no span is a red flag by
   construction.
2. It lets a later audit re-read the paragraph instead of trusting the card.
3. It makes regeneration possible when the source changes.

A card without a source span does not enter the deck. No exceptions.

## Prompt templates

These are starting points, not gospel. They are written to be pasted.

### 1. Extract

```
You are extracting candidate facts for spaced-repetition cards from a
technical document.

RULES
- Only extract facts that are STABLE (true in a year), ARBITRARY (must be
  memorized, not derivable), and NEEDED COLD (must be recalled without lookup).
- Skip: opinions, design trade-offs, multi-step procedures, anything requiring
  judgment, anything that is obvious from the name.
- Every candidate must include the exact sentence(s) it came from, quoted.

OUTPUT (markdown table)
| # | Fact (one sentence) | Type (definition/complexity/idiom/semantics/comparison) | Quote | Line ref |

Do not write cards yet. Do not invent facts. If the document is thin, return
fewer rows — 5 real candidates beat 30 weak ones.
```

### 2. Draft cards

```
Write Anki cards for the selected facts below.

HARD RULES
- One fact per card. If the answer contains "and", split it.
- The front must name its subject. No pronouns.
- The answer must be producible in under 10 seconds.
- No enumeration ("name the four...").
- The answer must not appear in the question.
- Prefer Cloze when the fact lives in a sentence; Basic otherwise.
- Escape < > & in code as &lt; &gt; &amp;. Indent code with spaces, never tabs.
- MathJax: \(...\) inline, \[...\] display. Never $...$.

OUTPUT (TSV, tab-separated, no header)
NoteType<TAB>Front<TAB>Back<TAB>Tags

For each card also output one manifest line: row, source_span, confidence.
```

### 3. Audit

```
Audit these cards against the checklist. For each card output PASS or FAIL
with the failing check number and a one-line fix.

CHECKS
1  one fact only            9  no near-duplicate
2  answer < 10 seconds      10 no multi-step reasoning
3  front names its subject  11 anchor present if needed
4  answer not in question   12 simplest note type
5  recall, not recognition  13 code escaped, spaces not tabs
6  no enumeration           14 MathJax syntax correct
7  source span present      15 four tag axes present
8  confidence matches source

Be strict. A card that "could be improved" is a FAIL. Return only the table and
a count of passes and fails.
```

The audit prompt is where most of the value is. Agents are noticeably better at
rejecting against explicit criteria than at generating without them.

## Failure modes and how to catch them

| Failure | Symptom | Catch |
| --- | --- | --- |
| **Hallucinated fact** | Card states an API/behaviour that does not exist; sounds perfectly plausible | No source span, or span does not contain the claim. Re-read the span, never the card |
| **Obsolete-as-current** | Card teaches a deprecated API as if current | `lifecycle::evolving` + an `audit::YYYY` tag; re-check yearly |
| **Trivial card** | Answer is obvious from the question or the name | Audit check 4; also the human select step |
| **Near-duplicate** | Same fact, three phrasings | Front hash + normalized-text similarity. **Do not rely on Anki's own duplicate check** — it is exact-string on the first field only, so it misses every rephrasing |
| **Orphan card** | "It returns null" with no subject | Audit check 3 |
| **Recognition card** | "Is X true?" / multiple choice | Audit check 5 |
| **Multi-step card** | Requires tracing a loop or a derivation | Audit check 10 |
| **Deck bloat** | 300 cards from a 1,000-word doc | Cap: at most 1 card per 100 words of source, and expect far fewer |
| **Answer leak** | Question restates the answer's key term | Audit check 4 |

The worst failure is the first one, and it is the only one an agent cannot
reliably catch by itself. Spaced repetition makes hallucinations *durable*, so
the verification step is not optional overhead — it is the reason the pipeline
is allowed to exist.

## Density

A useful cap: **one card per 100 words of source, maximum.** A 2,000-word
document yields at most 20 cards, and a good extraction usually yields 5–8. If
an agent returns 60, it is carding restatements, not knowledge.

Track your acceptance rate (accepted cards ÷ drafted cards). A healthy pipeline
sits around 30–50%. Above 80%, your audit is too permissive. Below 15%, your
extraction prompt is pulling the wrong kind of fact.

## Metrics to keep in the manifest

- **Acceptance rate** — health of extraction.
- **Hallucination rate** — cards rejected because the span did not support them.
  Should trend to zero; if it does not, the model or the source is the problem.
- **Duplicate rate** — should fall as your dedup index grows.
- **Cards per source doc** — catches bloat.

## When not to automate

Automate only after you can write a good card by hand and explain why it is
good. Until then, an agent's cards will look fine to you and you will have no
basis to reject them. The first month is hand-written for a reason (`04`).

Also: never automate the *choice* of what to learn. An agent will happily
generate a 200-card deck for a topic you do not need. The deck becomes an
obligation, and obligations get abandoned.

## The export contract

Follow [`data/deck-schema.md`](../data/deck-schema.md):

- `data/decks/<name>.tsv` — four columns, tab-separated, UTF-8 no BOM.
- `data/decks/<name>.manifest.json` — provenance, confidence, review status.

A deck that cannot be audited is a deck you will not maintain.

→ Next: [07 — CS roadmap](07-cs-roadmap.md)
