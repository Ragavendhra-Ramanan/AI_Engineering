"""

    ## Problem Statement

A **digital root** is obtained by repeatedly summing the digits of a number until a single digit remains.

For example:

- Digital root of 38: 3 + 8 = 11 → 1 + 1 = 2
- Digital root of 157: 1 + 5 + 7 = 13 → 1 + 3 = 4

We define a **Digital Root Chain** as the sequence of numbers you get before reaching the final single digit.

For the number 38: [38, 11, 2]
For the number 157: [157, 13, 4]

**Your Task:**

Write a program that finds all numbers between 1 and 1000 where:

1. The digital root is 7
2. The chain length is exactly 3 (meaning it takes exactly 2 steps to reach the single digit)

Then, calculate the **sum of all such numbers**.

**Example:**

- 79: 7 + 9 = 16 → 1 + 6 = 7 (Chain: [79, 16, 7], Length = 3) ✓
- 88: 8 + 8 = 16 → 1 + 6 = 7 (Chain: [88, 16, 7], Length = 3) ✓
- 7: Already single digit (Chain: [7], Length = 1) ✗
"""


def digital_root(n):
    count = 1
    while n >= 10 and count <= 3:
        n = sum(int(i) for i in str(n))
        count += 1
    if (n == 7) and (count == 3):
        return 1
    return 0


def solve():
    total = 0
    candidates = []
    for i in range(1, 1001):
        if digital_root(i):
            total += i
            candidates.append(i)
    return total, candidates


if __name__ == "__main__":
    total, candidates = solve()
    print("Total:", total)
    print("Candidates:", candidates)
