x, y, z = map(int, input().split())


def solve(x, y, z):
    if (1 <= x <= 12) and (1 <= y <= 12) and (x != y):
        return 0
    return 1


print(solve(x, y, z))
