# 07 — CS roadmap in the AI era

This is not a curriculum. It is an argument about **what to go deep on**, and a
sequenced path that builds one system instead of twenty tutorials.

The premise: an agent can now produce competent code for well-specified,
well-bounded problems. What it cannot do is own a system, notice that the
specification is wrong, or debug a failure it did not cause. Those are the
scarce skills, and they are all depth skills.

## What AI commoditized

| Commoditized | Why it collapsed |
| --- | --- |
| Boilerplate CRUD, scaffolding, form validation | Fully specified, pattern-heavy, cheap to verify |
| Simple scripts and glue code | Small blast radius, easy to check by running |
| Translating code between languages | Mechanical, and errors surface immediately |
| Routine unit tests for obvious behaviour | Generated faster than written |
| Summarizing docs, writing first-draft README | Low stakes, easily reviewed |
| Recalling exact API signatures | Lookup cost went to zero |

If your plan is "get good at the things on this list", you are training for a
job that is being automated while you train.

## What it did not commoditize

| Scarce | Why agents are bad at it |
| --- | --- |
| Debugging a system you did not write | Requires a model of the system that is not in the context window |
| Performance reasoning | Needs measurement, not generation; agents guess at hot paths |
| Correctness under concurrency | The failure modes are non-local and hard to test |
| Data modelling | Depends on future requirements nobody wrote down |
| Security | Requires adversarial thinking against an unspecified attacker |
| Writing the specification | The agent executes a spec; deciding what to build is the job |
| Code review judgment | Knowing which of 40 plausible diffs is wrong |
| Knowing when not to use AI | Taste, and accountability |

Notice that most of these are **systems** skills, not **syntax** skills. That is
the whole strategic picture.

## The enduring core

What a CS degree is actually for, ranked by how much it pays rent in the AI era:

| Subject | Learn it | Why |
| --- | --- | --- |
| Data structures & algorithms | Deeply | Not for interviews — for reasoning about cost. This is the vocabulary of every performance conversation |
| Operating systems | Deeply | Processes, memory, scheduling, syscalls. Every mysterious production failure lives here |
| Databases | Deeply | Indexes, query plans, transactions, isolation levels. Most slow software is a database problem wearing a costume |
| Networks | Deeply | Latency, TCP behaviour, DNS, TLS. Distributed systems are networks with more failure modes |
| Discrete math, probability | Deeply | Probability is the language of performance, caching, and ML |
| Compilers / language theory | Moderately | Not to build one; to understand why a language behaves as it does |
| Linear algebra | Moderately | Only if you touch ML, graphics, or search |
| Calculus | Skim | Rarely load-bearing for a working engineer |
| Formal methods | Skim, then revisit | High value in specific domains (protocols, safety) |

The pattern: **cost, failure, and state**. Everything worth learning deeply is
about what something costs, how it fails, and where the state lives.

## AI-era literacy (the new layer)

This is the part a 2015 curriculum does not cover, and it is smaller than the
hype suggests.

| Skill | What it actually means | Stability |
| --- | --- | --- |
| Specification writing | Turning a vague goal into acceptance criteria a machine can be held to | Stable — this is just clear thinking |
| Evaluation | Building the test set that tells you whether output is correct. Property-based, differential, and adversarial tests | Stable |
| Reading diffs critically | Reviewing agent output for the failure the tests miss | Stable |
| Context engineering | Deciding what the model sees: files, examples, constraints | Churning |
| Tool/agent orchestration | Composing agents, tools, retries, and human checkpoints | Churning fast |
| Failure-mode awareness | Hallucination, silent wrongness, over-broad edits, confident nonsense | Stable in kind, changing in detail |
| Cost and latency awareness | Tokens, caching, batching, streaming | Churning |

Rule of thumb: **anything about thinking is stable; anything about a specific
framework is churning.** Learn the stable layer properly and treat the churning
layer as a weekly skim.

### What the data actually says

The honest summary of 2025–2026 evidence: AI helps on greenfield, well-specified
work, and can *slow down* experienced developers on mature codebases. Both are
true at once.

