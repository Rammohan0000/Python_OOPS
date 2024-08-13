class BankAccount:
    def __init__(self):
        self.Account_holder = "XYZ"
        self.Balance = 10
        
    def getinfo(self):
        print(f"Account Information: {self.Account_holder},  {self.Balance}")
  
account = BankAccount()
account.getinfo() 