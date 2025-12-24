# Rock, Paper, Scissors game
import random

while True :
    sign = input("Rock, Paper, Scissors ? (r/s/p) : ").lower()
    if sign == 'r' or sign == 'p' or sign == 's' :
        if sign == 'r' :
            # rock = 1, paper = 2, scissors = 3
            symbol1 = random.randint(1,3)
            if (symbol1 == 1):
                print("You chose 🪨\nComputer chose 🪨")
                print("Tie")
            elif (symbol1 == 2):
                print("You chose 🪨\nComputer chose 📃")
                print("You lose")
            elif (symbol1 == 3):
                print("You chose 🪨\nComputer chose ✂️")
                print("You win")
        elif sign == 'p' :
            # rock = 1, paper = 2, scissors = 3
            symbol2 = random.randint(1,3)
            if (symbol2 == 1):
                print("You chose 📃\nComputer chose 🪨")
                print("You win")
            elif (symbol2 == 2):
                print("You chose 📃\nComputer chose 📃")
                print("Tie")
            elif (symbol2 == 3):
                print("You chose 📃\nComputer chose ✂️")
                print("You lose")
        elif sign == 's' :
            # rock = 1, paper = 2, scissors = 3
            symbol2 = random.randint(1,3)
            if (symbol2 == 1):
                print("You chose ✂️\nComputer chose 🪨")
                print("You lose")
            elif (symbol2 == 2):
                print("You chose ✂️\nComputer chose 📃")
                print("You win")
            elif (symbol2 == 3):
                print("You chose ✂️\nComputer chose ✂️")
                print("Tie")
        restart = input("Continue? (y/n) : ").lower()
        if restart == 'y':
            continue
        elif restart == 'n':
            break
        else :
            print("Invalid choice")
            break
    else :
        print("Invalid choice")