| Finding | Source | Confidence |
| --- | --- | --- |
| 55.8% faster on a well-specified greenfield task (HTTP server) | GitHub Copilot RCT, Peng et al. 2023, [arXiv:2302.06590](https://arxiv.org/abs/2302.06590) | `[moderate]` — one task, narrow |
| 19% *slower* for experienced OSS devs on their own mature repos | METR RCT 2025, [metr.org](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | `[moderate]` — devs believed they were faster |
| 45% of developers say debugging AI-generated code is time-consuming; 46% distrust accuracy vs 31% who trust it | Stack Overflow Developer Survey 2025, [survey.stackoverflow.co/2025](https://survey.stackoverflow.co/2025/ai) | `[moderate]` — self-report, large N |
| Code duplication rose sharply as AI adoption rose (211M changed lines analysed, ~4× more cloning) | GitClear 2025, [gitclear.com](https://www.gitclear.com/ai_assistant_code_quality_2025_research) | `[moderate]` — vendor data, methodology not fully public |
| Entry-level (22–25) employment in AI-exposed roles fell relative to older cohorts | Stanford Digital Economy Lab, Brynjolfsson et al. 2025, [digitaleconomy.stanford.edu](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/) | `[moderate]` — correlational, not causal |

Read together: the tool is a multiplier on **specification quality and
verifiability**. Where those are high, it wins big. Where the task is
"understand and change a system you did not write", it can cost you time. That
is exactly why the scarce skills below are the ones worth training.

Two clichés to discard: *"AI won't replace you, someone using AI will"* — the
2025 data does not support the confident version of this. And *"just learn to
prompt"* — prompting is a two-week skill, not a career.

### The evaluation ladder

"Evaluation" is the AI-era skill people name and then fail to define. It is a
ladder, cheapest first:

| Level | What you write | Catches | Cost |
| :-: | --- | --- | --- |
| 1 | Example tests: known inputs → known outputs | Obvious breakage | Minutes |
| 2 | Property-based tests: invariants over generated inputs | Edge cases you did not imagine | Hours |
| 3 | Differential tests: compare against a slow-but-correct reference implementation | Subtle divergence in optimised code | Hours |
| 4 | Golden / replay tests: record real inputs and outputs, diff on every change | Regressions in LLM features, where there is no single right answer | Days |
| 5 | Human diff review with a written rubric | The failure the tests encode as acceptable | Always |

Level 4 is the one nobody teaches and every AI feature needs. If your product
calls a model, you cannot assert equality — you assert *stability* and *bounds*.

### How agent-assisted work actually fails

| Failure | What it looks like | How you detect it |
| --- | --- | --- |
| Hallucinated API | Confident call to a method that does not exist | Compile + type check, every time |
| Silent wrongness | Code runs, output is subtly incorrect | Tests that assert semantics, not shapes |
| Over-broad edit | Twelve files changed for a one-line fix | Read the full diff before accepting |
| Test gaming | Agent edits the test to match the bug | Review test diffs with the same suspicion as source |
| Injected instructions | A comment or docstring in the repo steers the agent | Treat repo content as untrusted input |
| Cost runaway | Retry loops, huge contexts, no budget | Hard token/time caps per task |

None of these are exotic. They are the normal failure surface, and each has a
cheap countermeasure. Learn the countermeasures before you learn the frameworks.

## The spine: one system, evolved

Instead of a list of topics, build one system and keep making it harder. Each
phase adds a constraint that forces you to learn the next layer. This is the
only structure that produces depth without a syllabus.

**The system:** a small service you own end to end. A URL shortener is fine. A
pastebin is fine. What matters is that you operate it and it can fail.

| Phase | Time | Constraint added | What you are forced to learn | Project milestone |
| --- | --- | --- | --- | --- |
| 1 | 4–6 wk | It must run from the command line, with tests | One language properly, git, testing, error handling | CLI tool, 80% test coverage, clean history |
| 2 | 6–8 wk | It must serve HTTP to real clients | Networking, HTTP semantics, statelessness, input validation | Server handling 1k req/s locally |
| 3 | 8–10 wk | Data must survive a restart, and queries must be fast | Databases, indexes, query plans, transactions | Persistent store with an index you can explain |
| 4 | 6–8 wk | It must handle concurrent users without corrupting data | Concurrency, locking, isolation, idempotency | Load test that finds your race condition |
| 5 | 6–8 wk | It must be observable and deployable | Logging, metrics, tracing, CI/CD, containers | Deployed, with a dashboard you actually read |
| 6 | 6–8 wk | It must survive an incident | Failure analysis, capacity, rollback, postmortems | A written incident report about your own outage |

Roughly 9–12 months of part-time work. At the end you have one system you
understand down to the failure modes, which is worth more than ten tutorials.

**What to deliberately not learn yet:** Kubernetes internals, five frontend
frameworks, microservices patterns, blockchain, "AI agents" as a product, the
newest language. None of them are prerequisites for depth, and all of them are
comfortable places to hide.

### Why a spine and not a topic list

A topic list lets you study the interesting parts and skip the parts that hurt.
A system forces the order: you cannot understand the index before the query is
slow, and you cannot understand the race condition before you have concurrency.
The constraint generates the curriculum.

## Where Anki fits

| Card it | Do not card it |
| --- | --- |
| Complexity of named operations | Design trade-offs |
| Protocol fields and handshake order | Debugging process |
| SQL semantics (`NULL` in aggregates, isolation levels) | Query tuning intuition |
| Git commands and their effects | Architecture decisions |
| Syscall behaviour and errno meanings | "How to structure a project" |
| Language idioms that recur | Anything you will look up once |

The line is the same as `04`: **facts that are stable, arbitrary, and needed
cold.** Everything in the right column is learned by doing, reviewed by writing,
and retained by using.

A good signal that you are carding correctly: your deck grows slowly and your
projects get harder. A bad signal: the deck grows fast and the projects stay the
same size.

## Proof of work in 2026

| Signals competence | Noise |
| --- | --- |
| A working system with real constraints (load, failure, data volume) | A clone of a tutorial app |
| A design document explaining a trade-off you actually faced | A list of 20 technologies on a CV |
| An incident write-up with a root cause | Certificate stacks |
| An open-source PR that survived review | "Built a todo app in 5 frameworks" |
| A benchmark you ran yourself, with methodology | Claiming performance without measurement |
| Code someone else had to maintain | Code only you have read |

The common thread: **evidence that something was hard and you handled it.**
Agents make it easy to produce volume. Volume is now the cheapest signal, so it
is worth the least.

## Honest risks

**Shallow fluency.** You can produce working software without understanding it.
It passes tests, ships, and fails at scale in a way you cannot diagnose. The
countermeasure is the spine: operate something, and let it break.

**Dependency.** The first time you are offline or the model is down, you find
out what you actually know. Keep one skill agent-free (`03`).

**Evaluation blindness.** If you cannot tell whether output is correct, you are
not engineering, you are gambling. Build the test before the feature.

**Taste erosion.** Design judgment comes from having maintained bad code. If you
never maintain anything, you will keep choosing the option that demos best.

None of these are solved by studying harder. They are solved by owning
something for long enough that it becomes embarrassing.

→ Next: [08 — English for developers](08-english-for-developers.md)
