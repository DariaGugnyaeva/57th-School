from turtle import *

k = 30
screensize(2000, 2000)
tracer(0)
left(90)
down()
begin_fill()
for _ in range(6):  # Повтори 6 [Направо 36 Вперёд 10 Направо 36]
    right(36)
    forward(10*k)
    right(36)
end_fill()
up()

g = getcanvas()
count = 0
for x in range(-20, 20):
    for y in range(-20, 20):
        info = g.find_overlapping(x*k, y*k, x*k, y*k)
        if len(info) == 1 and info[0] == 5:
            count += 1
done()
print(count)
