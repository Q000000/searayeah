n, i, j = map(int, input().split())


def solve(n, i, j):
    if i > j:
        a = i
        i = j
        j = a

    max_ = n / 2 - 1 if n % 2 == 0 else (n - 1) / 2 - 1

    if j - i - 1 > max_:
        return i - 1 + n - j
    elif j - i - 1 < max_:
        return j - i - 1
    else:
        return int(max_)


print(solve(n, i, j))
