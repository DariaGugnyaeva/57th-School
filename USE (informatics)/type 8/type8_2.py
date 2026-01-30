# Сколько существует чисел, восьмеричная
# запись которых содержит 5 цифр, причем в
# записи нет цифры 1. Также все цифры
# записи различны и никакие две чётные и
# две нечётные цифры не стоят рядом.
from itertools import *

d = 0
even, not_even = '0246', '357'
for i in product(even + not_even, repeat=5):
    if len(set(i)) == 5 and i[0] != '0':
        k = (i[0] in even and i[2] in even and i[4] in even)
        c = (i[1] in not_even and i[3] in not_even)
        k1 = (i[0] in not_even and i[2] in not_even and i[4] in not_even)
        c1 = (i[1] in even and i[3] in even)
        if (k and c) or (k1 and c1):
            d += 1

print(d)
