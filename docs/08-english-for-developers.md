# 08 — English for developers

Two different goals get confused here, and the confusion wastes years:

- **English as a subject** — grammar, exams, four skills in balance.
- **English as a tool** — read a spec, follow a conference talk, write a clear
  commit message, survive an interview.

For a CS student, the tool version pays first and pays continuously. The subject
version is worth doing, but it should not be the entry point, because it is
slow, abstract, and easy to abandon.

This document is about the tool version, with Anki as the retention layer.

## What actually predicts progress

| Factor | Evidence | Comment |
| --- | --- | --- |
| Amount of comprehensible input | `[moderate]` | Extensive reading meta-analyses (Nakanishi 2015) show a real but moderate effect |
| Vocabulary size | `[strong]` | Coverage thresholds are the best-established number in the field |
| Repeated encounters with a word in context | `[strong]` | Incidental learning needs roughly 8–10 encounters (Webb & Chang) |
| Output with feedback | `[moderate]` | Swain's output hypothesis; writing/speaking forces retrieval |
| Deliberate study of high-frequency words | `[strong]` | The 2,000 most frequent word families cover ~80% of running text |
| Grammar drills in isolation | `[practice]` | Low transfer; grammar is better learned as a by-product of input + output |

The single most useful number: **98% coverage** is roughly the threshold at
which you can read unassisted without constantly stopping (Hu & Nation 2000;
Laufer & Ravenhorst-Kalovski 2010). For novels that is around 8,000–9,000 word
families. For technical documentation the vocabulary is narrower and more
repetitive, so the threshold arrives much sooner — which is why a CS student can
read a framework's docs competently long before they can read a novel.

**Practical consequence:** do not try to learn "English vocabulary" in general.
Learn (a) the top ~2,000 general words to completion, then (b) the technical
register you actually meet. Everything else is better acquired by reading.

## The Four Strands, applied

Nation's framework says a balanced course needs four kinds of work. Applied to a
developer with 20 minutes a day:

| Strand | Share | What it looks like for you |
| --- | --- | --- |
| Meaning-focused input | ~40% | Read docs, changelogs, RFCs, error messages, blog posts. Listen to talks at 1× |
| Meaning-focused output | ~20% | Write commit messages, PR descriptions, code comments, a short technical note in English |
| Language-focused learning | ~25% | Anki for high-frequency words, collocations, and technical terms you keep meeting |
| Fluency development | ~15% | Reread something easy fast; shadow a talk; re-explain a concept in English without stopping |

The common failure is 100% input. You can read English for years and still
freeze when producing a sentence, because production is a different skill with a
different retrieval path.

## Why Anki helps here, and where it does not

Anki is excellent for the part of vocabulary that is **arbitrary**. That
`mitigate` means "make less severe" is a convention; there is no way to derive
it. Arbitrary mappings are exactly what spaced repetition is for.

Anki is poor for the part that is **compositional** — sentence structure,
discourse, register. Those need input and output, not recall.

So the rule: **card the arbitrary unit, read for everything else.**

### Card shapes that work

**1. Collocation cloze (the highest-value English card).**
> We need to {{c1::mitigate}} the risk, not eliminate it.

This teaches the word *and* its collocation (*mitigate a risk*, not *reduce a
risk* in formal writing). Word-level cards miss this entirely.

**2. Technical term in a real sentence.**
> The request is {{c1::idempotent}}, so retrying it is safe.

Better than "What does idempotent mean?" because it also encodes the *use*.

**3. Contrast pair.**
> `affect` is a {{c1::verb}}; `effect` is usually a {{c1::noun}}.

**4. Word family / morphology.**
> `robust` → noun: {{c1::robustness}}. The system lacks robustness.

**5. Reading-context recall (sparingly).**
> In a code review, "this is a nit" means {{c1::a minor style point, not a blocker}}.

That last one is register knowledge — high value for a developer, and almost
never taught.

### Card shapes that do not work

| Bad card | Why |
| --- | --- |
| "What does *ubiquitous* mean?" | Isolated rare word; you will meet it twice a year |
| Word → Vietnamese translation only | You learn a mapping, not a use. Also breaks the English-only habit |
| "List 5 synonyms of big" | Enumeration; and synonyms are rarely interchangeable |
| A card for every unknown word in an article | Deck bloat, 90% of it never reviewed |
| Grammar rule cards ("when do you use present perfect?") | Rules are not retrieval units; they need examples |

The bloat risk is specific and severe for English. A student reading an article
can generate 40 cards. Twelve of them are worth keeping. The filter: **would I
use this word in writing or speech this month?** If no, do not card it — look it
up again later, or let context teach it.

## Reading: the highest-leverage habit

For a developer, reading is the skill that compounds. Concretely:

1. **Read documentation in English, always.** Never switch to a translated
   version. Documentation is the one genre where you get dense, repeated,
   context-rich input on exactly the vocabulary you need.
2. **Read error messages slowly.** They are a controlled vocabulary — the same
   200 phrases recur for your entire career. Learning to parse them exactly is
   worth more than any grammar book.
3. **Read one RFC or design doc per month**, even partially. The register
   ("MUST", "SHOULD", "in the absence of") is the register of every spec you
   will ever read.
4. **Read changelogs.** Free, short, and they teach you how versioning language
   works.

Target: 20–30 minutes a day of real English text you actually want to read.
Comics, forums, and man pages all count. Graded readers do not, for you — you
are past that level and they will bore you into quitting.

## Listening and speaking

- **Listening:** conference talks (1×, no subtitles first, then with). The goal
  is parsing connected speech, not comprehension of ideas — you already know the
  ideas.
- **Shadowing:** play 30 seconds, repeat aloud simultaneously, matching rhythm.
  This is the fastest fix for the "I can read but I cannot speak" gap `[practice]`
  but it is well-established in pronunciation teaching.
- **Speaking:** the cheapest version is talking to an AI in English about your
  own work — explaining a design decision, a bug, a trade-off. You are
  practicing production, not conversation. Record it and listen back once.

Speaking matters most for interviews, which are the highest-stakes English
event in a developer's life. Practice describing your projects in English before
you need to.

## A minimal English loop

| When | What | Minutes |
| --- | --- | --- |
| Daily | Anki English deck (due cards only) | 5 |
| Daily | Read something you want to read, in English | 20 |
| Weekly | Write one technical paragraph in English (PR, note, comment) | 15 |
| Weekly | Shadow one talk segment | 10 |
| Monthly | Re-read an old note of yours and fix the English | 15 |

That is under 40 minutes a day and it is enough to keep improving for years,
because it is all real use rather than study.

## The trap

The trap is treating English as a prerequisite: "I will learn English, then
learn programming properly." That order is backwards and slow. Do the technical
work in English from day one, badly, with a dictionary open. The vocabulary
arrives because you needed it, which is the only reason vocabulary ever sticks.

→ Next: [09 — The weekly loop](09-weekly-loop.md)
