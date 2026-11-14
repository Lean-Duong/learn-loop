# 01 — What still works

The useful question is not "what is a good study technique" but "which
techniques have survived attempts to debunk them, and under what conditions do
they backfire".

This document is organized by strength of evidence, not by popularity. The
anchor is Dunlosky et al. (2013), which reviewed ten techniques across the
experimental literature and rated them on generality and evidence quality. Most
of what follows either confirms or refines that review.

## The short version

| Technique | Evidence | Best for | Fails when |
| --- | --- | --- | --- |
| Retrieval practice | `[strong]` | Everything | The prompt is ambiguous or the answer is multi-part |
| Spaced repetition | `[strong]` | Durable facts, vocabulary, idioms | Cards are non-atomic; intervals are crammed |
| Interleaving | `[strong]` | Problem categories, discrimination | You have not learned the individual procedures yet |
| Worked examples | `[strong]` | Novices in procedural domains | You are already competent (expertise reversal) |
| Self-explanation | `[moderate]` | Conceptual material | You explain vaguely and never check the explanation |
| Elaborative interrogation | `[moderate]` | Facts with causal structure | The fact is arbitrary (no "why" exists) |
| Deliberate practice | `[moderate]` | Skilled performance | The task is not well-defined, or feedback is absent |
| Project-based learning | `[moderate]` | Integration, motivation | It replaces instruction instead of following it |
| Dual coding | `[moderate]` | Spatial/structural material | The diagram is decorative |
| Sleep and consolidation | `[strong]` | Retention of everything | You use it as an excuse to skip review |

## Retrieval practice

**What it is.** Producing information from memory rather than re-exposing
yourself to it. A closed book, a blank page, a flashcard, a quiz.

**Evidence.** Roediger & Karpicke (2006) showed that students who read a passage
once and then tested themselves outperformed students who read it four times, on
a delayed test — while the rereaders *predicted* they had done better.
Karpicke & Blunt (2011) found retrieval practice beat elaborative concept
mapping on transfer questions, not just verbatim recall. This is one of the most
replicated findings in the field `[strong]`.

The mechanism is not mysterious: retrieving a memory modifies it, making it
easier to retrieve next time, and the effort of retrieval is what does the work.
Recognition does not count. Reading a solution and nodding does not count.

**For CS.** Retrieval practice is why "I understand it when I read the code"
and "I can write it from scratch" are different skills, and only the second one
survives an interview or an incident. Practical forms:

- Close the editor and write the function signature, the invariant, the
  complexity, from memory.
- Predict the output of a snippet before running it.
- Explain a system's failure mode out loud with no notes.
- Re-derive a proof or an algorithm's recurrence rather than rereading it.

**Failure mode.** Retrieval practice on a badly formed prompt trains the wrong
thing. If the question is "explain TCP", you will retrieve a vague paragraph
forever and never notice it is vague. The prompt has to name a specific
retrievable unit. This is the entire reason Anki card design matters
(`04-anki-card-design.md`).

## Spaced repetition

**What it is.** Reviewing at expanding intervals, timed to just before you would
forget.

**Evidence.** Cepeda et al. (2006) meta-analysis of 254 studies: spaced
practice beat massed practice reliably, and the optimal gap scales with how long
you need to retain the material. Cepeda et al. (2008) found the optimal gap is
roughly 10–20% of the retention interval. `[strong]`

**For CS.** Facts that will not change: complexity classes, protocol handshakes,
SQL semantics, language idioms, English collocations. Spaced repetition is the
right tool and almost the only tool. It is the wrong tool for design judgment
and debugging, which need varied practice, not recall (`04`).

**Failure mode.** Spacing a bad card makes it worse, not better: you rehearse
the same wrong answer on a schedule and it becomes fluent. Also, spacing only
works if the interval actually expands — reviewing everything daily is massed
practice wearing a costume.

## Interleaving

**What it is.** Mixing problem types within a session instead of blocking one
type.

**Evidence.** Rohrer & Taylor (2007) on math practice and Kornell & Bjork (2008)
on category induction both found interleaved practice produced worse
performance during practice and better performance on delayed tests `[strong]`.
The discomfort is the point.

**For CS.** This is the single most underused technique in programming study.
Doing ten binary-search problems in a row teaches you to pattern-match the
section heading. A mixed set — two binary search, two DP, two graph, two
unfamiliar — forces you to *classify* the problem, which is the actual skill.
Same for debugging: mixed bug categories beat a tutorial on "the five bug
types".

**Failure mode.** Interleaving before you can execute any single procedure
produces confusion, not discrimination. Learn the procedure blocked first
(usually with worked examples), then interleave.

## Worked examples, and the expertise reversal effect

**What it is.** Studying a fully worked solution before attempting problems.

**Evidence.** For novices, worked examples beat unguided problem solving,
because they free working memory for schema construction (Sweller's cognitive
load theory). But Kalyuga et al. (2003) showed the effect reverses: once you
have the schema, worked examples become redundant and *worse* than solving
`[strong]`.

