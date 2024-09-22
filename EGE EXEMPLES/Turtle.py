from turtle import *
tracer(0)
left(90)
screensize(10000,10000)
m = 25
for _ in range(4):
    forward(16 * m)
    right(90)
    forward(18 * m)
    right(90)
up()

right(90)
forward(10 * m)
lt(90)
forward(10 * m)
down()
for _ in range(4):
    fd(15 * m)
    rt(90)
up()
fd(1*m)
lt(90)
fd(1*m)
rt(90)
down()
for _ in range(7):
    fd(12*m)
    rt(90)
update()
up()
for x in range(-50, 50):
    for y in range(-50,50):
        goto(x * m, y * m)
        dot('blue')
exitonclick()
