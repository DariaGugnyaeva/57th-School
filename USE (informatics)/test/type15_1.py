p = list(range(15, 41))
q = list(range(21, 64))
x = []
# (x  P) → (((x  Q) /\ ¬(x  A)) → ¬(x  P))
for i in range(100):
    if ((i in p) <= (((i in q) and (i not in x)) <= (i not in p))) == 0:
        x.append(i)
# если равно 1 поставить, весь диапазон входит....
print(x[-1] - x[0])
