n = int(input())
mnoj = ""
data = set(range(1, n + 1))
my_set = set()
true_set = set()
while mnoj != "HELP":
    mnoj = input()
    if mnoj != "HELP":
        input_ = set(map(int, mnoj.split()))
        half = n // 2
        len_input = len(input_)
        if len_input <= half:
            print("NO")
            n = n - len_input
            my_set.update(input_)
        else:
            print("YES")
            n = len_input
            true_set.update(input_)
if len(true_set) != 0:
    print(*sorted((true_set - my_set)))
else:
    print(*sorted(data - my_set))
