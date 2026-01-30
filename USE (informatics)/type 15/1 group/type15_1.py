
for A in range(1000):
    flag = 1
    for x in range(1000):
        if (((x & 114 != 0) or (x & 94 != 0)) <= ((x & 73 == 0) <= (x & A != 0))) == 0:
            flag = 0
    if flag == 1:
        print(A)
        break
