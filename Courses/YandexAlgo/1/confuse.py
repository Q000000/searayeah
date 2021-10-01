n, k = map(int, input().split())
data = list(map(int, input().split()))

answer = max(data) - min(data)

print(answer)
