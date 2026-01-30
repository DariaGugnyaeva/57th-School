b = set()
for A in range(100):
    flag = 1
    for x in range(1000):
        if not((x & 17 == 0) or (x & A == 0)):
            b.add(A)
            flag = 0
    if flag == 1:
        print(A)
print(b)