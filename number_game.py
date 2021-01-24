import random

number_range = list(range(1, 11))
min_range = min(number_range)
max_range = max(number_range)
number = random.randint(min_range, max_range)

prompt = "\nI'm thinking of an integer between " + str(min_range) + " and " + str(max_range) + "."
prompt += "\nGuess the number or type 'quit' to exit: "

guess = input(prompt)

active = True

while active:
     if guess != 'quit':
        try:
            int(guess)
        except:
            guess = input("That is not a number! Try again: ")
            continue
    if guess == 'quit':
        print("\nThanks for playing!")
        active = False
    elif int(guess) not in number_range:
        guess = input("\nOut of range! Guess an integer between " + str(min_range) + " and " + str(max_range) + ": ")
    elif int(guess) < number:
        guess = input("\n" + guess + " is too low! Try again: ")
    elif int(guess) > number:
        guess = input("\n" + guess + " is too high! Try again: ")
    elif int(guess) == number:
        guess = input("\nCongratulations! "
                      + guess + " is correct!\n\nEnter 'Y' to play again or enter any key to exit: ")
        if guess.upper() == 'Y' or guess.upper() == 'YES':
            number = random.randint(min_range, max_range)
            guess = input(prompt)
            continue
        else:
            print("\nThanks for playing!")
            active = False
