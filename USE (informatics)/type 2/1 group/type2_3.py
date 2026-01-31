from itertools import *

def k(x, y, z, w):
    # (x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w
    return (x and (not y)) or (y == z) or (not w)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    t = [(a1, 0, a2, a3), (1, 0, a4, 0), (1, a5, 0, 0)]
    if len(set(t)) == 3:
        for p in permutations('xyzw'):
            if [k(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(*p)