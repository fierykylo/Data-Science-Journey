# 	Write a program that:
# •	Accepts age from user 
# •	Raises a custom exception InvalidAgeError if: 
# •	Age < 18 → "Not eligible" 
# •	Age > 60 → "Too old for this policy"

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age : "))
    if age < 18:
        raise InvalidAgeError("Not Eligible")
    if age > 60:
        raise InvalidAgeError("Too old for this policy")
except ValueError as e:
    print(f"Error :  {e}")
except InvalidAgeError as e:
    print(f"Error : {e}")
