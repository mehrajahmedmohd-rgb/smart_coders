import turtle
import random

WIDTH = 800
HEIGHT=600
color = ["red", "white", "blue", "purple", "orange", "pink", "yellow"]

screen = turtle.Screen()
screen.title("turtle race")
screen.setup(WIDTH , HEIGHT)
screen.bgcolor("black")
try:

    num_of_racing_turtle = int(screen.textinput( title="number of racing turtles", prompt="enter the  numbers of racing turtles [2-7]"))

except ValueError:
    print("error")

race_turtle_list = []
spacing= WIDTH / (num_of_racing_turtle + 1)
for i in range(num_of_racing_turtle):
    race_turtle = turtle.Turtle()
    race_turtle.color(color[i])
    race_turtle.shape("turtle")
    race_turtle.penup()
    race_turtle.goto(-WIDTH/2 + spacing * (i+1) , -HEIGHT/2 +20)
    race_turtle.pendown()
    race_turtle.left(90)
    race_turtle_list.append(race_turtle)
    
index = -1
while True:
    for race_turtle in race_turtle_list:
        distance = random.randrange(start=1,stop=20)
        race_turtle.forward(distance)
        x_curr , y_curr = race_turtle.position()

        if  y_curr >= HEIGHT/2 -25:
            break

    if y_curr >= HEIGHT/2 -25:
        break    



screen.mainloop()