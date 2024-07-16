def Duplicate(list):
    Data=[]
    get=duplicate=0
    for i in range(len(list)):
        Data.append(list.count(list[i]))

    for i in range(len(Data)):
        if Data[i]>1:
            duplicate+=1
    return duplicate

List=[]
size=int(input('Enter The Size Of Array:-'))
print("Enter The Element Of Array:-")
data=0

for i in range(-1,size):
    data=int(input(""))
    List.append(data)
print("Your Entered Data Is:-")

for i in range(size):
    print(List[i])

result=Duplicate(List)
print("No Of Duplicate No is:-",result)