command = ""
started = False


while command.lower() != "exit":
    input_command = input(">>> ")
    if input_command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif input_command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif input_command == "stop":
        if not started:
            print("Already stopped...")
        else:
            started = False
            print("Car stopped...")
    elif input_command == "exit":
        break
    else:
        print("Sorry, I don't understand that...")



