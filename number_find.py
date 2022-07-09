import random

number = random.randint(1, 100)
print(f"Clue: {number+100}, {number-200}, {number+200}, {number-100}")
attempt = 0
while True:
    _input_number = int(input("Guess any number between(1-100): "))
    attempt += 1
    if _input_number == number:
        print("Yes, You correctly guessed the number.")
        break
    elif _input_number < number:
        print("Nope!Try to guess a large number")
        continue
    elif _input_number > number:
        print("Nope!Try to find a small number")
        continue
print(f"You have tried {attempt} times to find it")
