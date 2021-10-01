x1, y1, x2, y2 = map(int, input().split())
x3, y3, r = map(int, input().split())

counter = 0
for i in range(y3 - r, y3 + r + 1):
    resh1 = (r ** 2 - (y3 - i) ** 2) ** 0.5 + x3
    resh2 = -((r ** 2 - (y3 - i) ** 2) ** 0.5) + x3

    if y1 <= i <= y2 and not (x2 > x1 > resh1 or resh2 > x2 > x1):
        max_ = resh1 if x2 > resh1 else x2
        min_ = resh2 if x1 < resh2 else x1
        if min_ == max_:
            counter += 1
        else:
            if type(max_) is float and int(max_) != max_ and max_ < 0:
                max_ = int(max_) - 1
            if type(min_) is float and int(min_) != min_ and min_ > 0:
                min_ = int(min_) + 1
            counter += int(max_) - int(min_) + 1

print(counter)
