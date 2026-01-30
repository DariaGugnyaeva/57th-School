from collections import Counter
path = r"C:\Users\USER\Desktop\programming\57th-School\RSE (informatics)\inf_24_01_9.csv"
with open(path, encoding='utf-8') as f:
    data = f.read().split()
c = 0
for row in data:
    row = list(map(int, row.split(';')))
    if len(set(row)) == 4:
        k = sorted(Counter(row).items(), key=lambda x: x[1], reverse=True)
        if k[0][1] == 3:
            if (3*k[0][0])**2 > (k[1][0]+k[2][0]+k[3][0])**2:
                c += 1
            
print(c)
