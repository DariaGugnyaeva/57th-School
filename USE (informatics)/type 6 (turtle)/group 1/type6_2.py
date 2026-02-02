from turtle import *

# 81
tracer(0)
screensize(2000, 2000)
k = 30
down()

for _ in range(4):  # Повтори 4 [Вперёд 10 Направо 90]
    forward(10*k)
    right(90)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(4, 'red')
done()