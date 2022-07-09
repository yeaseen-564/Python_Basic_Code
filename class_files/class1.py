# Creating class and object:
# There is no use of <def __init__>:

class Car:  # class
    name = ""
    color = ""
    _type = ""

    def start(self):
        print(f"{self.name} is starting the engine")

    def stop(self):
        print(f"{self.name} is stopping the engine")


my_car = Car()  # Object of <class> Car

my_car.name = "Marci-ties"  # Using the methods/functions of <class> Car
my_car.start()
my_car.stop()

my_car.name = "Bugatti"  # Using the methods/functions of <class> Car
my_car.start()
my_car.stop()




