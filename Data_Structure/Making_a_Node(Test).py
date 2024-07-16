#THIS PROGRAM IS SHOWING HOW A NODE WORK AND CREATE...

#Create a node class for creating a particular node :-
class Node:
    def __init__(self,data):
        self.data=data
        self.add = None

a = Node(2)
b = Node(3)
c = Node(4)
d = Node(5)
e = Node(6)
f = Node(6)
g = Node(6)
h = Node(6)
i = Node(6)
j = Node(6)

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))
print(id(g))
print(id(h))
print(id(i))
print(id(j))


print(a.data,a.add)
print(b.data,b.add)
print(c.data,c.add)

a.add =id(b)
b.add =id(c)

print(id(a))
print(a.add)
print(b.add)
#print(c.add)
print(id(d))
print(id(e))
print(id(f))
print(id(g))
print(id(h))
print(id(i))
print(id(j))
