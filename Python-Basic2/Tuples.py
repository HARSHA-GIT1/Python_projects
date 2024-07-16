#THIS PROGRAM SHOWINFG THE WORKING OF TUPLES AND ITS FUNCTIONS..
tuple1=(10,1,0,9,8,1,3,1)
tuple2=(1.2,3.22,1.45,2.90,3.3456,4.333)
tuple3=('Pasie','Nahi','Ha','Chura','Lo')
tuple4=(10)
tuple5=(10,)
tuple6=(10,)*5
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)
print(tuple6)
#Tuple Functions
print(type(tuple4))
print(type(tuple5))
print(len(tuple1))
print(tuple1.count(1))
print(tuple2.index(3.22))
print(tuple3.index('Ha'))
print(tuple1[0])
print(tuple2[-3])
print(tuple1[0:4])
print(tuple1[0::6])
list=[9,0,4,5,6]
print(tuple(list))#CHANGE THE LIST INTO TUPLES
print(max(tuple1))
print(min(tuple1))
import sys
print(sys.getsizeof(tuple1))
print(sys.getsizeof(tuple4))
print(sys.getsizeof(tuple5))
#TUPLES IS IMMUTABLE
#print(tuple1)
