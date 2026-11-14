# Card quality checklist

Apply this to every card before it enters a deck. Each item is yes/no.
A card that fails any **hard** item is rejected, not "improved later".

| # | Check | Hard? | Fails when |
| :-: | --- | :-: | --- |
| 1 | Exactly one fact is being retrieved | yes | Answer has two parts joined by "and" |
| 2 | Answer is producible in under ~10 seconds | yes | You have to reconstruct a derivation |
| 3 | The question stands alone, with no dangling pronoun | yes | "What does it return?" / "Why is this faster?" |
| 4 | The answer is not visible in the question | yes | Question restates the answer's key term |
| 5 | It is recall, not recognition | yes | Multiple choice, or "is X true?" |
| 6 | No enumeration | yes | "Name the four...", "List the steps of..." |
| 7 | The source span is recorded | yes | Card exists with no traceable origin |
| 8 | Confidence tag matches the source claim | yes | `[practice]` claim presented as `[strong]` |
| 9 | Not a near-duplicate of an existing card | yes | Same fact, different wording |
| 10 | Requires no multi-step reasoning | yes | Tracing a loop by hand across 6 iterations |
| 11 | Has an anchor if the fact is context-dependent | no | "The default timeout is 30s" — of what? |
| 12 | Uses the simplest note type that works | no | Basic card where a Cloze would be clearer |
| 13 | Code is escaped and indented with spaces | no | Raw `<` in a `<pre>` block, or tabs |
| 14 | MathJax uses `\(...\)` not `$...$` | no | Formula renders as literal text |
| 15 | Tagged on all four axes | no | Card is invisible to future filtering |

## The three failures that matter most

**Enumeration (#6).** This is the single most common AI-generated card defect.
An enumeration card trains you to recall *that there were four items*, not the
items. It also breaks scheduling: you know three of four, so you grade it
"hard" forever and the card becomes a leech. Split it into one card per item,
each asked from a distinct angle.

**Answer leakage (#4).** "What data structure gives O(1) average lookup and uses
hashing — a hash table?" No retrieval happened. The cue has to leave the
answer genuinely unstated.

**Orphan context (#3, #11).** Cards written by an agent that just read a
paragraph inherit that paragraph's pronouns. Six months later "it" means
nothing. Every card must name its subject explicitly.

## Leech policy

If a card is failed 8+ times, do not keep grinding it. That is information
about the card, not about you. Delete it and write two smaller cards, or accept
that the fact belongs in a reference document rather than in memory.
