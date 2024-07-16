#THIS PROGRAM IS SHOWING THE WORKING OF IRETRATORS...
#CASE-1(Without Iretrator)
List1=[1,5,0,2,9,5,3,8]
#for i in List1:
    #print(i)
'''
#CASE-2(Iretrator)
it =iter(List1)
print(it.__next__())
#OR
print(next(it))
'''
#CASE-3(FOR Loop With Iretrator)
it =iter(List1)
val=len(List1)
for i in range(val):
    print(next(it))