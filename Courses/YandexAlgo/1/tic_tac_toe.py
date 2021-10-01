def solve():
    temp = [list(map(int, input().split())) for i in range(3)]
    flat = [x for y in temp for x in y]
    temp.append([temp[0][0], temp[1][1], temp[2][2]])
    temp.append([temp[0][2], temp[1][1], temp[2][0]])
    temp.append([temp[0][0], temp[1][0], temp[2][0]])
    temp.append([temp[0][1], temp[1][1], temp[2][1]])
    temp.append([temp[0][2], temp[1][2], temp[2][2]])

    krestiks = flat.count(1)
    nolics = flat.count(2)
    zeros = flat.count(0)

    if (krestiks - nolics != 0) and (krestiks - nolics != 1):
        return "NO"
    if ([2, 2, 2] in temp) and (krestiks - nolics != 0):
        return "NO"
    if ([1, 1, 1] in temp) and (krestiks - nolics != 1):
        return "NO"
    return "YES"


print(solve())
