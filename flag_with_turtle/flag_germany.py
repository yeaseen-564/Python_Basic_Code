import turtle


def draw_flag_box(length, width):  # Function for flag box
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)


draw_flag_box(450, 300)  # Calling function for flag box

for black in range(3):
    turtle.begin_fill()
    turtle.color("black")
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
for red in range(3):
    turtle.begin_fill()
    turtle.color("red")
    turtle.forward(450)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()

turtle.exitonclick()
