#THIS PROGRAM IS SHOWING THE WORKING OF WHILE-LOOP....
count=1
while count<5:
    print("hello")
    count+=1

'''List=[1,2,3,4,5,6]
while List:
    print(List)
    List.pop()'''

List=[1,2,3,4,5,6]
i=0
while i< len(List):
    print(List[i])
    i+=1
#While-else
a=0
List1=['Paise','Nahi','Ha','Chura','Lo']
while a< len(List1):
    print(List1[a])
    #if 'Chura' in List1[a]:
        #break
    a+=1
else:
    print('While Loop Execute Successfuly')
print("Hello")