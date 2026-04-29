class InsufficientBalanceError(Exception):
    pass

class BankAccount:

    def __init__(self,account_no, account_holder_name,transactions):
        self.account_no = account_no
        self.account_holder_name = account_holder_name
        self.transactions = transactions
        self.balance = sum(transactions)
        self.status = True

    def check_status(self):
        self.balance = sum(self.transactions)

        if(self.balance < 1000):
            self.balance = False
        else:
            self.balance = True
        
        return self.balance
    
    def deposit(self,amount):

        self.transactions.append(amount)
        self.balance += amount
        print(f"Deposited {amount} in account!!")

    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise InsufficientBalanceError("Withdrawal would cause negative balance!")

        self.transactions.append(-amount)
        self.balance -= amount
        print("Withdrawn:", amount)

    

        