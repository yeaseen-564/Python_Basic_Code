import turtle


# Indian Flag pre code and not modified:
#
# turtle.speed(0)
# # Box painting
# for i in range(4):
#     turtle.forward(300)
#     turtle.right(90)
#
# # Orange color
# turtle.begin_fill()
# turtle.color("orange")
# turtle.right(90)
# turtle.penup()
# turtle.forward(100)
# turtle.pendown()
# turtle.left(90)
# turtle.forward(300)
# turtle.left(90)
# turtle.penup()
# turtle.forward(100)
# turtle.pendown()
# turtle.left(90)
# turtle.forward(300)
# turtle.left(90)
# turtle.end_fill()
# turtle.penup()
# turtle.forward(200)
#
# # White color
# turtle.begin_fill()
# turtle.color("white")
# turtle.pendown()
# turtle.left(90)
# turtle.forward(300)
# turtle.left(90)
# turtle.penup()
# turtle.forward(100)
# turtle.pendown()
# turtle.left(90)
# turtle.forward(300)
# turtle.end_fill()
# turtle.left(90)
# turtle.penup()
# turtle.forward(200)
# turtle.left(90)
# turtle.pendown()
#
# # Green color
# turtle.begin_fill()
# turtle.color("green")
# turtle.forward(300)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(300)
# turtle.left(180)
# turtle.end_fill()
# turtle.forward(140)
# turtle.left(90)
# turtle.penup()
# turtle.forward(45)
# turtle.pendown()
#
# # Circle at the center
# turtle.color("blue")
# command = 0
# while command < 25:
#     command += 1
#     for i in range(4):
#         turtle.forward(20)
#         turtle.right(90)
#     turtle.forward(5)
#     turtle.right(15)
# turtle.exitonclick()


# Indian Flag code more modified and short code

for i in range(2):
    turtle.forward(450)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
for orange in range(3):
    turtle.begin_fill()
    turtle.color("orange")
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
for green in range(3):
    turtle.begin_fill()
    turtle.color("green")
    turtle.forward(450)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()

turtle.penup()
turtle.forward(220)
turtle.right(90)
turtle.forward(150)
turtle.pendown()

turtle.color("blue")
command = 0
while command < 25:
    command += 1
    for i in range(4):
        turtle.forward(20)
        turtle.right(90)
    turtle.forward(5)
    turtle.right(15)
print(turtle.position())
turtle.exitonclick()

