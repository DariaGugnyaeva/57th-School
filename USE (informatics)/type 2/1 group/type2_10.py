from itertools import *
# (¬x ≡ z) → (y ≡ (w ∨ x))
def k(x, y, z, w):
    return ((not x) == z) <= (y == (w or x))

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    t = [(0, 0, a1, a2), (0, a3, a4, 0), (0, a5, 0, 0)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [k(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(*p)