import turtle
from random import randint
import time

turtles = []
points = []
number_of_players = 8 # 8 maximum players
if number_of_players > 8:
	number_of_players = 8
elif number_of_players < 1:
	number_of_players = 1

def setup():
	colors = ["orange", "red", "yellow", "blue", "green", "cyan", "purple", "pink"]
	turtles.clear()

	for i in range(number_of_players):
		turtles.append(turtle.Turtle())
		color = colors[randint(0,len(colors) - 1)]
		colors.remove(color)
		turtles[i].color(color)
		turtles[i].penup()
		turtles[i].goto(-262.5+75*i,-250)
		turtles[i].pendown()
		turtles[i].setheading(90)

	turtles[0].getscreen().bgcolor("grey")
	race()

def race():
	j = 0
	while j != 1:
		for i in range(number_of_players):
			if j == 1:
				break
			turtles[i].forward(randint(0,50))
			time.sleep(0.1)
			if turtles[i].ycor() >= 250:
				points[i] += 1
				print("Score: " + str(points))
				j = 1
		
	turtle.clearscreen()
	setup()

for i in range(number_of_players):
	points.append(0)
setup()
turtle.done()
