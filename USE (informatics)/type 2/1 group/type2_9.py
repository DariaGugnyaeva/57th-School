from itertools import *

def k(x, y, z, w):
    # ((y → x) ≡ (x → w)) ∧ (z ∨ x)
    return ((y <= x) == (x <= w)) and (z or x)

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    t = [(0, a1, a2, 0), (0, 0, 0, a3), (a4, a5, 0, a6)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [k(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(*p)