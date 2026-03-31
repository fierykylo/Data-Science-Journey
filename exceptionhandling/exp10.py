# 	Write a program that:
# •	Raises a custom exception WeakPasswordError if password: 
# •	Is less than 8 characters 
# •	Does not contain a digit

class WeakPasswordError(Exception):
    pass

def check_digit(password):
    return any(char.isdigit() for char in password)

try:
    password = input("Enter a password")
    if len(password) < 8:
        raise WeakPasswordError("Must be atleast 8 characters long")
    
    if not check_digit(password):
        raise WeakPasswordError("Must atleast contain one digit")

    print("Strong Password!!")
    
except WeakPasswordError as e:
    print(f"Error: {e}")
