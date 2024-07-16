#THIS PROGRAM IS SHOW BASICALLY A DEPOSITE AND WITHDRAWAL THE MONEY IN BANK ACCOUNT...
class Bank_Account:
    Amount=0
    def Deposite(self,D_amount):
        self.Amount=D_amount+self.Amount
        return f'Succesfully Deposite And Current Balance Is:-{self.Amount}'

    def Withdraw(self,W_amount):
        if W_amount>self.Amount:
            return f'Insufficent Balance'
        else:
            self.Amount=self.Amount-W_amount
            return f'Succesfully And Current Balance Is:-{self.Amount}'

Person1=Bank_Account()
Condition=1

while Condition==1:
    print('Welcome To XYZ Bank Money Deposite And Withdrawl System')
    print('1 for Deposite and 2 For Withdrawl')
    Choice=int(input('Enter Your Choice:-'))
    if Choice==1 or Choice==2:
        if Choice==1:
            amount=int(input('Enter The Deposite Amount:-'))
            print(Person1.Deposite(amount))
        else:
            amount = int(input('Enter The Withdrawl Amount:-'))
            print(Person1.Withdraw(amount))
    else:
        print('Press Only Required Or Optinal Key')
    Condition=int(input('Do You Want To Continue Press 1 or For Not Press 0:-'))