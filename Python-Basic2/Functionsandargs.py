#THIS PROGRAM IS SHOWING THE WORKING OF FUNCTIONS...
def Intro():
    print('Hello')
Intro()

#Function With Arguments Or Parameters
#Position:-
'''def Sum(a,b):
    print(f'Sum of {a} and {b} is:',(a+b))
a=int(input('Enter First No:'))
b=int(input('Enter Second No:'))
Sum(a,b)'''

#Or
def Intro(name,age):
    print('Hello',name,'Your Age is',age)
Intro("Harsh","19")
Intro("19","Harsh")


#Keyword:-
def Intro(name,age):
    print('Hello',name,'Your Age is',age)
Intro("Harsh","19")
Intro("19","Harsh")
Intro(name="Harsh",age="19")
Intro(age='19',name='Harsh')
Intro("Harsh",age='19')
#Intro(age='19','Harsh')#Give Error Because poistion came before keyword...


#Arbitory:-
#(i)Position Arbitory
def Sum(a,b):
    print("Sum is:",(a+b))
Sum(2,3)
#Sum(2,3,4)#Give Error
#But Using Posi-Arbitory arg...
def Sum(*No):#(Here No work as Tuple)
    c=0
    for i in No:
        c=c+i
    print('Sum is:',c)
Sum(1,2,3,4,5,6)


#(ii)Keyword Arbitory
def Introduction(**Intro):
    for key,value in Intro.items():
        print(key,value)#Note:-Here keyword arbi work on dictionaries(Key and value)...
Introduction(name="Harsh",age='19',add='Khirwa')

