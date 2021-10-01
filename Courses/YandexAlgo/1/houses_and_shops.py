data = list(map(int, input().split()))

final = 0
for i in range(len(data)):
    if data[i] == 1:
        j = i
        counter1 = 0
        switch1 = False
        if j == 0:
            switch1 = True
        while j != 0:
            counter1 += 1
            j -= 1
            if data[j] == 2:
                break
            if j == 0:
                switch1 = True
        j = i
        counter2 = 0
        switch2 = False
        if j == len(data) - 1:
            switch2 = True
        while j != len(data) - 1:
            counter2 += 1
            j += 1
            if data[j] == 2:
                break
            if j == len(data) - 1:
                switch2 = True
        if switch1 is True and switch2 is False:
            counter = counter2
        elif switch2 is True and switch1 is False:
            counter = counter1
        else:
            counter = min([counter1, counter2])
        if final < counter:
            final = counter
print(final)
