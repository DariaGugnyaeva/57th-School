from itertools import *

def f(x, y, z, w):
    return (x and y and (not z)) or ((not w) and y and z)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(0, a1, 1, 0), (a2, 1, 1, a3),
         (1, 1, a4, 1), (0, 1, a5, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1, 1]:
                print(*p, sep='')
