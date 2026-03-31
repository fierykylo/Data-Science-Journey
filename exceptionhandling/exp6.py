#  Write a Python program that prompts the user to input two numbers
#  and raises a TypeError exception if the inputs are not numerical. 

try:
    a = int(input("Enter : "))
    b = int(input("Enter : "))
except ValueError:
    raise TypeError("The value must be numerical!!")

