from turtle import *
# 24
# Повтори 4 [Вперёд 8 Направо 150 Вперёд 8 Направо 30]
down()
tracer(0)
screensize(2000, 2000)
k = 30
for _ in range(4):
    forward(8*k)
    right(150)
    forward(8*k)
    right(30)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(4, 'red')
done()