import turtle

# shape 0
# wn = turtle.Screen()
# wn.bgcolor("light green")
# wn.title("Turtle")
# skk = turtle.Turtle()
# skk.forward(100)
# turtle.done()

# shape 1: square
# skk = turtle.Turtle()
# for i in range(4):
#     skk.forward(50)
#     skk.right(90)
# turtle.done()

# shape 2: star
# star = turtle.Turtle()
# star.right(75)
# star.forward(100)
# for i in range(4):
#     star.right(144)
#     star.forward(100)
# turtle.done()

# shape 3: hexagon
# polygon = turtle.Turtle()
# num_sides = 6
# side_length = 70
# angle = 360 / num_sides
# for i in range(num_sides):
#     polygon.forward(side_length)
#     polygon.right(angle)
# turtle.done()

# shape 4: parallelogram
# t = turtle.Turtle()
# t.speed(1)
# for i in range(2):
#     t.forward(100)
#     t.left(60)
#     t.forward(50)
#     t.left(120)

# shape 5: circle
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(100)
pen.fillcolor("red")
pen.begin_fill()
pen.circle(100)
pen.end_fill()
pen.hideturtle()
turtle.done()