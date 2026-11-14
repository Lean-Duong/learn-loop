# Bad cards, and the fix

Four real failure modes. Read these before auditing a generated deck — they are
easier to recognize than to describe.

---

## 1. Enumeration

**Bad**
> Front: What are the four ACID properties?
> Back: Atomicity, Consistency, Isolation, Durability

You will learn *that there are four*. You will not reliably learn which one
does what, and when you miss one you cannot tell which.

**Fixed** — one card per property, each cued by a scenario:

> Front: A transfer debits one account and credits another; the process crashes
> between the two writes. Which ACID property is violated?
> Back: Atomicity

> Front: Which ACID property guarantees concurrent transactions produce a result
> equivalent to some serial order?
> Back: Isolation

---

## 2. Answer leakage

**Bad**
> Front: Which data structure gives O(1) average lookup by hashing keys?
> Back: Hash table

Nothing was retrieved. The front already contains "hashing keys".

**Fixed**

> Front: Average-case lookup cost of a hash table?
> Back: O(1)

Or, if the fact you actually want is the *trade-off*:

> Front: A hash table has O(1) average lookup. What is its worst-case lookup
> cost, and why?
> Back: O(n) — all keys collide into one bucket

---

## 3. Orphan context

**Bad**
> Front: What does it return when the list is empty?
> Back: None

Written while reading a paragraph. Six months later "it" is nothing.

**Fixed**

> Front: In Python, what does <code>min([])</code> raise?
> Back: <code>ValueError: min() arg is an empty sequence</code>

---

## 4. Multi-step reasoning

**Bad**
> Front: What is the output of this loop?
> <pre><code>s = 0
> for i in range(1, 5):
>     for j in range(i):
>         s += j
> print(s)</code></pre>
> Back: 10

This is a practice problem. It tests tracing, not retrieval, it takes 30+
seconds, and one wrong step means you grade it "again" without learning which
step was wrong. Anki will schedule it as if it were a fact.

**Fixed** — card the *fact* the exercise was teaching, and put the exercise in
your interleaved practice set:

> Front: Sum of <code>range(n)</code>?
> Back: <code>n(n-1)/2</code>

---

## The general shape

| Bad card is | Because | Fix |
| --- | --- | --- |
| A list | Tests "how many", not "which" | One card per item |
| Self-answering | No retrieval occurs | Remove the giveaway term |
| Context-free | Unreadable later | Name the subject |
| A computation | Tests procedure, not memory | Card the underlying fact |

If a card cannot be graded in under ten seconds and for the right reason, it is
not a card. It is an exercise wearing a card's clothes.
