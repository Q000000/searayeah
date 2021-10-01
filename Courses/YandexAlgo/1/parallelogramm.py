def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def coef(x1, y1, x2, y2):
    return (y1 - y2) / (x1 - x2) if x1 != x2 else 0


def solve():
    n = int(input())
    answer = []
    for i in range(n):
        temp = list(map(int, input().split()))
        data = list(zip(temp[::2], temp[1::2]))

        sum_ = []
        if len(set(data)) == 4:
            for i in range(len(data)):
                for j in range(i + 1, len(data)):
                    sum_.append(
                        dist(data[i][0], data[i][1], data[j][0], data[j][1])
                        + coef(data[i][0], data[i][1], data[j][0], data[j][1])
                    )

            if len(set(sum_)) == 4:
                answer.append("YES")
            else:
                answer.append("NO")
        else:
            answer.append("NO")
    return answer


print(*solve(), sep="\n")
