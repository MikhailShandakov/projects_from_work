from turtle import Screen as S, Turtle as T

wn = S()

wn.bgcolor("green")

t = T("circle")

t.turtlesize(3)
t.hideturtle()
t.color("white")
t.penup()

t1 = T()

t1.hideturtle()
t1.pensize(20)
t1.penup()
t1.goto(-200, 200)
t1.pendown()
t1.color("white")

for m in range(4):
    t1.fd(400)
    t1.right(90)

t.goto(100, 100)

dx, dy = 1.3, 2.3

X, Y = 50, 50

t.speed("fastest")
t.showturtle()

while True:
    t.goto(X+dx, Y+dy)
    X, Y = t.xcor(), t.ycor()
    if X<-175 or X>175:
        dx = dx*-1
    if Y<-175 or Y>175:
        dy = dy*-1
