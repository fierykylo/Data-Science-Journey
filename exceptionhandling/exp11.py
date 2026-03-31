# 	Create a program that:
# •	Accepts marks (0–100) 
# •	Raises custom exception InvalidMarksError if: 
# •	Marks < 0 or > 100


class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter marks : "))
    if marks < 0:
        raise InvalidMarksError("Marks cant be less than 0")
    if marks > 100:
        raise InvalidMarksError("Maximum marks 100")
    
    print("marks successfully logged!!")
except ValueError:
    print("Please enter numeric values only!!")
except InvalidMarksError as e:
    print(f"Error: ", e)
