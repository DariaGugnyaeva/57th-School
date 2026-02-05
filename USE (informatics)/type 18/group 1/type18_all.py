path = r"C:\Users\USER\Desktop\programming\57th-School\USE (informatics)\type 18\group 1\zadanie18_6.csv"

with open(path, encoding='utf-8') as f:
    data = f.read().split()
for row in data:
    r = map(int, row.split(';'))
    print(r)