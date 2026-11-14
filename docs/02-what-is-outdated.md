# 02 — What is outdated

This is the harder half. Everyone knows they should test themselves; almost
nobody has removed the techniques that feel productive and are not.

A useful test for any study habit: **does it produce something you could be
wrong about?** If there is no possible wrong answer, you are not learning, you
are organizing.

## The list

| Practice | Status | Why it survives anyway |
| --- | --- | --- |
| Rereading | Fails | Familiarity feels like mastery |
| Highlighting / underlining | Fails | It is fast and looks like work |
| Summarization as default | Mostly fails | It works for some texts, badly for others |
| Cramming (massed practice) | Fails for retention | It passes the exam |
| Learning-styles matching | False | Intuitive, and nobody checks |
| Passive video / tutorial hell | Fails | The production quality is high |
| Transcription note-taking | Fails | Notes feel like an artifact |
| "10,000 hours" | Misread | It is a memorable number |
| Memorizing syntax | Depreciating fast | It used to be required |
| Breadth-first bootcamp hopping | Fails | Each new stack is exciting |

## Rereading

Callahan & Dunlosky and the Dunlosky et al. (2013) review put rereading at low
utility: it produces a reliable *feeling* of fluency with almost no delayed
retention benefit. The mechanism is simple — fluency with the text is not
fluency with the content. The third read is easier because you recognize the
page, not because you can reconstruct the argument.

What to do instead: read once, close it, write what you remember, then check.
The gap between your recall and the text is the actual study material.

## Highlighting and underlining

Low utility in the same review, and worse than that: highlighting can *reduce*
learning by focusing attention on isolated phrases rather than the relation
between them. It also converts a text into a list of fragments with no argument
attached.

If you must mark something, mark it with a question in the margin ("why does
this hold?"). A mark you cannot turn into a question is decoration.

## Summarization as a default

Dunlosky rated summarization low-to-moderate: it helps when you are already
skilled at summarizing and the text has clear structure, and hurts otherwise
because a bad summary drops exactly the causal links that matter. It is a
technique for people who can already write, applied to texts that may not
summarize.

For technical material, the better move is a **worked example plus a
reconstruction**: what is the invariant, what breaks without it, what is the
complexity.

## Cramming

Massed practice works for the test on Thursday and fails for everything after.
Cepeda et al. (2006) is unambiguous: the same total study time distributed
across days produces substantially better retention than massed.

Cramming is rational under bad incentives — a course that grades one exam
rewards it. If you have to cram, cram, but do not then conclude that your
memory is bad. You optimized for a different objective.

## Learning styles (VAK)

The meshing hypothesis — that matching instruction to a "visual/auditory/
kinesthetic" preference improves learning — has no supporting evidence. Pashler
et al. (2008) reviewed the literature and found the studies that would test it
properly had not been done, and the ones that existed did not support it
`[strong]`.

What is true is narrower: some *content* is better presented visually (a graph
structure), and some people have more prior knowledge in a domain. Neither of
those is a learning style.

The cost is real: believing you are "a visual learner" gives you permission to
avoid the retrieval practice that would actually work.

## Passive video and tutorial hell

Watching a well-produced course feels like progress because the explanation is
clear. Clarity is the problem: a good lecture removes the difficulty that
produces learning (Bjork's desirable difficulties). You end up able to follow,
not able to produce.

"Tutorial hell" is the specific loop of following tutorials, feeling competent,
attempting something alone, discovering you cannot, and starting a new tutorial
to feel competent again. The exit is not a better tutorial. It is a small
project with a constraint you cannot Google your way out of, plus a review of
what you built.

The rule that works: **for every hour of tutorial, spend two hours building
without one.** If you cannot, the tutorial was too advanced or you were not
paying attention to the right layer.

## Transcription note-taking

Typing a lecture verbatim is the lowest-yield form of note-taking: it engages
working memory with transcription and leaves nothing for comprehension. The
classic Mueller & Oppenheimer (2014) finding — longhand beats laptop for
conceptual questions — has been contested and partially replicated, so treat the
specific medium claim as `[moderate]` at best.

The robust part is not pen vs keyboard. It is **generative processing**: notes
that restate in your own words, ask questions, and record what you did not
understand beat notes that record what was said. A transcript is a recording,
not a note.

## The 10,000-hour rule

Gladwell's popularization flattened Ericsson's research into a number. The
original claim was about *deliberate* practice — structured, effortful,
feedback-driven — not about time served. Macnamara et al. (2014) found
deliberate practice explains a modest fraction of performance variance, and much
less in professions than in games and music `[moderate]`.

The damage is that "put in the hours" replaces "practice the thing you are bad
at with feedback". Those are different activities and only one of them works.

## Memorizing syntax

This one is genuinely changing, and it is the interesting case in this document.
Ten years ago, knowing the exact signature of a standard-library function was
part of competence because looking it up cost a context switch. Now an agent
produces it in a second.

What did *not* depreciate: knowing **what exists** and **what it costs**. You
still need to know that a hash map gives average O(1) and worst-case O(n), that
a database index is a B-tree and why range queries are cheap, that `JOIN` order
changes the plan. The syntax is free; the model is not.

So the rule is: stop drilling signatures, keep drilling *semantics and costs*.
`05` and `04` cover which of these are worth a card.

## Breadth-first bootcamp hopping

Learning five frameworks shallowly used to be a hedge. It is now close to
worthless, because the shallow layer is exactly what agents do well. What is
scarce is depth: one system you understand down to the failure modes
(`07-cs-roadmap.md`).

The tell is your own vocabulary. If you can only describe a technology by its
features, you learned the marketing. If you can describe how it fails, you
learned the technology.

## A note on "AI as first resort"

Not in the original list, but it belongs here. Asking an agent before
attempting recall is a *new* way to skip retrieval practice, and it is more
seductive than rereading because the answer is correct. See
[`03-learning-with-ai.md`](03-learning-with-ai.md) for the protocol. The
one-line version: **attempt first, ask second, verify third.**

## What to keep from all this

You do not need to delete your habits. You need to stop counting the ones that
produce no artifact you could be wrong about.

The replacement is always the same shape: produce something from memory, then
check it. That is what rereading, highlighting, and watching cannot do.

→ Next: [03 — Learning with AI](03-learning-with-ai.md)
