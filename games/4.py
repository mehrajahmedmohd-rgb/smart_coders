import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
t = turtle.Turtle()
t.speed(2)

# Set fill and border colors
t.fillcolor("white")
t.pencolor("red")
t.pensize(8)

# Draw filled triangle
t.begin_fill()

for i in range(4):
    t.forward(120)
    t.left(90)
    



t.end_fill()

# Hide turtle
t.hideturtle()

# Keep window open
turtle.done()