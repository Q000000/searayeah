l = int(input())
data = list(map(int, input().split()))

sorted_data = sorted(data)
print(sum(sorted_data[:-1]))
