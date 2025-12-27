import sys


def calc(n):
    table = [sys.maxsize for _ in range(n+1)]
    table[0] = 0
    
    for k in range(2, n+1):
        table[k] = 1 + table[k-1]
        if k % 2 == 0:
            table[k] = min(table[k], 1 + table[k // 2])
        if k % 3 == 0:
            table[k] = min(table[k], 1 + table[k // 3])
    
    operations = []
    while n > 1:
        operations.append(n)
        if table[n] == 1 + table[n-1]:
            n -= 1
        elif n % 2 == 0 and table[n] == 1 + table[n // 2]:
            n //= 2
        elif n % 3 == 0 and table[n] == 1 + table[n // 3]:
            n //= 3

    return [1] + operations[::-1]

ans = calc(int(input()))
print(len(ans) - 1)
print(*ans)