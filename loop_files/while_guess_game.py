index = 0
loop_limit = 3
hidden_number = 7
while index < loop_limit:
    guess = int(input("Guess a number between 1 and 10: "))
    index += 1
    if guess == hidden_number:
        print("You guessed it!")
        break
    else:
        print("Wrong!")
else:
    print("Sorry, you failed!")
