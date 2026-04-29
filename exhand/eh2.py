try:
    value = int(input("Enter an integer: "))
    if not value.isdigit():
        raise ValueError("PLease enter a valid integer")
except ValueError as e:
    print(e)
    
