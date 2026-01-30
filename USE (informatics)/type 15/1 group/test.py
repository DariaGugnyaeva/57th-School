for a in range(1, 100): 
    k = 0
    for x in range(1, 1000):
        if (x % a == 0) <= ((x % 21 == 0) + (x % 35 == 0)):
            k += 1
    if k == 999:
        print(a)
        break