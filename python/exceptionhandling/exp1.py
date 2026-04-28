try:
    num = int(input("Enter the numerator : "))
    den = int(input("Enter the denominator : "))
    result = num / den
    print(f"the result is {result}")
except ZeroDivisionError:
    print("Cant divide by 0 baka!!")
