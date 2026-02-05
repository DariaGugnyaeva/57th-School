from itertools import *

def k(x, y, z, w):
    return  ((y <= w) == (x <= (not z))) and (x or w)

for a1, a2 in product([0, 1], repeat=2):
    t = [(0, 1, 1, 1), (1, 0, 1, 0), (a1, 0, 0, a2)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [k(**dict(zip(p, r))) for r in t] == [0, 1, 1]:
                print(*p)