# simple python calculator

operator = input("Enter an operator (+, -, *, /): ")

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    if num2 == 0:
        print("Division not possible — cannot divide by zero!")
    else:
        print(num1 / num2)

else:
    print(f"{operator} is not a valid operator.")
