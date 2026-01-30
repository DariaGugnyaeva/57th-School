import pandas as pd

f = pd.read_csv(r"C:\Users\USER\Desktop\programming\1_9.csv", delimiter=';', names=list('abcde'))
def k(x):
    if len(set(x)) == len(x):
        x1 = sorted(x)
        maxes = x1[-1] + x1[-2]
        less = x1[0] + x1[1] + x[2]
        return int(maxes <= less)
    return 0
f['k'] = f.apply(lambda x: k(x), axis=1)
print(f['k'].value_counts())
