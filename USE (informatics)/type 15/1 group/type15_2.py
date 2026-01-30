# ДЕЛ(x, А) → (ДЕЛ(x, 21) + ДЕЛ(x, 35))
def k(x, A):
    return (x % A == 0) <= ((x % 21 == 0) + (x % 35 == 0))

for A in range(1, 1000):
    c = 0
    for x in range(1, 1000):
        if k(x, A) == 1:
            c += 1
    if c == 999:  # т.е. если при всех значениях истинно
        print(A)
        break
