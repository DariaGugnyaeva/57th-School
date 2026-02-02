from turtle import *
# : Повтори 6 [Вперёд 10 Направо 60]
k = 40
screensize(2000, 2000)
down()
tracer(0)
begin_fill()
for _ in range(6):
    forward(10*k)
    right(60)
end_fill()
up()
g = getcanvas()
count = 0
for x in range(-20, 20):
    for y in range(-20, 20):
        info = g.find_overlapping(x*k, y*k, x*k, y*k)
        # if len(info) == 1 and info[0] == 5: # -- inside
        # if len(info) > 1:  # if (0, 0) belongs on the shapes edge
        if len(info) >= 1:  # it belongs to the figure and its border too
            count += 1
done()
print(count)