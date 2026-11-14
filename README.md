# learn-loop

A small, opinionated knowledge base on **how to learn** — for a CS student who
has to survive an AI-agent job market, retain what he learns, and do it in
English.

Not a course. Not a productivity system. A reference you read once, then keep
open while you study.

---

## Why this exists

Three things changed at once:

1. **Generative AI removed the penalty for not knowing things** — you can look
   up any syntax in four seconds. That makes *retention* feel optional, and
   most people quietly stop building durable knowledge.
2. **The evidence on learning has been stable for twenty years** and is still
   ignored by most study advice online, which optimizes for the feeling of
   learning rather than the fact of it.
3. **Spaced repetition is the one lever with a large, replicated effect** — but
   it is also the easiest thing to ruin. A deck of bad cards is worse than no
   deck, because it burns wrong facts into memory on a schedule.

So the goal is narrow: keep the methods that work, drop the ones that do not,
and use Anki in a way that produces cards worth reviewing in two years.

## Who this is for

A Vietnamese IT student (me) who:

- wants depth in a few areas, not breadth in twenty;
- reads English comfortably but wants more practice;
- uses AI agents daily and does not want his own skill to atrophy;
- will later feed this repo to an agent that generates study documents and
  flashcards.

If you are not that person, the methods section still transfers. The Anki and
English sections assume a technical reader.

---

## Read in this order

| # | Document | Answers | Read it when |
| :-: | --- | --- | --- |
| 01 | [What still works](docs/01-what-works.md) | Which methods have real evidence behind them | First. Everything else assumes this |
| 02 | [What is outdated](docs/02-what-is-outdated.md) | Which popular methods are a waste of time | Right after 01, to unlearn things |
| 03 | [Learning with AI](docs/03-learning-with-ai.md) | How agents help and how they quietly make you worse | Before you build an AI study habit |
| 04 | [Anki card design](docs/04-anki-card-design.md) | What makes one card good and another useless | Before your first real deck |
| 05 | [Anki scheduling](docs/05-anki-scheduling.md) | FSRS, settings, and what is actually noise | Once you have 200+ cards |
| 06 | [AI deck pipeline](docs/06-ai-deck-pipeline.md) | How an agent should generate and audit decks | When you automate card making |
| 07 | [CS roadmap](docs/07-cs-roadmap.md) | What to learn, in what order, in the AI era | When planning a semester |
| 08 | [English for developers](docs/08-english-for-developers.md) | How to actually get better at English | Ongoing, low intensity |
| 09 | [The weekly loop](docs/09-weekly-loop.md) | One minimal system that fits a real week | If you only read one doc, read this one |
| 10 | [Sources](docs/10-sources.md) | Every citation, with links | When you want to check a claim |

Supporting material:

- [`templates/concept-note.md`](templates/concept-note.md) — note format that
  is also card-generation input.
- [`templates/card-quality-checklist.md`](templates/card-quality-checklist.md) —
  15 pass/fail checks for a card.
- [`data/deck-schema.md`](data/deck-schema.md) — TSV + manifest format.
- [`AGENTS.md`](AGENTS.md) — the contract for AI agents reading this repo.

---

## The rules this repo follows (KISS)

1. **One idea per file.** If a document needs a table of contents, it should be
   two documents.
2. **Every claim is tagged.** `[strong]` = meta-analysis or replicated.
   `[moderate]` = one good study. `[practice]` = opinion. Untagged means
   opinion.
3. **No method gets recommended without a failure mode.** "Use spaced
   repetition" is incomplete; "spaced repetition fails when the cards are
   non-atomic" is the useful version.
4. **English is canonical.** Vietnamese mirrors live in `docs/vi/` and
   `README.vi.md`. They exist for reading comfort, not as a second source of
   truth.
5. **Agents read English only.** See the token note below.
6. **Nothing here is a productivity system.** If a rule cannot survive a bad
   week, it is not in here.
7. **Decks are data, not prose.** Cards live in TSV + manifest so they can be
   audited, regenerated, and diffed.

---

## Using Anki with this repo (quick start)

1. Read `docs/04-anki-card-design.md` once. It is the only part you must not
   skim.
2. Install Anki, turn on FSRS, set desired retention to ~0.90. Ignore every
   other setting for now (`docs/05-anki-scheduling.md`).
3. Write cards by hand for the first month. Hand-written cards teach you what a
   good card feels like; AI-generated cards do not.
4. Once you know the shape of a good card, use
   `docs/06-ai-deck-pipeline.md` to automate the boring half.
5. Review daily, ~15–25 minutes. If a session runs long, you have too many new
   cards, not too little discipline.

---

## For AI agents

Read [`AGENTS.md`](AGENTS.md) first — it is short and it will save you tokens.

The one thing worth repeating here: **this repo is English-first. Do not read
`README.vi.md` or anything under `docs/vi/`.** Those are Vietnamese mirrors for
the human owner. They contain no information the English files lack, so reading
them doubles cost for zero gain.

---

## What this is not

- Not medical or clinical advice. The sleep and exercise material is about
  study performance, not treatment.
- Not a claim that these methods work identically for everyone. Effect sizes
  are averages; your variance is your own.
- Not finished. Evidence tags and versioned-tooling claims get re-checked;
  everything else is stable enough to leave alone.

## Status

Started 2026-11. Content is a synthesis of published research plus practice.
Where the two disagree, the doc says so. If you find a claim that is wrong or
out of date, the fix is a one-line edit plus a source in `docs/10-sources.md`.

## Tiếng Việt

Bản tiếng Việt: [`README.vi.md`](README.vi.md) và thư mục [`docs/vi/`](docs/vi/).
Bản tiếng Anh là bản gốc và đầy đủ nhất.

## License

MIT. Use it, fork it, feed it to your own agents.
