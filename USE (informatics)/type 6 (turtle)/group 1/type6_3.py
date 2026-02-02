from turtle import *
# 66
tracer(0)
k = 30
screensize(2000, 2000)
down()
for _ in range(4):
    forward(k*5)
    right(90)
    forward(10*k)
    right(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(4, 'red')
done()