sets = '0123456789ABCDEFGHI'
k = 0
d = 0
for i in sets:
    s = int(f'98897{i}21', 19) + int(f'2{i}923', 19)
    if s % 18 == 0:
        k = i
        d = s
print(k, d / 18)
