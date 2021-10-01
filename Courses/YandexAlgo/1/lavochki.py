l, k = map(int, input().split())
data = list(map(int, input().split()))


def solve(l, data):
    answer1 = -1
    answer2 = -1
    if l % 2 != 0:
        if int(l / 2) in data:
            print(int(l / 2))
        else:
            center1 = int(l / 2)
            center2 = int(l / 2) + 1
            for point in data:
                if point <= center1:
                    answer1 = point
                if answer2 == -1 and point >= center2:
                    answer2 = point
            print(answer1, answer2)

    else:
        center = int(l / 2)
        for point in data:
            if point < center:
                answer1 = point
            if answer2 == -1 and point >= center:
                answer2 = point
        print(answer1, answer2)


solve(l, data)
