# 09 — The weekly loop

If you read one document in this repo, read this one. The rest is justification.

The design constraint is real life: classes, a part-time job, family, and the
fact that motivation is not a stable input. A system that requires a good week
is not a system.

So: **one loop, one deck, one project, one book.** Everything else is optional.

## The loop

```
   read / watch  ──►  attempt by hand  ──►  card the gaps  ──►  review daily
        ▲                                                        │
        └────────────────────────────────────────────────────────┘
```

Four steps. The one people skip is step two, and it is the only step where
learning happens.

1. **Read** one thing properly (not five things shallowly).
2. **Attempt** — close the source, write the code, answer the question, draw the
   diagram. Badly is fine. This is the generation event.
3. **Card the gaps** — only the things you failed to retrieve, and only if they
   are single retrievable units (`04`).
4. **Review** — daily, due cards only, 10–20 minutes.

## Daily block (45–75 min)

| Minutes | Activity | Notes |
| --- | --- | --- |
| 10–15 | Anki, due cards only | Never add new cards here; new cards are a weekly decision |
| 30–45 | Deep work on the current project or topic | One thing. No tab switching |
| 5–10 | Attempt-from-memory | Close everything and reproduce what you just learned |
| 5 | English Anki | Separate deck, collocation clozes |

The order matters more than the durations: **review first**, because it is the
thing you will skip if it comes last, and because it primes the topic you are
about to work on.

## Weekly block (90–120 min, one sitting)

1. **Pick next week's one topic** (10 min). One. Not three.
2. **Write 10–20 new cards by hand** from this week's material (30 min). Hand,
   not generated — at least for the first months.
3. **Audit the deck** (15 min): delete leeches, split multi-fact cards, fix
   orphan context. Run
   [`templates/card-quality-checklist.md`](../templates/card-quality-checklist.md).
4. **Interleaved practice set** (30 min): 6–8 problems from *different* past
   topics, chosen so you cannot tell the category from the heading.
5. **Write 5 lines of English** about what you learned (10 min). A commit
   message, a note, anything real.

That is the whole system. Two hours a week of deliberate structure plus a daily
hour.

## Monthly block (45 min)

- Read your own notes from the month. Anything you cannot reconstruct is a gap —
  either card it or delete the note.
- Check deck health: retention rate, leech count, cards with `lifecycle::ephemeral`
  that have expired.
- Kill one thing. A topic, a subscription, a side project. Depth requires
  subtraction, and nothing else enforces it.

## Time budget

| Layer | Per week | What it buys |
| --- | --- | --- |
| Daily loop | ~7 h | The floor. Without this nothing else matters |
| Weekly block | ~2 h | Deck quality and interleaving — the two things that decay silently |
| Monthly block | ~45 min | Pruning |
| **Total** | **~10 h** | A semester of real progress alongside coursework |

If you have less than 7 hours a week, cut the weekly block to 45 minutes before
you cut the daily review. Review is the compounding part.

## The bad-week protocol

Some weeks you will have 20 minutes total. Do exactly this, in this order, and
nothing else:

1. **Anki due cards.** 10 minutes. Even on the worst day.
2. **One attempt-from-memory** of anything you studied recently. 5 minutes.
3. Stop.

Do not "catch up" afterwards. Catching up means doubling the review queue, which
produces a 200-card day, which produces a skipped week, which produces quitting.
Let the backlog be a backlog; FSRS will spread it out. The only unrecoverable
failure is stopping the review entirely.

## What to cut, in order

When the system is too heavy:

1. Cut the English shadowing (lowest marginal return).
2. Cut the weekly interleaved set to 4 problems.
3. Cut new cards to zero for a week (keep reviewing).
4. Cut the project to maintenance.
5. **Never** cut daily review. That is the one thing that compounds.

## Metrics that are worth watching

| Metric | Healthy | Meaning if it drifts |
| --- | --- | --- |
| True retention (FSRS) | 85–90% | Below 80%: too many new cards, or cards are bad |
| Leeches per 100 cards | < 5 | High: card design problem, not discipline |
| Cards added per week | 10–25 | Higher: you are carding instead of learning |
| Days with a review | 6–7 / week | Below 5: the loop is broken, fix the trigger not the will |
| Problems solved without looking | rising | The only metric that reflects actual skill |

Card count is not a metric. Deck size is not an achievement. A 5,000-card deck
reviewed badly is worse than a 400-card deck you actually know.

## Why this shape

Every element maps to evidence in `01`:

- **Daily review** — spaced repetition, the one large reliable effect.
- **Attempt-from-memory** — retrieval practice, the other one.
- **Interleaved weekly set** — the technique Anki cannot give you.
- **Hand-written cards** — generation effect; you learn the material while
  writing the card.
- **Monthly pruning** — keeps the deck from becoming an obligation you resent.

Nothing here is novel. That is the point. A system you follow for two years
beats an optimal system you follow for three weeks.

→ Next: [10 — Sources](10-sources.md)
