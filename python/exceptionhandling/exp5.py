try:
    a = int(input("Enter : "))
    b = int(input("Enter : "))
    res = a / b
    print(f"The result is {res}")
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Division by zero not allowed")
except ArithmeticError:
    print("Error: Arithmetic Error")
