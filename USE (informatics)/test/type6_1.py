from turtle import *

k = 20
screensize(2000, 2000)
tracer(0)
down()

for i in range(9):
    forward(22*k)
    right(90)
    forward(6*k)
    right(90)
up()
forward(1*k)
right(90)
forward(5*k)
left(90)
down()
for i in range(9):
    forward(53*k)
    right(90)
    forward(75*k)
    right(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(5, 'red')
done()
