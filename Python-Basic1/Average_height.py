#THIS PROGRAM SHOW THE WORKING OF FIND AVERAGE HEIGHT...
'''Data=input('Enter The Heights in Cm(At Single Time Enter Only 5): ')
List=Data.split()
Sum =0
for i in List:
    Sum = Sum + int(i)
Average=Sum//5
print(f'Average Height is :{round(Average)}')'''

Data=input('Enter The Heights in Cm With Seprate Space: ')
List=Data.split()
count,Sum=0,0
for i in List:
    count=count+1
for i in range(count):
    Sum += int(List[i])
Average=Sum/count
print(f'Average Height is :{round(Average)}')

'''Data=input('Enter The Heights in Cm: ')
List=Data.split()
Sum =0
for i in List:
    Sum = Sum + int(i)
Average=Sum/len(List)
print(f'Average Height is :{round(Average)}')'''