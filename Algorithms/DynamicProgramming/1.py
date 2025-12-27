import sys


def change(mon):
    table = [sys.maxsize for _ in range(mon+1)]
    table[0] = 0

    for m in range(1, mon+1):
        for c in [1, 3, 4]:
            if c <= m:
                table[m] = min(table[m], 1 + table[m-c])

    return table[-1]


print(change(int(input())))