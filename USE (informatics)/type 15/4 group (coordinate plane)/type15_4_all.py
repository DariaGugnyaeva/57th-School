def f(x, y, a):
    return ((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9))
# ((x ≤ 9) →(x ⋅ x ≤ A)) ⋀ ((y ⋅ y ≤ A) → (y ≤ 9))
amax = []
for a in range(1, 1000):
    if all(f(x, y, a) == 1 for x in range(1, 1000) for y in range(1, 1000)):
        amax.append(a)
print(max(amax))


def f1(x, y, a):
    return ((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6))
# ((x < 6) → (x2 < A)) ∧ ((y2 ≤ A) → (y ≤ 6))
c = 0
for a in range(1, 1000):
    if all(f1(x, y, a) for x in range(1000) for y in range(1000)):
        c += 1
print(c)


def f2(x, y, a):
    return ((x < a) <= (x**2 < 100)) and ((y**2 <= 64) <= (y <= a))
# ((x < A) → (x2 < 100)) ∧ ((y2 ≤ 64) → (y ≤ A))
c = 0
for a in range(1000):
    if all(f2(x,y,a) for x in range(1000) for y in range(1000)):
        c += 1
print(c)

def f3(x, y, a):
    return (y + 2*x < a) or (x > 30) or (y > 20)
for a in range(1000):
    if all(f3(x,y,a) for x in range(1000) for y in range(1000)):
        print(a)
        break

# ((x ∈ A) → (x2 ≤ 100)) ∧ ((x2 ≤ 64) → (x ∈ A))
# тождественно истинна при любом вещественном x. Какую наибольшую длину может иметь отрезок A
def f4(x, a):
    return ((x in a) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in a))

a = set(range(-1000, 1000))
for x in range(-1000, 1000):
    if not f4(x, a):
        a.remove(x)
print(len(a)-1)

def f5(x, y, a):
    return ((x in a) <= (x**2 <= 81)) and ((y**2 <= 36) <= (y in a))
# ((x ∈ A) → (x2 ≤ 81)) ∧ ((y2 ≤ 36) → (y ∈ A))
# тождественно истинна при любых вещественных x и y. Какую наибольшую длину может иметь отрезок A
a = set(range(-1000, 1000))
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if not f5(x, y, a):
            if x in a:
                a.remove(x)
            if y in a:
                a.remove(y)
print(len(a)-1)

# Для какого наибольшего целого неотрицательного числа A выражение
# (y + 2x ≠ 48) ∨ (A < x) ∨ (A < y)
# тождественно истинно, то есть принимает значение 1 при любых целых неотрицательных x и y?
def f6(x, y, a):
    return (y + 2*x != 48) or (a < x) or (a < y)
amax = 0
for a in range(1000):
    if all(f6(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
        amax = a
print(amax)

# Для какого наименьшего целого неотрицательного числа A выражение
# (2x + 3y > 30) ∨ (x + y ≤ A)
# тождественно истинно при любых целых неотрицательных x и y?
def f7(x, y, a):
    return (2*x + 3*y > 30) or (x + y <=a)
for a in range(1000):
    if all(f7(x,y,a) for x in range(1000) for y in range(1000)):
        print(a)
        break

# Для какого наименьшего целого неотрицательного числа A выражение
# (3x + 4y ≠ 70) ∨ (A > x) ∨ (A > y)
# тождественно истинно при любых целых неотрицательных x и y?
def f8(x,y,a):
    return (3*x + 4*y != 70) or (a >x) or (a>y)
for a in range(1000):
    if all(f8(x,y,a) for x in range(1000) for y in range(1000)):
        print(a)
        break

# Для какого наименьшего целого неотрицательного числа A выражение
# (2x + 3y ≠ 60) ∨ (A ≥ x) ∨ (A ≥ y)
# тождественно истинно при любых целых неотрицательных x и y?
def f9(x,y,a):
    return (2*x+3*y != 60) or (a>=x) or (a>=y)
for a in range(1000):
    if all(f9(x,y,a) for x in range(1000) for y in range(1000)):
        print(a)
        break

# Для какого наименьшего целого неотрицательного числа A выражение
# (y + 2x < A) ∨ (x > 15) ∨ (y > 30)
# тождественно истинно при всех вещественных значениях x и y?
def f10(x,y,a):
    return (y + 2*x < a) or (x > 15) or (y > 30)
for a in range(1000):
    if all(f10(x,y,a) for x in range(1000) for y in range(1000)):
        print(a)
        break

# Для какого наименьшего целого неотрицательного числа A выражение
# (2m + 3n > 40) ∨ ((m < A) ∧ (n ≤ A))
# тождественно истинно при любых целых неотрицательных m и n?
def f11(m,n,a):
    return (2*m + 3*n > 40) or ((m < a) and (n <= a))
for a in range(1000):
    if all(f11(m,n,a) for m in range(1000) for n in range(1000)):
        print(a)
        break