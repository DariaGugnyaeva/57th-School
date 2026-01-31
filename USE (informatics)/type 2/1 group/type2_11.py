from itertools import *

def k(x, y, z, w):
    # ((x ∧ y) ∨ (y ∧ z)) ≡ ((x → w) ∧ (w → z))
    return ((x and y) or (y and z)) == ((x <= w) and (w <= z))

for a1, a2 in product([0, 1], repeat=2):
    t = [(0, 1, 1, 1), (0, 1, 0, a1), (0, 1, 0, a2)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [k(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(*p)