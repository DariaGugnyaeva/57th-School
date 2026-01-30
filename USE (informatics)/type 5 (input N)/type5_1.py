for N in range(0, 30):
    b = bin(N)[2:]
    if N % 3 == 0:
        b += b[-3:]
    else:
        b += bin(3*(N % 3))[2:]
    r = int(b, 2)
    if r >= 200:
        print(N)
