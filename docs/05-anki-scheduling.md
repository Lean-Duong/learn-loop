# 05 — Anki scheduling

Card design is the part that matters. Scheduling is the part that is easy to
get wrong in ways that cost you months.

Two rules before anything else:

1. **Turn FSRS on.** It is not the default, and it is the single biggest
   improvement over the legacy scheduler.
2. **Change almost nothing else.** Nearly every Anki settings guide you will
   find describes a scheduler you are not running.

Version note: the specifics below reflect Anki 26.x (late 2026). Version-dependent
claims are tagged; re-check them when you upgrade, because this is the one part
of this repo that rots.

## FSRS vs SM-2

**SM-2** is the legacy scheduler: one ease factor per card, multiplied into the
previous interval. Its structural failure is **ease hell** — repeated failures
permanently depress a card's ease factor, so its intervals stay short forever,
and you respond by adding learning steps, which makes it worse. `[strong]` as a
description of the mechanism; the outcome difference is well documented in Anki's
own manual.

**FSRS** is a fitted model of forgetting with three variables per card:

| Variable | Meaning |
| --- | --- |
| **D** — difficulty | How hard this item is for you |
| **S** — stability | The interval at which retrievability decays to 90% |
| **R** — retrievability | Probability you recall it now, computed from elapsed time and S |

A review updates (D, S) from your grade and the delay; the next interval is when
R is predicted to hit your desired retention. "Optimize" runs gradient descent
over your own review log, so the parameters are personal by construction.

Origin: Ye, Su & Cao, KDD '22 (`10.1145/3534678.3539081`), implemented in Rust
as `fsrs-rs`.

The practical consequence: **there is no ease factor to get stuck.** That is why
the elaborate learning-step ladders people built to escape ease hell are now
pointless — they were a workaround for a scheduler you are no longer using.

## Is it the default?

