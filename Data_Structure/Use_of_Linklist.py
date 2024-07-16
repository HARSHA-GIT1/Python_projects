#THIS PROGRAM IS SHOWING THE WORKING OF LINKLIST...
import Making_a_linklist,sys

L=Making_a_linklist.Linklist()
print(len(L))
print(sys.getsizeof(L))
L.insert_head(2)
L.insert_head(4)
L.insert_head(5)
L.insert_head(6)
print(len(L))
print(sys.getsizeof(L))

L.insert_head(7)
L.insert_head(8)
L.insert_head(9)
L.insert_head(10)
print(sys.getsizeof(L))
print(L)

L.insert_end(11)
print(L)
L.insert_end(13)
L.insert_end(14)
L.insert_end(15)
L.insert_end(16)
print(L)

L.insert_after(11,12)
print(L)

L.insert_before(2,3)
print(L)
L.insert_before(11,1)
print(L)
print(len(L))

"""L.clear()
print(L)"""

L.delete_from_head()
print(L)

L.delete_from_Tail()
print(L)

L.delete_By_value_after(2)
print(L)

L.delete_By_value_before(11)
print(L)

print(len(L))

L.search_by_value(11)
L.search_by_value(2)
print(L[0])
print(L[100])

del L[2]
print(L)
del L[6]
print(L)
del L[0]
print(L)
del L[8]
print(L)
del L[11]