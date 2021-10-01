p = int(input())


def triangle_check(a, b, c):
    return (a < b + c and b < a + c and c < a + b) or (a == b == c)


def calc_area(a, b, c):
    P = (a + b + c) / 2
    return P * (P - a) * (P - b) * (P - c)


min_ = -1
max_ = 0
maxi = []
mini = []

for i in range(int(p / 3), int(p / 3) + 2):
    ost = p - i
    n = int(ost / 2) if ost % 2 == 0 else int(ost / 2 + 1)
    k = int(ost / 2) if ost % 2 == 0 else int(ost / 2 - 1)
    if triangle_check(i, n, k):
        area = calc_area(i, n, k)
        if area > max_:
            max_ = area
            maxi = [i, n, k]


for i in range(int(p / 2), int(p / 2) - 2, -1):
    ost = p - i
    n = i
    k = p - (i + n)
    if triangle_check(i, n, k):
        area = calc_area(i, n, k)
        if min_ == -1:
            min_ = area
            mini = [i, n, k]
        elif area < min_:
            min_ = area
            mini = [i, n, k]
    ost = p - i
    n = i - 1
    k = p - (i + n)
    if triangle_check(i, n, k):
        area = calc_area(i, n, k)
        if min_ == -1:
            min_ = area
            mini = [i, n, k]
        elif area < min_:
            min_ = area
            mini = [i, n, k]


if min_ != -1 and max_ != 0:
    print(*sorted(maxi))
    print(*sorted(mini))
else:
    print(-1)
