import turtle

for i in range(2):
    turtle.begin_fill()
    turtle.color("green")
    turtle.forward(350)
    turtle.right(90)
    turtle.forward(260)
    turtle.right(90)
    turtle.end_fill()
turtle.right(90)
turtle.penup()
turtle.forward(210)
turtle.left(90)
turtle.forward(170)
turtle.pendown()
turtle.begin_fill()
turtle.circle(90)
turtle.color("red")
turtle.right(90)
turtle.end_fill()

turtle.exitonclick()
