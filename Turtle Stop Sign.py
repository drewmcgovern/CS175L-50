#Andrew McGovern
#CS 175L 50
#Turtle Stop Sign

import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Calculate the center of the octagon with the diameter and radius
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)
radius = diameter / 2

# Initialize the turtle.
turtle.speed(ANIMATION_SPEED)

# Move the turtle to the starting point.
turtle.penup()
StartX = -(radius-x) #Starts in top left corner
StartY = WINDOW_HEIGHT/4
turtle.goto(StartX, StartY)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()  #fills the upcoming closed figures with red

# Draw the octagon.
for x in range(8):
    turtle.forward(100)
    turtle.right(45)
turtle.end_fill()    #ends filling closed figures

# Display 'STOP'
turtle.penup()
turtle.color("white")
turtle.goto(0, -(diameter/4))
turtle.write("STOP", align="center", font=("Courier New", 50, "bold"))
turtle.hideturtle()
