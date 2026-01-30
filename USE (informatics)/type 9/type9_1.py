# —  в строке есть одно число, которое
# повторяется трижды, остальные четыре числа различны;

# —  среднее арифметическое неповторяющихся чисел
# строки не больше повторяющегося числа.

# Определите сумму чисел в строке с наибольшим номером,
# для которой выполнены оба условия:
from collections import Counter

with open(r"C:\Users\USER\Desktop\programming\57th-School\RSE (informatics)\DEMO_9.csv", encoding='utf-8') as f:
    data = f.read().split()
c = 0
for i in data:
    row = list(map(int, i.split(';')))
    if len(set(row)) == 5:
        d = list(Counter(row).items())
        if d[0][1] == 3 and (d[1][0] + d[2][0] + d[3][0] + d[4][0]) // 4 <= d[0][0]:
            c = sum(row)

print(c)
    
