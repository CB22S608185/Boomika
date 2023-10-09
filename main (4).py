






class BankAccount:

  def__int__(self,account_number, account_holder_name,initial_balance=0,0):
self.account_number=account_number
self.account_holder_name=account_holder_name
self.account_balance=initial_balance

def deposit (self, account):
  if amount > 0:
    self.__account_balance +=amount
#self.__account_balance=self.__account_balance + amount
print("Deposited ₹{}.New balance ${}". format(amount,self.__amount_balance) 

      else:
print("invalid deposit amount.please deposit a positive amount.")

def withdrawal (self,amount):
  if amount > 0and amount <=self.__account_balance:
    self.__account_balance -= amount
    #self.__account_balance = self.__account_balance-amount
print("withdraw ₹{}.New balance: ₹{}".format(amount,self.__amount_balance))

else:
print("invalid withdrawal amount or insufficient balance.")

def display_balane(self):
print("Account balance for {} (Account #{}):₹{}"format (
  self.__account_holder_name, self.__account_number,
  self.__account_balance)) 


#create an instance of the BankAccount class 
account = BankAccount(amount_number="123456789"
    amount_holder_name= hari prabu,
    initial_balance=5000.0)

#Test deposit and withdrawal functionally
account.display_balance()
amount.deposit(500.0)
amount.withdraw(200.0)
amount.withdraw(2000.0)
amount.display_balance()