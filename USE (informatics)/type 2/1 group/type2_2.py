from itertools import *

def k(x, y, z):
    return (x == z) or (x <= (y and z))

for a1, a2, a3 in product([0, 1], repeat=3):
    t = [(0, 0, a1), (1, a2, a3)]
    if len(t) == len(set(t)):
        for p in permutations('xyz'):
            if [k(**dict(zip(p, r))) for r in t] == [0, 0]:
                print(*p)