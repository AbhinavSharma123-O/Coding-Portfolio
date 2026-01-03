class Account:
    def __init__(self,amt):
        self.balance=amt
        return
    def deposit(self,amt):
        self.balance=self.balance+amt
        
    def withdraw(self,amt):
        if(amt<=self.balance):
            self.balance=self.balance-amt
        else:
            print("Low Balance")
acc=Account(5000)
print(acc.balance)
acc.deposit(4000)
print(acc.balance)
acc.withdraw(6000)
print(acc.balance)
