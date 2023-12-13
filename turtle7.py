import turtle
t = turtle.Turtle()
t.hideturtle()
for i in range(4):
    t.forward(100)
    t.right(90)
    # t.up()
    t.penup()
    t.forward(100)
    t.pendown()
    # t.down()
turtle.done()