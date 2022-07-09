# mark=int(input("Please enter your mark of any subject : "))
#
# if mark > 100:
#     print("Try to input correct number! Programme Terminated")
# elif mark >= 80:
#     print("Congratulations, Your grade is A+ with ",mark)
# elif mark >= 70:
#     print("Your grade is A with ",mark)
# elif mark >= 60:
#     print("Your grade is A- with ",mark)
# elif mark >= 50:
#     print("Your grade is B with ",mark)
# elif mark >= 40:
#     print("Your grade is C with ",mark)
# elif mark >= 30:
#     print("Your grade is D with ",mark)
# else:
#     print("Oops! You have Failed! with ",mark)


_input_number = int(input("Please enter an integer: "))


if _input_number % 2 == 0:
    print(f"{_input_number} is even number")
elif _input_number <= -1:
    print(f"{_input_number} is minus")
else:
    print(f"{_input_number} is odd number")

# for i in range(1, 100+1):
# if i % 2 == 0:
#     print(i, "is even number")
# else:
#     print(i, "is odd number")

