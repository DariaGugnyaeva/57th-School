k = 0
for N in range(13):
    b = bin(N)[2:]
    if N % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    r = int(b, 2)
    if r > k:
        k = r
print(k)
