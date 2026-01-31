from itertools import *

def k(x, y, z, w):
    # (z ∧ y) ∨ ((x → z ) ≡ (y → w))
    return (z and y) or ((x <= z ) == (y <= w))

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    t = [(a1, a2, a3, 1), (1, a4, a5, 1), (1, a6, 1, 1)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [k(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(*p)