# Ask the user for a string and print out whether this string is a palindrome or not.
#  (A palindrome is a string that reads the same forwards and backwards.)

str = input("Enter a word: ")

reverseStr = str[::-1]
if str == reverseStr:
    print("This is a palindrome!")
else:
    print("This is not a palindrome!")
    

