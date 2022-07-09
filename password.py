# input_pass = input("Create a password: ")
# input_pass_again = input("Rewrite the password: ")
# index = 0
#
# while input_pass != input_pass_again:
#     print("Password don\'t match.Try again...")
#     input_pass = input("Create a password: ")
#     input_pass_again = input("Rewrite the password: ")
#     if input_pass == input_pass_again:
#         print("You\'re Registered successfully...")
#
# while index < 3:
#     enter_pass = input("Enter your password: ")
#
#     if enter_pass != input_pass and enter_pass != input_pass_again:
#         print("Try to enter a valid password...")
#
#     elif enter_pass == input_pass and enter_pass == input_pass_again:
#         print("You\'re authorized")
#         break

# ????????????????????????????????????????????????????????????????????????

# password = "1"
# password_again = "_"
# while password != password_again:
#     password = input("Create a password: ")
#     password_again = input("Rewrite the same password: ")
#
#     if password == password_again:
#         print("You are registered")
#         break
#     else:
#         print("First register yourself")
# index = 0
# hidden_number = 4
# while index < 3:
#     index += 1
#     guess = int(input("Guess any number: "))
#     if guess == hidden_number:
#         print("You won")
#         break
#     else:
#         print("You failed")

# ????????????????????????????????????????????????????????????????????????????????????

_input = "_"
_input_again = ""

while _input != _input_again:
    _input = input("Create a strong password: ")
    _input_again = input("Rewrite the same password: ")
    if _input != _input_again:
        print("Password didn't match.Try again....")
        continue
    elif _input == _input_again:
        print("Password match successful")
        break
while True:
    command = input(">>> ")
    if command == "help":
        print("""For name == N
To start == start
To stop == stop
To speed up == speed>>
To exit == exit""")
    elif command == "start":
        print("Started Successfully.Ready to go...")
    elif command == "stop":
        print("Successfully stopped.")
    elif command == "speed>>":
        print("Speeding up >>>>> ")
    elif command == "exit":
        break
    elif command == "N":
        print("You are driving Lambo-V12")
    else:
        print("I don't understand that.What are you doing?")








