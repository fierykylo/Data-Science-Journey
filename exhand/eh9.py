class InsufficientBalanceError(Exception):
    pass


try:
    balance = float(input("Enter balance: "))
    withdraw = float(input("Enter withdrawal amount: "))

    if withdraw > balance:
        raise InsufficientBalanceError("Insufficient balance!")

    balance -= withdraw
    print("Withdrawal successful. Remaining balance:", balance)

except InsufficientBalanceError as e:
    print("Error:", e)