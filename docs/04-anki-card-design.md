# 04 — Anki card design

Anki is a scheduler. It has no opinion about whether a card is worth reviewing.
You supply that judgment, and it is the whole game: a deck of bad cards produces
fluent wrong knowledge, on a schedule, for years.

This document is the part you must not skim.

## The one principle

**A card should test exactly one retrievable unit, cued well enough that the
answer is unambiguous.**

Everything below is a consequence.

Why "one unit" is not pedantry:

- Anki schedules a card as a whole. If a card holds three facts and you know two,
  you grade it "hard" forever. It becomes a **leech** — a card you fail
  repeatedly — and you learn nothing from the repetition except frustration.
- Retrieval difficulty feeds the scheduling model. A card that is hard because
  it is *three questions stapled together* teaches the scheduler the wrong
  thing about you.
- Partial knowledge is invisible. You will believe you know the card.

## The four properties

| Property | Test | Fix if it fails |
| --- | --- | --- |
| **Atomic** | Can the answer be stated as one sentence with no "and"? | Split into two cards |
| **Cued** | Does the front uniquely determine the answer? | Add the distinguishing detail to the front |
| **Standalone** | Would this make sense to you in 8 months with no context? | Name the subject explicitly |
| **Retrievable** | Can you produce it in under ~10 seconds? | It is a practice problem, not a card |

The "10 second" bound is not about speed. It is a proxy for *single retrieval
unit*. If producing the answer requires reconstructing a chain, you are
practicing a derivation, and Anki is the wrong container for that.

## Note types

| Type | Use when | Example |
| --- | --- | --- |
| `Basic` | The direction of the question is fixed | "Binary search worst case?" → O(log n) |
| `Basic (and reversed)` | Both directions are genuinely useful | term ↔ definition, where producing the term from the definition matters |
| `Cloze` | The fact is embedded in a sentence | "... membership in a Python `list` is O({{c1::n}})..." |

Reversed cards are overused. "What is O(log n)?" has infinitely many answers —
that is a bad reverse. Only reverse when the reverse is *also* a unique fact.

Cloze is the best default for technical material because it keeps the context
that makes the fact meaningful. The risk is cloze abuse: deleting a word from a
sentence you do not understand produces a card that tests word-shape
recognition. The surrounding sentence must be doing real work.

## Patterns by content type

| Content | Pattern | Good | Bad |
| --- | --- | --- | --- |
| Definition | Basic, term → one-sentence definition | "What does *idempotent* mean for an HTTP method?" | "Define idempotency, statelessness, and safety" |
| Complexity | Basic, named algorithm + case → bound | "Merge sort, worst case?" → O(n log n) | "What is the complexity of sorting?" |
| Code idiom | Cloze inside a real snippet | "`x in s` is O({{c1::1}}) for a `set`, O({{c1::n}}) for a `list`" | "How do you check membership in Python?" |
| Math | Basic or cloze with MathJax | "Master theorem, $T(n)=2T(n/2)+n$ → {{c1::Θ(n log n)}}" | "State the master theorem" |
| Comparison | Basic, one discriminating axis | "`rebase` vs `merge`: which rewrites commit hashes?" | "Compare rebase and merge" |
| English | Cloze on the collocation, in a sentence | "We need to {{c1::mitigate}} the risk, not eliminate it" | "What does mitigate mean?" |
| Failure mode | Basic, symptom → cause | "Query suddenly slow after adding an index on a low-cardinality column. Likely cause?" | "List reasons a query is slow" |

Note the shape: every good card names its subject and asks for one thing. Every
bad card is a small essay prompt.

## The enumeration problem

This is the most common defect, and it is the one AI generates most.

**Bad:** "What are the four ACID properties?"
You will learn *that there are four*. You will not reliably learn
atomicity, consistency, isolation, durability — and if you miss one, you cannot
tell which.

**Fix — one card per property, each from a different angle:**

- "A transaction that transfers money debits one account and credits another,
  and a crash occurs between the two. Which ACID property is violated?" →
  atomicity
- "Which ACID property guarantees that concurrent transactions produce the same
  result as some serial order?" → isolation
- "Cloze: Durability guarantees that committed data survives {{c1::a crash or
  power loss}}."

Same knowledge, four retrievable units, four independent scheduling histories.

The general rule: **never ask for a set; ask for one member, or ask what
distinguishes one member.**

## The multi-angle web

For anything that matters, one card is not enough — one card tests one
association. Build 3–5 cards on independent angles (Matuschak's prompt design):

1. **Definition** — what is it?
2. **Mechanism** — why does it work this way?
3. **Precondition** — when does it apply / not apply?
4. **Contrast** — what is the key difference from the nearest alternative?
5. **Failure** — what happens when a constraint is violated?

Five angles is not five copies. Each is a separate retrieval path into the same
concept, which is what makes the concept robust rather than the card.

## Context: the orphan card problem

Cards written while reading a paragraph inherit the paragraph's pronouns. Six
months later, "it" and "this function" are meaningless.

**Bad:** "What does it return when the list is empty?"
**Good:** "In Python, `min([])` raises what?"

The fix is mechanical: every card front must name its subject. If the subject is
a code symbol, include the symbol.

The related failure is **anchorless facts**: "The default timeout is 30
seconds." Of what? A fact with no anchor is not retrievable in the world, only in
the deck — and decks get deleted.

## What should not be a card

| Not a card | Why | Do instead |
| --- | --- | --- |
| Problem solving ("find the bug in this 40-line function") | Multi-step reasoning; the card tests the whole chain | Practice problems, interleaved |
| Design judgment ("should you use a queue here?") | Depends on context that a card cannot hold | Write a design note; discuss |
| Large code blocks | Recall of 30 lines is not a retrieval unit | Recall the *shape*: signature, invariant, complexity |
| "Understanding" | Not a retrievable unit | Retrieval of the *components* of understanding |
| Anything you can look up in 3 seconds and never need offline | Pure deck bloat | Nothing |
| Facts from a single blog post you have not verified | Hallucination risk compounds with repetition | Verify first (`06`) |

A useful filter: **would knowing this cold change what I do?** If not, it is
trivia. Trivia is allowed, but it should be tagged `tier::exam` or dropped, not
mixed into the deck that matters.

## Leech policy

Failed 8+ times is not a discipline problem, it is a card problem. Three
responses, in order:

1. Delete it. Some facts belong in a reference document, not in memory.
2. Split it into two smaller cards.
3. Add a cue that makes the answer actually determinable.

Do not keep grinding. Grinding a leech costs review time and teaches you to
dread the deck.

## Write by hand first

For the first month, write every card yourself. This is not sentimentality — it
is the only way to calibrate what "atomic" and "cued" feel like. People who
start with AI-generated decks never develop the judgment to audit them, and the
audit is the part that matters (`06`).

After a month, you will read a paragraph and see the three cards in it. Then
automate.

## One-page summary

- One fact per card.
- Name the subject.
- Ask for one thing, not a list.
- The answer must be producible in ten seconds.
- No card for anything requiring multi-step reasoning.
- If you fail it eight times, the card is wrong, not you.
- Check every card against
  [`templates/card-quality-checklist.md`](../templates/card-quality-checklist.md).

→ Next: [05 — Anki scheduling](05-anki-scheduling.md)
