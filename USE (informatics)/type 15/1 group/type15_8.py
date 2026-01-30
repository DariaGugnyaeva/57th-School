# x & 49 = 0 → (x & 28 ≠ 0 → x & А ≠ 0)
for A in range(128):
    B = True 
    for x in range(128):
        if (x & 49 != 0 or (x & 28 == 0 or x & A != 0)) == 0:
            B=False
    if B:
        print(A)
        break