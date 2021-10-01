x = input()
z = input()


splitter = [x[i:] for i in range(len(x))]
found_splitter = False
next_z = ""
for i in range(1, len(x) + 1):
    if z[:i] in splitter:
        found_splitter = True
        next_z = z[i:]
        if next_z[: len(x)] == x:
            break

    if i == len(z):
        break


if next_z == "":
    if found_splitter is False:
        print(z)
else:
    if found_splitter is True:
        while True:
            if next_z[0 : len(x)] == x:
                next_z = next_z.replace(x, "", 1)
            else:
                print(next_z)
                break
