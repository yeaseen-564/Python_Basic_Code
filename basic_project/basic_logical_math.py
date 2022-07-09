print("=-=-=-=-=-Python (Basic code) Calculator-=-=-=-=-=-=")
number1 = int(input("Please input the first integer : "))
number2 = int(input("Please input the first integer : "))
print('''Press 0 for Addition,
Press 1 for Subtraction,
press 2 for Multiplication,
Press 3 for Division''')
#
int_press = int(input("Please Press the existing numbers : "))


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


if int_press == 0:

    print(add(number1, number2))
elif int_press == 1:
    print(subtract(number1, number2))
elif int_press == 2:
    print(multiply(number1, number2))
elif int_press == 3:
    print(divide(number1, number2))

print("Thanks for being with us")
