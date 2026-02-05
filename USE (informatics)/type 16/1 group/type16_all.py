# 1
def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return f(n // 2)
    return f(n-1) + 1

b = 0
for n in range(1, 901):
    g = f(n)
    if g == 9:
        b += 1
print('1: ', b)

# 2
n = 2022
print('2: ', (n+1)**2)

# 3
# F(n) = 2 при n < 3;
# F(n) = F(n − 2) + F(n − 1) − n, если n > 2 и при этом n чётно;
# F(n) =F(n − 1) − F(n − 2) + 2 × n, если n > 2 и при этом n нечётно
def f(n):
    if n < 3:
        return 2
    if n % 2 == 0:
        return f(n - 2) + f(n - 1) - n
    return -f(n - 2) + f(n - 1) + n * 2

print('3: ', f(32))

# 4
# F(1) = 1;
# F(2) = 2;
# F(3) = 3;
# F(n) = F(n − 3) · n при n > 3.
# Чему равно значение функции F(11)
def f(n):
    if n in [1, 2, 3]:
        return n
    return f(n-3) * n

print('4: ', f(11))
# 5
# F(n) = 1 при n ≤ 2;
# F(n) = F(n − 1) + 3 · F(n − 2) при n > 2.
# Чему равно значение функции F(7)? В ответе запишите только натуральное число.
def f(n):
    if n <= 2:
        return 1
    return f(n-1)+3*f(n-2)
print('5: ', f(7))

# 6
# F(n) = n при n > 2024;
# F(n) = n · F(n + 1), если n ≤ 2024.
# Чему равно значение выражения F(2022) / F(2024)
def f(n):
    if n > 2024:
        return n
    return n * f(n+1)
print('6: ', 2022*2023)
print(f(2022) / f(2024))

# 7
import sys

sys.setrecursionlimit(10**6)

def f(n):
    if n == 1:
        return 1
    return n - 2 + f(n - 1)
print('7: ', f(2023) - f(2021))

# 8
def f(n):
    if n > 10**6:
        return n
    return n + f(2*n)

def g(n):
    return f(n) / n
c = 0
for n in range(1, 10**6+1):
    if g(n) == g(1000):
        c += 1
print('8: ', c)