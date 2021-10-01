def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def solve():
    d = int(input())
    x, y = map(int, input().split())
    if (y <= -x + d) and (x >= 0) and (y >= 0):
        return 0
    else:
        a = dist(0, 0, x, y)
        b = dist(d, 0, x, y)
        c = dist(0, d, x, y)
        if a <= b:
            if a <= c:
                return 1
            else:
                return 3
        else:
            if b <= c:
                return 2
            else:
                return 3


print(solve())
