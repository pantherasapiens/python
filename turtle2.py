import turtle

# Create a turtle screen
wn = turtle.Screen()
wn.bgcolor("black")

# Create a turtle
spiral = turtle.Turtle()
spiral.speed(0)  # Set the drawing speed (0 is the fastest)

# Define colors for the spiral
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw a colorful spiral
for i in range(360):
    spiral.color(colors[i % 6])  # Cycle through the colors
    spiral.forward(100)
    spiral.right(59)
    spiral.forward(100)
    spiral.right(59)
    spiral.forward(100)
    spiral.right(59)
    spiral.forward(100)
    spiral.right(59)
    spiral.forward(100)
    spiral.right(59)
    spiral.forward(100)
    spiral.right(59)

# Close the turtle graphics window when clicked
wn.exitonclick()