'''
  Starter Code for number guessing game
  
  Please enter your team members names here:
  Michael Alvarez
  Armando
'''

# Begin your code here
import random
rn = random.randint(1, 100)

while True:
    guess = int(input("Guess the number "))
    if guess == rn:
        print("You Win")
        break
    elif guess > rn:
        print("Too High")
    elif guess < rn:
        print("Too Low")