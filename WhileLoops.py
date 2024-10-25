### Part Two -- your code goes here. 
import random 
variable = random.randint(1, 100)

number = int(input("Guess a random number between 1 and 100: "))

while number != variable:
    if number > variable:
        print("Guess is too high")
        number = int(input("Guess a random number between 1 and 100: ")) 
    elif number < variable:
        print("Guess is too low")
        number = int(input("Guess a random number between 1 and 100: ")) 

print("number has been guessed")
