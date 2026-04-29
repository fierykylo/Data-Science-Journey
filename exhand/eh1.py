try:
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number : "))
     
    result = num1 / num2
    print(result)
except ZeroDivisionError as e:
    print("Error", e)
    