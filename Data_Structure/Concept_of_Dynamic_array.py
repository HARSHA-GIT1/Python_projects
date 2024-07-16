#This Program is Showing The Working of Dynamically Array-concept...

#CASE-1:-
"""import sys
List=[]
print(sys.getsizeof(List))
List.append(12)
print(sys.getsizeof(List))
List.append(1)
print(sys.getsizeof(List))
List.append("Harsh")
print(sys.getsizeof(List))
List.append(1.23)
print(sys.getsizeof(List))
List.append("Sohan")
print(sys.getsizeof(List))
"""

#CASE-2:-
import sys
List=[]
print(sys.getsizeof(List))
for i in range(10):
    List.append(i)
    print(List[i],sys.getsizeof(List))
