import turtle
import time

wn=turtle.Screen()
t=turtle.Turtle()
wn.bgcolor("light blue")
t.color("red")
# t.forward(100)
# t.right(50)
# t.forward(200)
# t.left(50)
# t.forward(500)
t.fillcolor("black")
t.begin_fill()
t.circle(100)
t.end_fill()
t.hideturtle()
time.sleep(500)
turtle.bye()