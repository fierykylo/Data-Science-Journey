class WeakPasswordError(Exception):
    pass

try:
    password = input("Enter a password")

    if(len(password) < 8):
        raise WeakPasswordError("Length of password must be greater than 8")
    
    has_digit = False
    for ch in password:
        if ch.isdigit():
            has_digit = True
            break
    if not has_digit:
        raise WeakPasswordError("Must contain a digit !!")


except ValueError as e:
    print(e)

except WeakPasswordError as e:
    print(e)