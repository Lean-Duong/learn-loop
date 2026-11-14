# AGENTS.md

Machine-facing contract. Read this before reading anything else in the repo.

## 1. Token rule (read this twice)

This repo is **English-first**. `README.md` and `docs/*.md` are the canonical,
complete, up-to-date source.

`README.vi.md` and `docs/vi/**` are Vietnamese mirrors written for the human
owner's reading comfort. **Do not read them.** They contain no information the
English files lack. Reading them doubles your token cost for zero gain. If you
are an agent and you opened a `vi/` file, close it and open the English one.

## 2. What this repo is

A research synthesis about *how to learn*, not a textbook and not a course.
It answers four questions:

1. Which study methods still hold up, and which are outdated?
2. How does learning change now that generative AI agents exist?
3. How do you use Anki without producing a deck full of junk?
4. How does a CS student learn English alongside technical material?

Every claim carries a confidence tag:

| Tag | Meaning | How to treat it |
| --- | --- | --- |
| `[strong]` | Systematic review / meta-analysis / replicated result | Safe to build on |
| `[moderate]` | Single good study, or consistent but thinner evidence | Usable, note the caveat |
| `[practice]` | Reasoned from experience or theory; no direct evidence | Opinion. Do not present as fact |

If a claim has no tag, treat it as `[practice]`.

## 3. How to use it as source material

1. Find the right doc through the index table in `README.md`.
2. Read only that doc, plus `docs/10-sources.md` if you need to verify a claim.
3. When you generate flashcards, follow `docs/06-ai-deck-pipeline.md` and
   `data/deck-schema.md` exactly. They are the contract.
4. Every generated card must record where it came from in the deck manifest.
5. **Never invent a fact that is not in the docs.** If the docs are silent,
   say the docs are silent. Do not fill the gap with plausible-sounding text.
   A hallucinated card is worse than a missing card, because spaced repetition
   will burn it into memory.
6. Run `python data/validate_deck.py` before handing a deck back. Exit code 1
   means the deck is not deliverable — fix the deck, do not waive the check.

## 4. Hard rules when generating cards

These are non-negotiable. `docs/04-anki-card-design.md` explains why.

- One retrievable fact per card. No exceptions.
- No enumeration cards ("name the four types of X"). Split them.
- The question must stand alone. No "it", "this function", "the above".
- The answer must be producible in under ~10 seconds.
- Reject anything that needs multi-step reasoning. That is practice, not recall.
- Reject anything where the answer is visible in the question.
- Deduplicate against every deck in `data/decks/`, using the `front_hash`
  definition in `data/deck-schema.md`.
- Mark each card's confidence and review status in the manifest.

## 5. What not to do

- Do not "improve" the docs by rewriting them in your own voice. They are
  versioned prose with specific citations. Quote or link instead.
- Do not add new sources without adding them to `docs/10-sources.md`.
- Do not turn `[practice]` claims into `[strong]` claims.
- Do not generate a 300-card deck from a 1,000-word doc. Density is not value.
