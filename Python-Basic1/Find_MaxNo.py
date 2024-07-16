#THIS PROGRAM SHOW THE WORKING OF FIND MAXIMUM NO FROM A LIST..
'''Data=input('Enter The No`s With Seprate space: ')
List=Data.split()
count=0
for i in List:
    count=count+1
for i in range(count):
    List[i]=int(List[i])
Max=List[0]
for i in List:
    if i >Max:
        Max=i
print(f'Maximum No is: {Max}')'''

'''Data=input('Enter The No`s With Seprate space: ')
List=Data.split()
for i in range(len(List)):
    List[i]=int(List[i])
max=List[0]
#for i in List:
for i in List:
    if i>max:
        max=i
print(f'Maximum no is: {max}')'''

Data=input('Enter the No`s with seprate space: ')
List=Data.split()
for i in List:
    Max=max(List)
print('Max NO is :',Max)