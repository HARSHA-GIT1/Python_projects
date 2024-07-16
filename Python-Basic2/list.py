#THIS PROGRAM SHOWING THE WORKING OF LISTS AND ITS FUNCTIONS...
#INTRODUCTION
"""listof_int=[1,2,3,4,5]
listof_float=[1.23,134,4.56]
listof_Mix=[1,1.234,'r','hello']
print(listof_int)
print(listof_float)
print(listof_Mix)
#OR
no=[1,2,3,4]
print(no[0])
print(no[1])
print(no[2])
print(no[3])"""
#FUNCTIONS
"""no1=[1,2,3,4]
no2=[1.232,123.34,34.34]
no3=["Heloo",12,1.34,'e']
print(len(no1))
print(type(no1))
print(len(no2))
print(type(no2))
print(len(no3))
print(type(no3))
no4=list([1,2,3])
print(no4)
#NEGATIVE INDEXING
print(no1[0])
print(no1[-1])"""
#RANGE ACCESS
'''no=[1,2,3,4,5,6]
print(no[2:])
print(no[0:4])
print(no[-5:-1])'''
#MAIN FUNCTIONS
'''data=list(['hello','bonjo','namaste','jai shri ram','kamcho'])
no=[1,4,0,-1,9,23,7]
print(no)
no.sort()
print(no)
print(data)
data.reverse()
print(data)
print(no)
no.append(23)
print(no)
no.insert(2,3)
print(no)
no.extend([2,3,4,1.23])
print(no)
data.remove('bonjo')
print(data)
print(no)
print(no.pop())
print(no)
print(no.pop(1))
print(no)
print(no.count(23))
print(no[20])'''
#NESTED LISTS
list=list([1,2,3,[0,7,5],9,-1])
list1=[10]
list2=[10]*5
print(list1)
print(list2)
print(len(list))
print(list)
print(list[3])
print(list[3][0])
print(list[3][0:3])
print(list[3][-1])
print(len(list[3]))
#Find the Size
import sys
print(sys.getsizeof(list))
print(sys.getsizeof(int))
print(max())

