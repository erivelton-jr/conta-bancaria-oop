class Bank:
    def __init__(self, account, balance=0):
        self.account = account
        self.balance = balance
    
    def withdraw(self, withdraw):
        self.balance -= withdraw
        if self.balance < withdraw:
            print('Not enough balance!')

    def deposit(self, deposit):
        self.balance += deposit
        
    def display(self):
        print(f'Hello {self.account}! You have {self.balance}$')



user = Bank('Jr', 50)
user.deposit(500)
user.withdraw(236)
user.display()
user.withdraw(7999)

        
