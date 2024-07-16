#This is a simple excercise based on Matrix problem...
list1=[0 ,0 ,0]
list2=[0 ,0 ,0]
list3=[0 ,0 ,0]
print('Matrix Before Input: ')
print(list1)
print(list2)
print(list3)
row=int(input("Enter The Row Position: "))
col=int(input('Enter The Coloumn Position: '))
if row==1:
    list1[col-1]='x'
elif row==2:
    list2[col-1]='x'
else:
    list3[col-1]='x'
print('Now Matrix Value is:')
print(list1)
print(list2)
print(list3)