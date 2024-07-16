#THIS PROGRAM IS SHOW BANK HOLDER DETAILS AND TRANSCATIONS DATA...
class Bank_Account:
    def __init__(self,name,amount):
        self.name=name
        self.Balance=amount
    def __str__(self):
        return f'Account Holder Name Is Mr/Mrs {self.name} and Account Balance is {self.Balance}'
    def Deposite(self,balance):
        self.Balance=self.Balance+balance
        return f'Amount Deposite Succesfully and Current Amount is:-{self.Balance}'
    def Withdrawl(self,balance):
        if self.Balance>balance:
             self.Balance=self.Balance-balance
             return f'Amount Withdrawl Succesfully and Current Amount is:-{self.Balance}'
        else:
            return f'Insuffisent Balance'
person1=Bank_Account('Harsha',1000)
print(person1)
print(person1.Deposite(1000))
print(person1.Withdrawl(10000))


