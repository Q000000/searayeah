n = int(input())
data = list(map(int, input().split()))

first = sum(data)
max_ = max(data)
data.remove(max_)
second = max_ - sum(data)


if first < second:
    if first > 0:
        print(first)
    else:
        print(second)
else:
    if second > 0:
        print(second)
    else:
        print(first)
