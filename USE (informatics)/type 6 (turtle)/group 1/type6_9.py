from turtle import *

k = 30
screensize(2000, 2000)
tracer(0)
down()



# the first figure
begin_fill()
for _ in range(4):
    fd(12*k)
    right(90)
right(30)
end_fill()
up()


count = 0  # it counts the number of dots inside the figure
c = 0  # it counts the number of dots on the border and inside the figure
g = getcanvas()
for x in range(-20, 20):
    for y in range(-20, 20):
        info = g.find_overlapping(x*k, y*k, x*k, y*k)
        if len(info) == 1 and info[0] == 5:
            count += 1
        if len(info) >= 1:
            c += 1
print(count, c)


# the second figure
down()
begin_fill()
for _ in range(3):
    fd(8*k)
    right(60)
    forward(8*k)
    right(120)
end_fill()
up()


count2 = 0  # it counts all the dots in the second 'odd' figure
g = getcanvas()
for x in range(-20, 20):
    for y in range(-20, 20):
        info = g.find_overlapping(x*k, y*k, x*k, y*k)
        if len(info) >= 1:
            count2 += 1
print(count2)
# Определите, сколько точек с целочисленными координатами будут находиться внутри обла-
# сти, ограниченной линией, заданной данным алгоритмом: Повтори 4 [Вперёд 12 Направо 90].
# и находиться вне области, ограниченной линией, заданной данным алгоритмом: Повтори 3
# [Вперёд 8 Направо 60 Вперёд 8 Направо 120]. Точки на линии учитывать не следует.
print(count - (c+count2) / 2)