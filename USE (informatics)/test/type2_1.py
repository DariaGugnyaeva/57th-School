from itertools import *

for w in range(2):
    for z in range(2):
        for y in range(2):
            for x in range(2):
                if ((w<=y)<=x or not z) == 0:
                    print()#w, z, y, x)

def f(x, y, z, w):
    return ((w<=y)<=x) or (not z)
 
for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat = 7):
    table = [(a1, a2, 1, a3), (a4, 0, a5, a6), (a7, 1, 0, 0)]
    if 3 == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(table)
                print(*p, sep='')