#Create a program that asks the user for a number and then prints out a
# list of all the divisors of that number. (If you don’t know what a 
# divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
num = int(input("Enter a number to find its divisors: "))

divisors = []
x = 0
while x < num:
    x += 1
    y = num % x
    if y== 0:
        divisors.append(x)
    else:
        print(str(x) + " is not a factor of " + str(num))
print(divisors)
