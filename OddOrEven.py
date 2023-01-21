#Ask the user for a number. Depending on whether the number is even or odd,
 #print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
num = input("Enter a number: ")
num = int(num)
mod = num % 2
if mod > 0:
    print("The number is odd")
else:
    print("The number is even")