import turtle

for i in range(2):
    turtle.forward(450)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
for red in range(3):
    turtle.begin_fill()
    turtle.color("red")
    turtle.forward(450)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()
for white in range(3):
    turtle.begin_fill()
    turtle.color("white")
    turtle.forward(450)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.end_fill()
for red in range(3):
    turtle.begin_fill()
    turtle.color("red")
    turtle.forward(450)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()

turtle.exitonclick()
