from turtle import *

left(90)
k = 30
screensize(600,600)
tracer(0)
down()
# Повтори 5 [Вперёд 9 Направо 90 Вперёд 3 Направо 90].
for _ in range(5):
    forward(9*k)
    right(90)
    forward(3*k)
    right(90)
penup()

for x in range(-20,20):
    for y in range(-20,20):
        setpos(x*k,y*k)
        dot(4,'red')
done()

