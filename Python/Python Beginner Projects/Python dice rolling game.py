import random

while True:
    Roll = input("Roll the dice ? (y/n) : ")
    if Roll == 'y' or Roll == 'Y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif Roll == 'n' or Roll == 'N':
        print("Thanks for playing !")
        break
    else:
        print("Invalid choice")