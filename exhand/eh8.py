class InvalidAgeError:
    pass

try:
    age = int(input("Enter your age : "))
     
    if(age < 18):
        raise InvalidAgeError("Must be older than 18")
    elif (age > 60):
        raise InvalidAgeError("Too old!!")
    else:
        print("You are eligible to vote !!")
except ValueError as e:
    print("Error : ", e)
except InvalidAgeError as e:
    print("Error : ", e)
    