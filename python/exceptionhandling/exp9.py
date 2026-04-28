# 	Write a Python program that:
# •	Defines a custom exception InsufficientBalanceError 
# •	Accepts balance and withdrawal amount 
# •	Raises exception if withdrawal amount exceeds balance

class InsufficientBalanceError(Exception):
    pass



try:
    balance = int(input("Enter the balance : "))
    amount = int(input("Enter the withdrawl amount : "))
    if amount > balance:
        raise InsufficientBalanceError("Not enough funds!!")
    balance -= amount
except ValueError as e:
    print(f"Error: {e}")
except InsufficientBalanceError as e:
    print(f"Error: {e}")
