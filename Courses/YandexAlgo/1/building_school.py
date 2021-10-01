n = int(input())
a = list(map(int, input().split()))


def solve(n, a):
    return a[int((n - 1) / 2)]


print(solve(n, a))
