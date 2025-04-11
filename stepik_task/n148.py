import turtle
import random
import time

while True:
    turtle.Screen().bgcolor("DimGray")
    t = turtle.Turtle()
    t.penup()
    t.backward(300)
    t.turtlesize(3, 3)
    t.shape(random.choice("turtle circle arrow triangle square classic".split()))

    for color in ["coral", "pink", "chocolate",
    "yellow", "brown", "grey",
    "green", "DarkOrchid", "red",
    "blue", "DeepSkyBlue", "CadetBlue"]:
      t.color(color)
      t.stamp()
      t.forward(50)
    time.sleep(1) 
    turtle.clearscreen()
