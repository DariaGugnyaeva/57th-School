from turtle import *
# 38
left(90)
tracer(0)
down()
screensize(2000, 2000)
k = 30
# Повтори 7 [Вперёд 10 Направо 120].
for _ in range(7):
    forward(10*k)
    right(120)
up()
for x in range(-20,20):
    for y in range(-20,20):
        setpos(x*k,y*k)
        dot(4,'red')
done()