import turtle

t = turtle.Turtle()
t.hideturtle()
t.color("green")
for i in range(5):
    t.fd(100)
    t.rt(90)
    t.penup()
    t.fd(10)
    t.pendown()

t.clear()
t.pencolor("blue")
for x in range(5):
    t.bk(100)
    t.lt(90)
    t.up()
    t.back(100)
    t.down()

turtle.done()