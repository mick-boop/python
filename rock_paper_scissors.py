# Rock, Paper, Scissors game that keeps score

import random

x_beats_y = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

computer_score = 0
player_score = 0
quits = ['quit']

active = True

while active:
    computer = random.choice(list(x_beats_y.values()))
    user_choice = input("\nEnter rock, paper, or scissors, or enter quit to stop playing: ")
    if user_choice.lower() in quits:
        print("\nThanks for playing!")
        active = False
    elif user_choice.lower() not in list(x_beats_y.values()):
        continue
    else:
        if user_choice.lower() == computer:
            print("\nComputer chose " + computer)
            print("It's a tie!")
            print("\nScore\nComputer: " + str(computer_score) + "\nPlayer: " + str(player_score))
            repeat = input("\nEnter quit to leave, or enter any key to play again: ")
            if repeat.lower() in quits:
                print("\nThanks for playing!")
                active = False
            else:
                continue
        elif (user_choice.lower(), computer) in x_beats_y.items():
            print("\nComputer chose " + computer)
            print("You win!")
            player_score += 1
            print("\nScore\nComputer: " + str(computer_score) + "\nPlayer: " + str(player_score))
            repeat = input("\nEnter quit to leave, or enter any key to play again: ")
            if repeat.lower() in quits:
                print("\nThanks for playing!")
                active = False
            else:
                continue
        else:
            print("\nComputer chose " + computer)
            print("You lose!")
            computer_score += 1
            print("\nScore\nComputer: " + str(computer_score) + "\nPlayer: " + str(player_score))
            repeat = input("\nEnter quit to leave, or enter any key to play again: ")
            if repeat.lower() in quits:
                print("\nThanks for playing!")
                active = False
            else:
                continue
