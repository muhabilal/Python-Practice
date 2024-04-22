#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
userInput=input("Enter a list of numbers")
list=userInput.split(",")
tuple=tuple(list)
# Print the list
print('List : ', list)

# Print the tuple
print('Tuple : ', tuple)