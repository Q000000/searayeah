r = int(input())
i = int(input())
c = int(input())


def solve(r, i, c):

    if i == 0:
        if r != 0:
            return 3
        else:
            return c

    elif i == 1:
        return c

    elif i == 4:
        if r != 0:
            return 3
        else:
            return 4

    elif i == 6:
        return 0

    elif i == 7:
        return 1

    return i


print(solve(r, i, c))
