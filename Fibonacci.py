# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this 
# opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers 
# in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the 
# sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
num = int(input("How many fibonacci numbers would you like to generate? "))

def Fibonacci(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return Fibonacci(x - 1) + Fibonacci(x - 2)

print(Fibonacci(num))