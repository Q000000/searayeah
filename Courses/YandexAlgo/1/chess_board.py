n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
per = 0
for point in data:
    neighbour_counter = 0
    neighbours = [
        [point[0], point[1] + 1],
        [point[0], point[1] + 1],
        [point[0] + 1, point[1]],
        [point[0] + 1, point[1]],
    ]
    for neighbour in neighbours:
        if neighbour in data:
            neighbour_counter += 1
    per += 4 - neighbour_counter

print(per)
