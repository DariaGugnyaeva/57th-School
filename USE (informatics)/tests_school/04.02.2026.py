from itertools import *
 # F = ((x ∨ y) → z) ∨ (y ≡ w) ∨ z,

def f(x, y, z, w):
    return ((x or y) <= z) or (y == w) or z

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    t = [(0, 1, a1, a2), (1, a3, 1, 0), (a4, 1, 1, 0)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(*p)
# wyxz

print(124*1024 // 2000 - 28)
print(2**(8*35 // 34))  # 256

# 13
# (3y – x > 12) ∨ (2x + 6y ≥ 72) ∨ (x > 24) ∨ (x ⋅ y < A) 
print(12*8+1)

print(1380 / 12)  # 115 единиц
# 15
# Сеть задана IP-адресом 192.168.0.0 и маской сети 255.255.192.0. Сколько в этой сети IP
# адресов, в двоичной записи которых единиц больше, чем нулей?
from ipaddress import *

net = ip_network('192.168.0.0/255.255.192.0')
global_c = 0
for i in net:
    l = 0
    k = str(i).split('.')
    for c in k:
        c = bin(int(c))[2:]
        l += c.count('1')
    if l > 16:
        global_c += 1
print(global_c)
print(bin(192))
# 16 ex.
# F(n) = G(n − 1) − G(n − 5) 
# G(n) = 2 × (n + 1), если n ≤ 25 
# G(n) = G( n − 4) + n, если n > 25 
import sys

sys.setrecursionlimit(10**6)
def g(n):
    if n <= 25:
        return 2*(n+1)
    return g(n-4)+n
def f(n):
    return g(n-1) - g(n-5)

print(f(150774))  # 150773 ans.