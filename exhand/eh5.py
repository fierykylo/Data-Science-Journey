try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ArithmeticError:
    print("Error: Arithmetic operation failed!")