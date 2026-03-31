#.	Write a Python program to:
# •	Define a custom exception called NegativeNumberError 
# •	Raise the exception if the user enters a negative number 
# •	Display an appropriate message

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    
    if num < 0:
        raise NegativeNumberError("Number cannot be negative")
    
    print("You entered:", num)

except ValueError:
    print("Please enter a valid number")

except NegativeNumberError as e:
    print("Error:", e)