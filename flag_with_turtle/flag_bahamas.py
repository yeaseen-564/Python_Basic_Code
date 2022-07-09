import turtle

for i in range(2):
    turtle.forward(450)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
for indigo in range(3):
    turtle.begin_fill()
    turtle.color("indigo")
    turtle.forward(450)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()
for yellow in range(3):
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.forward(450)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.end_fill()
for indigo in range(3):
    turtle.begin_fill()
    turtle.color("indigo")
    turtle.forward(450)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()

turtle.forward(450)
turtle.begin_fill()
turtle.color("black")
turtle.right(140)
turtle.forward(250)
turtle.left(104)
turtle.forward(240)
turtle.end_fill()

turtle.exitonclick()
