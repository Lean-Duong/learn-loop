# 03 — Learning with AI

Most writing on this topic is either "AI will replace learning" or "AI is just a
tool". Both are useless. The useful question is narrower: **which parts of the
learning loop can an agent take over without breaking the loop?**

Short answer: agents are excellent at feedback, explanation-on-demand,
generating practice material, and being a critic. They are dangerous at the one
step that produces durable memory — producing the answer yourself.

## What the recent evidence actually shows

| Study | Design | Finding | Confidence |
| --- | --- | --- | --- |
| Kosmyna et al. (2025), MIT Media Lab, *Your Brain on ChatGPT* | 54 participants, EEG, essay writing across sessions; LLM vs search vs brain-only | LLM group showed the weakest neural connectivity during writing and could not quote from their own essay afterwards. When the LLM group was switched to brain-only in a later session, connectivity was still reduced | `[moderate]` — small n, preprint, one task |
| Lee et al. (2025), Microsoft Research + CMU, CHI | Survey of 319 knowledge workers, 936 examples | Higher *confidence in AI* predicted less critical thinking; higher *self-confidence* predicted more. People offload thinking when the tool feels reliable | `[moderate]` — self-report |
| Bastani et al. (2024), Wharton | ~1,000 high-school students, math practice | GPT-4 tutor improved practice performance by ~48% but students did **17% worse** on exams without access. The answer-giving variant helped practice more and exams not at all | `[moderate]` — strong design, narrow domain |
| Fan et al. (2025), BJET | Essay writing with ChatGPT vs expert vs no AI | Better essays with AI, weaker self-regulation, no retention advantage | `[moderate]` |
| Kestin et al. (2025), Harvard | AI tutor in an intro physics course | Roughly doubled learning gains in less time than active-learning class | `[moderate]` — and it is the counter-example |

Read together, these are not contradictory. The pattern is:

- **AI that explains and questions, and withholds answers, helps.**
- **AI that answers on demand improves performance and degrades learning.**
- **The degradation is invisible in the moment** — you feel faster and better.

Bastani's 48%-better-practice / 17%-worse-exam split is the cleanest statement
of the problem: the metric you can see improves while the metric you care about
falls.

## The 2-sigma myth, because every AI tutor sells it

Bloom (1984) observed that one-on-one tutoring produced outcomes about two
standard deviations above conventional group instruction. That single number is
the marketing foundation of the entire AI-tutoring industry, and it is weaker
than it looks.

- It was not one experiment. It was an extrapolation across several small
  studies, assembled to argue a research agenda.
- Meta-analyses of actual human tutoring find much smaller effects — roughly
  d ≈ 0.4–0.8 depending on what you compare against, not 2.0. `[strong]`
- **No AI system has reproduced 2σ on a well-controlled measure.** Kestin's
  "doubled gains" is consistent with d ≈ 0.5–0.9. Excellent — and a third of the
  claimed ceiling.

Practical consequence: expect a moderate, real improvement from a well-designed
AI tutor, and be suspicious of any product quoting 2σ. The effect size is not
the point anyway; the design that produces it is. Tutors help when they withhold
answers, ask for explanations, and give feedback — all of which `04` and `09`
build into the loop.

## The mechanism: offloading, not laziness

Cognitive offloading (Risko & Gilbert, 2016) is the normal human strategy of
moving mental work to the environment — writing a shopping list, using a
calculator. It is not a moral failure, and it is usually adaptive.

The problem is that **retrieval and generation are the learning events**. If the
agent generates, the agent learns. There is no transfer of the benefit back to
you, the way there is with a calculator, because the calculator was never
supposed to change your arithmetic ability.

Two specific losses:

**Generation effect.** Material you generate yourself is remembered better than
material you read (Slamecka & Graf 1978; Bertsch et al. 2007 meta-analysis
`[strong]`). An agent's explanation is read material. This is why "explain it to
me" feels great and teaches little, and why "explain it back to me and I will
tell you what is wrong" works.

**Metacognitive accuracy.** You cannot feel the difference between understanding
and recognizing. Rereading exploits this; AI exploits it harder, because the
output is fluent, confident, and usually correct. Your error signal — the thing
that tells you to go back and study — never fires.

## What agents are genuinely good at

Use them here without guilt:

1. **Immediate, specific feedback.** The bottleneck in deliberate practice is
   feedback latency. A reviewer that responds in ten seconds beats one that
   responds in a week. This is where the Harvard result comes from.
2. **Explaining the same thing four ways.** A good human tutor does this; a
   textbook cannot. Asking for the same concept at three levels of abstraction
   is legitimate and cheap.
3. **Generating practice items and adversarial questions.** "Give me five
   problems that look like binary search but are not" is a real use.
4. **Being a critic, not an author.** "Here is my explanation — find the gap"
   preserves the generation effect because *you* generated first.
5. **Scheduling and bookkeeping.** FSRS optimization, deck hygiene, duplicate
   detection. Pure overhead, no learning value in doing it by hand.
6. **Reading the thing you cannot read yet.** Dense papers, unfamiliar
   codebases. Legitimate, as long as you then reconstruct the argument yourself.

## What agents are bad at

1. **Answering your question before you tried.** The single highest-cost
   mistake, and the default behaviour of every chat interface.
2. **Telling you what to learn next.** They will happily produce a 14-phase
   curriculum. It will be plausible, generic, and not matched to what you
   actually cannot do.
3. **Judging your competence.** Fluency in the output does not mean you have
   the skill. Only a cold retrieval attempt or a real project tells you.
4. **Anything where being subtly wrong is expensive.** Hallucinated APIs,
   deprecated syntax presented as current, invented citations. The error rate is
   low enough to be trusted and high enough to hurt.

## The protocol

Six rules. They fit on a card.

1. **Attempt before asking.** Write your answer, your guess, your broken code
   first. Even a wrong attempt changes what the explanation does to you.
2. **Ask for questions, not answers.** "What should I be able to answer about
   X?" beats "explain X".
3. **Make the agent a critic.** Paste your explanation, your solution, your
   design. Ask what is wrong, not what is right.
4. **Never accept a fact you cannot source.** If it matters enough to remember,
   it matters enough to verify against a primary source — a man page, a spec, a
   paper.
5. **Close the loop by hand.** Whatever the agent produced, reproduce it from
   memory once. The reproduction is the learning event.
6. **Keep one thing agent-free.** Pick the skill you most want to own and never
   delegate it, not even for convenience. For a CS student this is usually
   debugging and system design.

The test of whether you are using AI well is not "did it help me finish". It is
**"could I do this without it next month?"** If the answer stays no for months,
the tool is not augmenting you, it is replacing you.

## The uncomfortable part

The MIT and CMU results point at something worse than skill loss: the loss is
not felt. Participants in the LLM condition did not report being worse off. They
reported the task as easier. That is the definition of a bad feedback loop — the
cost is deferred and invisible, and the benefit is immediate.

The only defence is structural, not motivational: rules that force generation
before consumption, built into your routine so they do not depend on willpower
on a bad day. That is what [`09-weekly-loop.md`](09-weekly-loop.md) is for.

## Using AI for Anki, specifically

This is the part people get wrong most often, so it has its own document:
[`06-ai-deck-pipeline.md`](06-ai-deck-pipeline.md). The short version — an agent
is good at *finding candidate facts and drafting prompts*, and bad at *deciding
what is worth remembering* and at *not hallucinating*. So the pipeline is:
agent drafts, human selects, agent audits for mechanical defects, human
spot-checks.

→ Next: [04 — Anki card design](04-anki-card-design.md)
