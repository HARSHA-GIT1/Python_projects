#THIS PROGRAM IS SHOWING THE WORKING OF PASSWORD GENRATOR...
import random
List1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
List2=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z']
List3=['!','@','#','$','%','^','&','*','(',')','{','}','[',']',':',';','?','/','<','>','+','-','=','|']
print("Welcome To Password Generator")
Num=int(input("Enter the no of Numerical digits: "))
Char1=int(input("Enter the no of Capital Alphabets: "))
Char2=int(input("Enter the no of Small Alphabets: "))
Sym=int(input("Enter the no of Symbols: "))
password_list=[]
for i in range(1,Num+1):
    no=random.randrange(0,10)
    password_list+=str(no)
for i in range(1,Char1+1):
    char1=random.choice(List1)
    password_list+=char1
for i in range(1,Char2+1):
    char2=random.choice(List2)
    password_list+=char2
for i in range(1,Sym+1):
    sym=random.choice(List3)
    password_list+=sym
password1=""
for i in password_list:
    password1+=i
print('Your Simple password is: ',password1)
random.shuffle(password_list)
password2=""
for i in password_list:
    password2+=i
print('Password in Strong Mode is: ',password2)