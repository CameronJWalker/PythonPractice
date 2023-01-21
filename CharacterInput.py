## Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. 
## Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year)
name = input("What is your name?: ")
age = input("How old are you?: ")
age = int(age)
hundred = (2023 - age) + 100
print(name + " you will be 100 years old in the year " + str(hundred)  )