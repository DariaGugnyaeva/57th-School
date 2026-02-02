from turtle import *
# 80.
tracer(0)
screensize(2500, 2500)
k = 60
down()
# Повтори 4 [Вперёд 10 Направо 60 Вперёд 10 Направо 120]
for _ in range(4):
    forward(10*k)
    right(60)
    forward(10*k)
    right(120)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(4, 'red')
done()