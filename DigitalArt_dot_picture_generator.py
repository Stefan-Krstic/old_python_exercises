import turtle as turtle_module
from turtle import Screen
import random

screen = Screen()
turtle_module.colormode(255)
koki = turtle_module.Turtle()
koki.speed(15)
koki.hideturtle()
screen.bgcolor("lightgray")
koki.penup()

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

def pomeraj(broj):
  for x in range(broj):
    koki.goto(-300, x * 70)
    for _ in range(broj):
      koki.pendown()
      koki.begin_fill()
      random_color = random.choice(color_list)
      koki.color(random_color)
      koki.circle(20)
      koki.end_fill()
      koki.penup()
      koki.forward(70)

pomeraj(10)
screen.exitonclick()
