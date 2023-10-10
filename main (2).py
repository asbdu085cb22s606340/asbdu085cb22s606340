class BankAccount:
  def __init__(self,balance=0):
    self.balance=balance
  def deposit(self,amount):
    self.balance+=amount
    print(f"Deposited {amount}units.current balance:{self.balance}units")
  def withdraw(self,amount):
    if self.balance>amount:
      self.balance-=amount
      print(f"withdrawn {amount}units.current balance:{self.balance}units")
    else:
      print("Insufficient funds.")
  def get_balance(self):
      print(f" current balance:{self.balance}units")

account=BankAccount()
account.get_balance()
account.deposit(1000)
account.get_balance()
account.withdraw(500)
account.get_balance()
    


