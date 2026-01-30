from turtle import *


k = 40
tracer(0)
screensize(2000, 2000)
down()
# Повтори 2 [Вперёд 14 Налево 270 Назад 12 Направо 90]
# Поднять хвост
# Вперёд 9 Направо 90 Назад 7 Налево 90
# Опустить хвост
# Повтори 2 [Вперёд 13 Направо 90 Вперёд 6 Направо 90].
for _ in range(2):
    forward(14*k)
    left(270)
    backward(12*k)
    right(90)
up()
forward(9*k)
right(90)
backward(7*k)
left(90)
down()
for _ in range(2):
    forward(13*k)
    right(90)
    forward(6*k)
    right(90)

up()
for x in range(-40, 40):
    for y in range(-40, 40):
        setpos(x * k, y * k)
        dot(5, 'red')
done()

