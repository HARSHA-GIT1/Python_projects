#THIS PROGRAM IS SHOWING THE WORKING OF FILTER,MAP AND REDUCE...
#FILTER:-You can able to filter the data in list using Filter().
#MAP:-You can change the value(Like +,-,*,and //) using Map().
#REDUCE:-You get the sum of list using Reduce().
#Synatx:-Function(Variable,iltrable).
from functools import reduce
#CASE-1:-(FILTER-FUNCTION)
List=[2,4,3,6,7,10,0,5]
Even=(filter(lambda a:a%2!=0,List))#Getting odd No...
print(Even)

#CASE-2:-(MAP-FUNCTION)
Modify=list(map(lambda a: a*2,List))
#Modify=list(filter(lambda a:a*2==0,List))
print(Modify)

#CASE-3:-(REDUCE-FUNCTION)
Sum=reduce(lambda n,m :m+n,List)
Sum1=reduce(lambda n,m :m+n,Modify)
print(Sum)
print(Sum1)