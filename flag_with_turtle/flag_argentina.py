import turtle

for i in range(2):
    turtle.forward(450)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
for blue in range(3):
    turtle.begin_fill()
    turtle.color("light blue")
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
for blue in range(3):
    turtle.begin_fill()
    turtle.color("light blue")
    turtle.forward(450)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()

turtle.penup()
turtle.forward(225)
turtle.right(90)
turtle.forward(130)
turtle.pendown()

turtle.color("orange")
counter = 0
while counter <= 16:
    counter = counter + 1
    turtle.right(10)
    for i in range(2):
        turtle.forward(50)
        turtle.right(187)
turtle.exitonclick()
