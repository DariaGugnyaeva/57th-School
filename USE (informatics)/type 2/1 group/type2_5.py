from itertools import *

def k(x, y, z, w):
    # (x ≡ ( w ∨ y)) ∨ ((w → z ) ∧ (y → w))
    return (x == ( w or y)) or ((w <= z ) and (y <= w))

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    t = [(1, a1, a2, 1), (a3, a4, a5, 1), (1, a6, 1, a7)]
    if len(set(t)) == len(t):
        for p in permutations('xyzw'):
            if [k(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(*p)