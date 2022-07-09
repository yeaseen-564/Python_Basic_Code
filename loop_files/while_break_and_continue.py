# action = ""
# while action != "e":
#     _input = input(" (O)k to continue or (E)xit to exit :")
#
#     if _input.lower() not in ["o"]:
#         print("Unknown operation")
#         break
#
#     n1 = int(input("Enter a number: "))
#     n2 = int(input("Enter the second number: "))
#     command = input("Enter add/sub to make any operation and (E)xit to exit: ")
#
#     if command.lower() == "add":
#         print(f"Addition is : {n1 + n2}")
#         break
#     elif command.lower() == "sub":
#         print(f"Subtraction is : {n1 - n2}")
#         break
#     elif command.lower() == "e":
#         break
#     elif command not in ["add", "sub"]:
#         print("Unknown operation")
#         continue

#
# while True:
#     _input = input(">>> ")
#
#     if _input == "help":
#         print("""To start -- start
# To stop -- stop
# To quit -- exit """)
#
#     elif _input == "start":
#         print("Car started.Ready to go...")
#
#     elif _input == "stop":
#         print("Car stopped.This won\'t run.")
#
#     elif _input == "exit":
#         break
#
#     else:
#         print("Unknown Operation.I can\'t understand")

while True:
    new = input("Y/n")

    if new.lower() == "n":
        break
    elif new.lower() not in ["y", "n"]:
        print("????")
        continue

    command = "-"
    while command != "_":
        _input = input(">>> ")

        if _input.lower() == "exit":
            break
        elif _input.lower() == "help":
            print("""For name: name,
For version: v""")
        elif _input.lower() == "name":
            print("You are driving BMW-451")
            break
        elif _input.lower() == "v":
            print("Your version of Honda is v-54G34,Gen-10")
            break
        else:
            print("I don't understand this type of word.Please type a valid str")
            continue

    break


