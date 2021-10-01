def eq(a, b):
    if a == 0:
        if b == 0:
            return "INF"
        else:
            return "NO"
    else:
        if b == 0:
            return 0
        else:
            return -b / a


def solve():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    one = eq(a, b)
    two = eq(c, d)

    if one == "INF" or one == "NO":
        return one
    elif one != two and one.is_integer():
        return int(one)
    else:
        return "NO"


print(solve())
