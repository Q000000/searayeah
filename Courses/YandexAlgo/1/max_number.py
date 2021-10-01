n = int(input())
max_ = n
count = 1
while n != 0:
    n = int(input())
    if n == max_:
        count += 1
    elif n > max_:
        count = 1
        max_ = n
print(count)
