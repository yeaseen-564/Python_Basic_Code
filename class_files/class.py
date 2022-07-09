# class Point:
#     def move(self):
#         print("Move")
#
#     def draw(self):
#         print("Draw")
#
#
# point1 = Point()
# point1.draw()
# point1.move()
# point1.x = 12
# point1.y = 90
# print(f"point.x = {point1.x}, point.y = {point1.y}")
#


class Mammal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")


class Dog(Mammal):
    pass


dog = Dog("Jhon")
dog.walk()
