#just some conditional statements

age = int(input("Enter your age : "))

if age < 0:
    print("Invalid age, enter a positive number")
elif age >= 18:
    print("You are eligible to vote")
else:
    print("You must be 18+ to sign up")

