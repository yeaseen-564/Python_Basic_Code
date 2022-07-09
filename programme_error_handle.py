try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(age, ",", risk)
except ValueError:
    print("Try to define integer")
except ZeroDivisionError:
    print("Age cannot be zero")

