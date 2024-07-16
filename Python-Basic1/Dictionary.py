#THIS PROGRAM IS SHOWING THE WORKING OF DICTIONARY AND ITS PROPERTIES WITH FUNCTION...
Phone_no1={
    'Harsh':12347,
    'Sunil':14576,
    'Rohan':89762,
    'Raman':34564
}
print(Phone_no1)
Phone_no2=dict(
    {
        'Rahul':345.32,
        'Ishaan':90877,
        'Elon':90786,
        'Mark':'UTES'
    }
)
print(Phone_no2)
print(Phone_no2['Rahul'])
Phone_no2['Rahul']="Heelo"
print(Phone_no2)
#print(Phone_no2['rahul'])#Give Error Because It Work On Case Sencevity
#You can add in Dictionary set,tuple,list and etc.
Phone_no1['ABHI']=123
print(Phone_no1)
Phone_no1['ABHI']=(1,2,3,4,5,6)
print(Phone_no1)
Phone_no1['Shivam']={
    'Shivam-Home':78622,
    'Shivam-Girl':34562,
    'Shivam-Work':56332
}
print(Phone_no1)
print(Phone_no1['ABHI'])
print(Phone_no1['Shivam'])
print(Phone_no1['Shivam']['Shivam-Home'])
#You can access the data or value using get functinon
print(Phone_no1.get('Shivam'))
print(Phone_no1.get('Shivam-Home'))
#Duplicate Is Not Allowed
Phone_no3={
    'Ram':78.,
    'Dola':45,
    'Ram':34,
    'Sunil':23,
}
print(Phone_no3)
#Functions
#*del
del Phone_no3['Ram']
print(Phone_no3)
#*pop()
print(Phone_no3.pop('Dola'))#It return Only value after pop
#*popitem()
print(Phone_no3.popitem())#It Return Key and value Both Before Pop
#*clear()
Phone_no3.clear()
print(Phone_no3)
#*Keys()
print(Phone_no1.keys())
#*Values()
print(Phone_no1.values())
#*Items()
print(Phone_no1.items())
#*Copy()
Phone_no3=Phone_no2.copy()
print(Phone_no3)
#*Len()
print(len(Phone_no1))
#Dictionaries Access from loop.
print('Key and Values Of Phone_No1')
for i in Phone_no1:
    print(i)
    print(Phone_no1[i])
print('Key And Values Of Phone_No2')
for i in Phone_no2.items():
    print(i)