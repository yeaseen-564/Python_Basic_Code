import random
import turtle
print(random.randint(10, 102102))
colors = ["red", "green", "blue", "purple", "orange"]
turtle.speed(0)
for i in range(100):
    # turtle.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.setposition(x, y)
    # random color
    random_color = random.randint(0, len(colors)-1)
    turtle.dot(10, colors[random_color])
turtle.exitonclick()

