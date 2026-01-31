from itertools import *

def k(x, y, z, w):
    #  ((x <= y) == (y <= z)) and (y or w)
    return ((x <= y) == (y <= z)) and (y or w)

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    t = [(0, a1, 0, a2), (0, 0, a3, 0), (a4, a5, a6, 0)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [k(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(*p)