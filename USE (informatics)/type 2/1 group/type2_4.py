from itertools import *

def k(x, y, z, w):
    # ((x → y ) ∧ (y → w)) ∨ (z ≡ ( x ∨ y))
    return ((x <= y ) and (y <= w)) or (z == (x or y))

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    t = [(1, a1, a2, 1), (1, a3, a4, a5), (a6, 1, a7, 1)]
    if len(set(t)) == 3:
        for p in permutations('xyzw'):
            if [k(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(*p)