**For CS.** This resolves an argument you see constantly online. "Don't look at
the solution" is right for someone with the schema and wrong for a beginner who
will otherwise spend four hours learning nothing. The honest rule: read the
worked example, then immediately reproduce it from memory, then solve a variant
without looking. The transition point is when you can predict the next line
before reading it.

**Failure mode.** Staying in worked-example mode forever. That is tutorial hell
with better production values (`02`).

## Self-explanation and elaborative interrogation

**What it is.** Explaining to yourself *why* a fact is true, or why a step
follows.

**Evidence.** Chi et al. (1994) found students who self-explained during
examples learned more; Dunlosky et al. rated both techniques as moderate utility
— they help, but they are weaker than testing and spacing, and they are easy to
do badly `[moderate]`.

**For CS.** The version that works is adversarial: "why is this O(log n) and not
O(n)?", "what breaks if I remove this lock?", "why did the authors choose a
B-tree here instead of a hash index?". The version that does not work is
paraphrasing the paragraph you just read.

**Failure mode.** Confabulation. A confident wrong explanation feels identical
to a correct one from the inside. This is why self-explanation needs a check —
a test, a peer, or an AI reviewer used as a *critic* rather than an answer key
(`03`).

## Deliberate practice

**What it is.** Practice on a specific weakness, at the edge of ability, with
immediate feedback, repeated with correction.

**Evidence.** Ericsson's original framing is often overstated. Macnamara et al.
(2014) meta-analysis found deliberate practice explained about 26% of variance
in games, 21% in music, 18% in sports, 4% in education, and under 1% in
professions `[moderate]` — real, but nowhere near the "10,000 hours" story
(`02`).

**For CS.** The useful part is the structure: pick one weakness (say, reasoning
about concurrency), get feedback fast (tests, a reviewer, a profiler), correct,
repeat. The useless part is counting hours.

**Failure mode.** Practicing things you are already good at because it feels
productive. Deliberate practice is supposed to feel like failure.

## Project-based learning

**What it is.** Building something real, with constraints, end to end.

**Evidence.** Freeman et al. (2014) meta-analysis of 225 STEM studies found
active learning raised exam scores by ~0.47 SD and cut failure rates `[strong]`
for *active learning*; project-based learning specifically is `[moderate]`,
because "project" covers everything from a guided build to being dropped in the
ocean.

**For CS.** Projects are where separate facts become a system, and systems
thinking is the part AI has not commoditized (`07`). But a project with no
review and no constraints teaches you to ship whatever compiles.

**Failure mode.** Project-based learning used as a *substitute* for instruction.
Kirschner, Sweller & Clark (2006) is the canonical argument: minimal guidance
does not work for novices, and "just build something" is minimal guidance.

## Teach-back / Feynman

**What it is.** Explain the concept in plain language to an imagined beginner,
find the point where the explanation collapses, go back to the source.

**Evidence.** It is a form of self-explanation plus retrieval, so the evidence
inherits from both `[moderate]`. The specific "Feynman technique" branding has
no dedicated literature.

**For CS.** Works well for mechanisms with a causal chain (how a hash table
resizes, why a TCP handshake needs three packets). Fails for anything you can
only gesture at.

**Failure mode.** Explaining to yourself in your own private shorthand, which
feels like teaching and is actually recognition. Explain to a real person, or
write it down and read it a week later.

## Dual coding

**What it is.** Pairing verbal material with a visual or structural
representation.

**Evidence.** Moderate support, strongest when the visual encodes structure that
the words cannot carry efficiently `[moderate]`. The "learning styles" version of
this idea is false (`02`).

**For CS.** Memory diagrams, state machines, call stacks, index structures.
Drawing the B-tree yourself is the technique; looking at a diagram of a B-tree
is not.

## Sleep

**What it is.** Consolidation during sleep stabilizes and integrates what you
learned.

**Evidence.** Diekelmann & Born (2010) review: sleep after learning improves
retention, and the effect is large enough to matter for exam timing `[strong]`.
All-nighters trade consolidation for exposure and lose.

**For CS.** The practical version is unglamorous: review before bed rather than
at 2am, and do not schedule a cram session the night before a practical exam.

**Failure mode.** Treating sleep as a substitute for retrieval. Consolidation
strengthens what is there; it does not create the memory.

## Desirable difficulties

Bjork's framing, and the correct lens for everything above: conditions that make
performance *worse during learning* and retention *better afterwards* —
spacing, interleaving, testing, varied practice, generation before instruction.

This is why self-assessment is unreliable. The techniques that feel effective
(rereading, highlighting, watching a clear lecture) are the ones that do not
work. Expect the good ones to feel bad.

## What this means for you

Three techniques carry most of the value, and they compose:

1. **Retrieval** — you produce the answer, not recognize it.
2. **Spacing** — you come back to it later, on a schedule.
3. **Interleaving** — you mix types so you learn to classify, not just execute.

Anki implements 1 and 2 almost perfectly. It implements 3 badly — that is your
job, in how you sequence practice sessions. Everything else in this document is
either a refinement or a special case.

→ Next: [02 — What is outdated](02-what-is-outdated.md)
