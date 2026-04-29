class NegativeNumberError(Exception):
    pass

try:
    a = int(input("Enter a number : "))
    if (a < 0):
        raise NegativeNumberError("The number must be greater than 0")
    print(a)
except ValueError as e:
    print("Error : ", e)
except NegativeNumberError as e:
    print("Error : ", e)

    