No. As of Anki 26.x you still enable it explicitly: *Deck options → FSRS →
Enable FSRS*. The manual still calls it "an alternative to the legacy SM-2
algorithm", and the maintainer's tracking issue "Make FSRS the default?"
(#3616) remained open as of late 2026.

This matters because a lot of current guides claim otherwise. If a guide says
"FSRS has been the default since 23.10", it is wrong, and the rest of its
settings advice is probably wrong too.

Timeline, for orientation:

| Version | Change |
| --- | --- |
| 23.10 | FSRS integrated (opt-in) |
| 25.07 | FSRS-6; "Compute minimum recommended retention" (CMRR) removed |
| 25.09 | Desired retention configurable per deck |
| 26.x | `fsrs-rs` updates, cloze-inside-MathJax fixes |

Enabling is global — you cannot run FSRS on one preset and SM-2 on another.

## The settings that matter

| Setting | Value | Why |
| --- | --- | --- |
| Desired retention | **0.90** | The single most important setting. Above 90% workload rises steeply; above 97% it is unmanageable |
| FSRS parameters | Optimize monthly, never hand-edit | The manual forbids copying parameters from anyone else — they are fitted to *your* memory |
| Learning steps | `10m` | Steps of 1 day or more are counterproductive under FSRS |
| Maximum interval | leave at default | Lowering it only increases workload |
| New cards/day | 10–20 | 20 new/day converges to ~200 reviews/day. That is the ceiling of a sustainable habit |
| Bury siblings | on | Two cards from one note never land on the same day — cheapest interference fix available |
| Easy days | one light day | Native since 24.11, works with FSRS |
| Review order | ascending retrievability | The FSRS-appropriate replacement for "relative overdueness" |
| Reschedule on change | off | Can dump a huge due pile at once |

That is the whole configuration. Nine rows.

## The arithmetic worth doing once

Interval scales with `ln(desired retention)`. So:

- 90% → 95% multiplies intervals by ≈0.49, i.e. **roughly doubles your reviews**
- 90% → 85% multiplies intervals by ≈1.54, i.e. **cuts reviews by about a third**

The curve is convex: the last few points of retention are the expensive ones.
This is why 0.90 is the default and why "I want 97%" is a decision to spend your
life in the review screen.

Rule of thumb: 0.90 normally; 0.85 if reviews are crowding out new material;
0.93 only for a deck attached to an exam date.

## What is noise

| Advice you will see | Reality |
| --- | --- |
| "Use learning steps `1m 10m 1d 4d 10d`" | An ease-hell workaround. Under FSRS, repeating a card within a day barely contributes to long-term memory |
| "Tune the maximum interval" | Nobody hits the cap. Tuning it is procrastination |
| "Copy these FSRS parameters" | The manual explicitly forbids it. Parameters are personal |
| "Click Compute minimum recommended retention" | **Removed in 25.07.** Guides still tell you to |
| "You need 1,000 reviews before Optimize works" | Obsolete since 24.06.3 |
| "Install FSRS Helper for X" | Most of it is native now. Its own README calls it "an added bonus, not recommended for extensive use". Two features still matter: Disperse Siblings and Remedy Hard Misuse |
| "Tune easy bonus / interval modifier / hard interval" | These are **hidden** under FSRS. Advice about them is advice about a scheduler you are not running |

If you are spending time on any row in that table, you are not studying.

## A concrete configuration for 30–60 min/day

One preset per subject family — `CS` and `English` — not per chapter. Presets
per chapter are a maintenance burden with no benefit.

```
FSRS:              on, optimize monthly
Desired retention: 0.90
Learning steps:    10m
Max interval:      default
New cards/day:     15 (hard cap 20)
Review cap:        200
Bury siblings:     on
Easy days:         Sunday light
Reschedule:        off
Review order:      ascending retrievability
```

Converges to roughly 150 reviews/day ≈ 15–20 minutes at 6–8 seconds per card,
plus 5–8 minutes of new cards. That is the 30–60 minute budget in
[`09-weekly-loop.md`](09-weekly-loop.md).

## Note types

| Type | Use it when | Trap |
| --- | --- | --- |
| `Basic` | One direction is a real retrieval task | — |
| `Basic (and reversed card)` | Both directions are unambiguous (L2↔L1 vocabulary) | For technical facts the reverse is usually ambiguous: "which algorithm is O(log n)?" has many answers |
| `Basic (optional reversed card)` | Best default for a generator — reversal is a per-note decision | — |
| `Basic (type in the answer)` | The exact string matters (flags, keywords) | Typing cost; use sparingly |
| `Cloze` | The fact lives in a sentence; enumerations | Cannot be created from a regular note type |
| `Image Occlusion` | Diagrams | Irrelevant for text material |

## Formatting traps that silently corrupt cards

These are Anki-specific and cost real debugging time. They belong in any
generator's validation step (`06`).

| Trap | Symptom | Fix |
| --- | --- | --- |
| Raw `<` in a code field | Text silently vanishes — `<T>` is parsed as an HTML tag | Escape as `&lt;T&gt;` |
| `}}` inside a cloze | Cloze terminates early, rendering breaks | Space it (`} }`) or use `<!-- -->` |
| `::` inside cloze text | Parsed as the cloze *hint* separator | `std:<!-- -->:variant` |
| `[$]...[/$]` | Needs a local LaTeX install, disabled by default, **fails silently** | Use MathJax `\(...\)` |
| Tabs inside a TSV field | Import columns shift | Spaces for indentation, always |
| Long lines in `<pre>` | Overflow off-screen | `white-space: pre-wrap` in template CSS |

MathJax and LaTeX image generation are two different mechanisms and are
routinely confused. MathJax (`\(...\)`) is client-side, needs no install, and
works on every platform. LaTeX image generation (`[latex]...[/latex]`, `[$]...[/$]`)
shells out to a local LaTeX install and writes a PNG. For anything automated:
**emit MathJax only.**

## How to know the schedule is working

| Signal | Meaning |
| --- | --- |
| True retention 85–90% | Healthy. Below 80%: too many new cards, or bad cards |
| Typical grades ~5–20% Again | If you are pressing Again far more often, the cards are wrong, not your discipline |
| Review time per card 6–8 s | Above ~12 s average, cards are too big |
| Leeches < 5 per 100 cards | More means a card-design problem |

The one that surprises people: under FSRS, a high Again rate is a **card
diagnostic**, not a willpower diagnostic. If you fail a quarter of your reviews,
fix the deck before you add discipline.

→ Next: [06 — AI deck pipeline](06-ai-deck-pipeline.md)
