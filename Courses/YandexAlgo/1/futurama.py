def replace(x1, x2):
    # a, b = current_situation.index(x1), current_situation.index(x2)
    current_situation[x2], current_situation[x1] = (
        current_situation[x1],
        current_situation[x2],
    )
    print(x1, x2)


n, k = map(int, input().split())

current_situation = [i for i in range(0, n + 1)]
for i in range(k):
    a, b = map(int, input().split())
    current_situation[a], current_situation[b] = (
        current_situation[b],
        current_situation[a],
    )
# print("BEGIN", current_situation)
for i in range(1, n - 1):
    if current_situation[i] != i:
        replace(i, n - 1)
        while current_situation[current_situation[n - 1]] != i:
            replace(current_situation[n - 1], n - 1)
        replace(current_situation[n - 1], n)
        replace(current_situation[n], n)
        replace(current_situation[n - 1], n - 1)
if current_situation[n - 1] != n - 1:
    replace(n - 1, n)
# print("answer", current_situation)
