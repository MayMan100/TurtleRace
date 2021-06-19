# Import requirements (view README.md for more details)
import random
from turtle import Turtle, Screen

# Initialize Variables
index = 0
race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
x_positions = [-230, -210, -90, -70]
all_turtles = []

# Setup the Turtle Screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Add Six Turtles with a unique color and line them up to the starting positions
for color in colors:
	color = Turtle(shape="turtle")
	color.penup()
	color.goto(x=-230, y=y_positions[index])
	color.color(colors[index])
	index += 1
	all_turtles.append(color)

# Check if user has placed a bet
if user_bet:
	race_on = True

while race_on:
	random_distance = random.randint(0, 10)
	random_turtle = random.choice(all_turtles)
	random_turtle.forward(random_distance)
	if random_turtle.xcor() > 230:
		race_on = False

if random_turtle.pencolor() == user_bet:
	print("Bet won!")
else:
	print("Bet Lost")


screen.exitonclick()