# Python — Sum of Products Till n

Generate a sequence defined by a recurrence and compute the sum of the products of each pair of consecutive terms, using a single loop and constant memory.

---

## Problem Statement

A sequence is defined by:

```
a(1)   = 1
a(n+1) = 1 / (1 + 1/a(n))
```

Given `n`, compute:

```
(a1 * a2) + (a2 * a3) + ... + (a(n-1) * a(n))
```

**Example**

```
Enter n : 4
The sum is : 0.75
```

---

## Solution

```python
"""
a(n+1)=1/(1+(1/a(n))))
a1=1
(a1*a2)+(a2*a3)+........(a(n-1)*an)=??
"""
n=int(input("Enter n : "))
ca=1.0
ts=0.0

for i in range(1,n):
    na=1/(1+(1/ca))
    ts+=(ca*na)

    ca=na

print(f"The sum is : {ts}")
```

---

## The Critical Idea

Keep only **two things** at any moment: the current term (`ca`) and the next term (`na`). Each loop iteration:

1. Computes the next term from the current one.
2. Adds their product to the running sum.
3. Slides forward: the next term becomes the current term.

No list of terms is needed, because each product only uses two neighbouring terms.

---

## How the Loop Works

| Variable | Meaning                            |
| -------- | ---------------------------------- |
| `ca`     | Current term, starts at `a1 = 1.0` |
| `na`     | Next term, `1 / (1 + 1/ca)`        |
| `ts`     | Running total of products          |

`range(1, n)` runs **n − 1 times**, which matches the number of products: a pair is needed for each of `(a1·a2)` through `(a(n-1)·a(n))`.

---

## Pseudocode

```
ca = 1.0
ts = 0.0
repeat n - 1 times:
    na = 1 / (1 + 1/ca)
    ts = ts + ca * na
    ca = na
print ts
```

---

## Dry Run

`n = 4`

| i   | ca (a_i) | na (a_i+1)       | Product `ca*na` | ts after |
| --- | -------- | ---------------- | --------------- | -------- |
| 1   | 1        | 1/(1+1) = 0.5    | 0.5             | 0.5      |
| 2   | 0.5      | 1/(1+2) = 0.3333 | 0.1667          | 0.6667   |
| 3   | 0.3333   | 1/(1+3) = 0.25   | 0.0833          | 0.75     |

**Output: 0.75** (floating-point output may show a tiny rounding difference such as `0.7499999999999999`)

---

## The Math Behind It

Simplify the recurrence:

```
a(n+1) = 1 / (1 + 1/a(n)) = a(n) / (a(n) + 1)
```

Starting from `a1 = 1`, the terms are `1, 1/2, 1/3, 1/4, ...`, so **a(n) = 1/n**.

Each product becomes:

```
a(k) * a(k+1) = 1/k * 1/(k+1) = 1/(k(k+1)) = 1/k - 1/(k+1)
```

The sum **telescopes**:

```
(1 - 1/2) + (1/2 - 1/3) + ... + (1/(n-1) - 1/n) = 1 - 1/n = (n-1)/n
```

So the answer has a closed form, `(n - 1) / n`. For `n = 4` that gives `3/4 = 0.75`, which matches the dry run.

---

## Complexity

- **Time:** O(n) for the loop. The closed form is O(1).
- **Space:** O(1). Only three variables.

---

## Edge Cases

| Case                | Behaviour                                                                |
| ------------------- | ------------------------------------------------------------------------ |
| `n = 1`             | Loop doesn't run, sum is `0.0` (no pairs exist)                          |
| `n = 2`             | One product, `1 * 0.5 = 0.5`                                             |
| `n = 0` or negative | Loop doesn't run, prints `0.0`, though the problem isn't meaningful here |
| Very large `n`      | Floating-point rounding errors accumulate slowly                         |
| Non-numeric input   | `ValueError` crash from `int()`                                          |
| Division by zero    | Can't happen, since `ca` is always positive                              |

---

## Code-Quality Notes

- Add a check that `n >= 1`, and print a message otherwise.
- Wrap `int(input(...))` in `try/except ValueError`.
- Use clearer names (`current`, `next_term`, `total`) in place of `ca`, `na`, `ts`.
- Use the closed form `(n - 1) / n` to verify the loop's result in a test.

---

## Natural Extension

- Compare the loop result against `(n - 1) / n` for several values of `n`.
- Use `fractions.Fraction` to get an **exact** answer with no rounding error.
- Print the **first n terms** of the sequence.
- Try other recurrences, such as Fibonacci ratios.

---

## Repository Structure

```
python-practice/
├── sum_of_products.py
└── README.md
```

---

## How to Run

```bash
python sum_of_products.py
```

---

## Key Concepts

- Recurrence relations
- Rolling variables (constant-space iteration)
- `for` loop with `range`
- Floating-point arithmetic
- Telescoping series

---

## Why This Problem Matters

It shows two ways to solve the same problem: a **simulation** that follows the definition term by term, and a **mathematical insight** that collapses it to one formula. Spotting a closed form is a useful habit for optimisation and for checking your own code.

---

## Contributing

Suggestions and improvements are welcome. Fork the repo, make your change and open a pull request.

---

## License

This project is open source and available under the MIT License.
