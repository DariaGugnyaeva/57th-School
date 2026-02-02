from turtle import *
# 38
# Повтори 12 [Направо 60 Вперёд 1 Направо 60 Вперёд 1 Направо 270
k = 30
screensize(2000, 2000)
down()
tracer(0)
for _ in range(12):
    right(60)
    forward(1*k)
    right(60)
    forward(1*k)
    right(270)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(4, 'red')
done()