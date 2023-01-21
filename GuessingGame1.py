# Generate a random number between 1 and 9 (including 1 and 9). Ask the user 
# to guess the number, then tell them whether they guessed too low, too high, 
# or exactly right. 
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random

randInt = (random.randint(1,9))
guess = 0
count = 0
while guess != randInt:
    guess = int(input("Guess the random number between 1 and 9: "))

    if guess == "exit":
        break

    if guess > randInt:
        print("Too high")
    elif guess < randInt:
        print("Too low")
    else:
        print("You got it right!")
    count = count + 1

print("It took you this many tries: " + str(count))