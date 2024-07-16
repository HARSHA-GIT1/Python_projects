#THIS PROGRAM IS SHOWING THE WORKING OF LOOP-CONTROLER STATEMENT...
#Break:-
'''count=[1,2,-1,4,5,6]
for i in count:
    print(i)
    if i==4:
        break
    i+= 1'''
#OR
'''a=0
Tuple=(1,2,-1,9,10,-14,11,66,'Hello','e',1.23)
while a<len(Tuple):
    print(Tuple[a])
    if 10 == Tuple[a]:
        break
    a+=1'''
#Contuinue:-
a=0
while a<5:
    print(a)
    a+=1
    if(a==3):
        continue
    print("Hello")
#OR
for i in range(1,11):
    if i==6:
        continue
    print(i)


