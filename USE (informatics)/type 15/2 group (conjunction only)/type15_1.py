# x & 29 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)

for A in range(100):
    flag = 1
    for x in range(1000):
        if (x & 29 == 0 or (x & 17 != 0 or x & A != 0)) == 0:
            flag = 0
    if flag == 1:
        print(A)
        break