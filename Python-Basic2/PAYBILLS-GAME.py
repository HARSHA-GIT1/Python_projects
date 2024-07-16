#THIS PROGRAM FOR SHOWING THE WORKING OF PAYBILL GAME....
import random
'''data=['Sunil','Raman','Neeraj da','Abhimanyu','Harsh','Ganesh']
result=random.choice(data)
print(result,'Pay today Bill')'''
#OR
data=input('Enter the names of guests: ')
if(data =="Neeraj"):
        data='Vijay'
newdata=data.split()#This function sperate the all words as from parameters to lists...
print(' Guests Name is : ',newdata)
payguest=random.randrange(0,len(newdata))
print('Today payment is credited from Mr',newdata[payguest])
print('Thanks To All For Giving Your Presence In Our Resort')

