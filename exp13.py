#handle all types of error in your best possible capacity

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 12, 19, 21]

try:
    num = int(input("Enter the index for numerator"))
    den = int(input("Enter the index for denominator"))
    numerator = numbers[num]
    denominator = numbers[den]
    result = numerator // denominator
    print(result)
except ValueError:
    print("Please enter a valid value")
except IndexError:
    print("Please enter a valid index")
except ZeroDivisionError:
    print("Can't Divide by Zero you chose denominator with value 0")
except ArithmeticError:
    print("Error!!")