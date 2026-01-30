from itertools import *

c = 0
for i in product('0123456789AB', repeat=5):
    if i[0] != '0' and i.count('7') == 1:
        if (i.count('9') + i.count('A') + i.count('B')) <= 3:
            c += 1
print(c)
