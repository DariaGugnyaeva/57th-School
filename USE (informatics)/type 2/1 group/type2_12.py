from itertools import *

def k(x, y, z, w):
    return (x and (not y)) or (y == z) or (not w)

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    t = [(0, a1, a2, 0), (0, 1, 0, 1), (a3, 1, 0, a4)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [k(**dict(zip(p, r))) for r in t] == [0,0,0]:
                print(*p)