path = r"C:\Users\USER\Downloads\inf_24_01\inf_24_01\Доп.файлы_24_01\Задание 17\inf_24_01_17.txt"
with open(path, encoding='utf-8') as f:
    data = f.read().split()
data = [int(i) for i in data if i]
pair = 0
summ = 0
for k, v in enumerate(data):
    if k == len(data)-1:
        break
    if v % 16 == 0 or data[k + 1] % 16 == 0:
        pair += 1
        if v + data[k + 1] > summ:
            summ = v + data[k + 1]

# print(n, m) всего эл-тов 10000, кратно16 676 из них
print(pair, summ)
