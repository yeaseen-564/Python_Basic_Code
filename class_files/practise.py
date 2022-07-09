# Inheritance
class Animal:  # Base class
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} can walk")

    def eat(self):
        print(f"{self.name} can eat")

    def sleep(self):
        print(f"{self.name} can sleep")


class Human(Animal):  # Derived class
    def dance(self):
        print(f"{self.name} can dance")


class Dog(Animal):  # Derived class
    pass


# Objects
man = Human("Yeaseen")
dog = Dog("Tom")

# Outputs for object man
man.walk()
man.eat()
man.sleep()
man.dance()

# Outputs for dog object
dog.walk()
dog.eat()
dog.sleep()


