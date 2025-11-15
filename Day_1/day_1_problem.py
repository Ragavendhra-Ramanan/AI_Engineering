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
