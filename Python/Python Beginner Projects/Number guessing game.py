import random
value = random.randint(1,100)
guess = 0
while True: 
  num = int(input("Enter number from 1 to 100 : "))
  if value == num :
     print("Congratulations! You guessed the number.")
     break
  elif value > num : # 34 > num
     print("Too low")
  elif value < num : # 34 < num
     print("Too high")
  guess += 1
print(f"\nGuessed in {guess}, guesses.")