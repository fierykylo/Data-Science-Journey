
class InsufficientBalanceError(Exception):
    pass



class BankAccount:
    def __init__(self, account_no, account_holder_name, transactions):
        self.account_no = account_no
        self.account_holder_name = account_holder_name
        self.transactions = transactions
        self.balance = sum(transactions)
        self.status = False


    def checkStatus(self):
        if self.balance < 1000:
            self.status = False
        else:
            self.status = True
        return self.status


    def deposit(self, amount):
        try:
            amount = float(amount)
        except TypeError:
            print("Please enter numeric value only")
        self.balance += amount
        self.transactions.append(amount)
        print(f"{amount} deposited successfully.")

    
    def withdraw(self, amount):
        try:
            amount = float(amount)
        except TypeError:
            print("Please enter numeric value only")
        if self.balance - amount < 0:
            raise InsufficientBalanceError("Withdrawal failed: Insufficient balance!")
        else:
            self.balance -= amount
            self.transactions.append(-amount)
            print(f"{amount} withdrawn successfully.")


try:
    acc1 = BankAccount(101, "Aarush", [2000, -500, 300, -200, 100])
    acc2 = BankAccount(102, "Sarthak", [1500, -700, -300, 200, -100])
    acc3 = BankAccount(103, "Ganpat Sir", [1000,1000,2000,-6000])
    acc4 = BankAccount(104, "Aman", [(1000,1000,1000)])
except:
    print("Please initialise the class corectly[account num(numeric), name = float(), transactioins() ]")


try:
    acc1.deposit(500)
    acc1.withdraw(3000)
except AttributeErrorError:
    print("No such methods!!")
except InsufficientBalanceError as e:
    print(e)

try:
    acc2.deposit(200)
    acc2.withdraw(1000)
except AttributeError:
    print("No such methods!!")

except InsufficientBalanceError as e:
    print(e)

try:
    print(acc4.balance)
    acc4.deposit(1000)
    acc4.withdraw(100)
except AttributeError:
    print("No such methods!!")
except InsufficientBalanceError as e:
    print(e)


print("\nAccount 1:")
print("Balance:", acc1.balance)
print("Status:", "ACTIVE" if acc1.checkStatus() else "INACTIVE")

print("\nAccount 2:")
print("Balance:", acc2.balance)
print("Status:", "ACTIVE" if acc2.checkStatus() else "INACTIVE")

print("\n ACCOUNT 3")



