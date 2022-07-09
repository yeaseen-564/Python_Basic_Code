# Creating class and object using <def __init__> :
# Here I will use <INHERITANCE>:

class Vehicle:  # class named <Vehicle> which is <global class>
    def __init__(self, name, color, founder, founding_year, power, direction):
        self.name = name
        self.color = color
        self.founder = founder
        self.founding_year = founding_year
        self.power = power
        self.direction = direction

    def start(self):  # function/Method of <class 'vehicle'>
        print(f"Starting the engine of {self.name}")

    def brake(self):  # function/Method of <class 'vehicle'>
        print(f"Braking the car {self.name}")

    def drive(self):  # function/Method of <class 'vehicle'>
        print(f"Driving car {self.name}")

    def turn(self):
        print(f"{self.name} is turning to {self.direction}")


class Car(Vehicle):  # <class 'Car'> derived from <class 'Vehicle'>
    pass


my_car = Car("Marci-ties", "Black", "Gogo-tim", "2022", "6000000 cc", "left")  # Object of <class 'Car'>

my_car.start()  # Method/Function derived from <class 'Vehicle'>
my_car.drive()  # Method/Function derived from <class 'Vehicle'>
my_car.brake()  # Method/Function derived from <class 'Vehicle'>
my_car.turn()  # Method/Function derived from <class 'Vehicle'>


class Honda(Vehicle):  # <class 'Honda'> derived from <class 'Vehicle'>
    pass


r15 = Honda("R-15", "Black-Red", "Apollo-g7", "2022", "2000 cc", "right")  # Object of <class 'Car'>

r15.start()  # Method/Function derived from <class 'Vehicle'>
r15.drive()  # Method/Function derived from <class 'Vehicle'>
r15.brake()  # Method/Function derived from <class 'Vehicle'>
r15.turn()  # Method/Function derived from <class 'Vehicle'>
