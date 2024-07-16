#This Program Is Show The Working Of Global and Local Scope..
#Show the Working Global Keyword..
a=1
def Print():
        global a
        a=a-1
        print(a)
print(a)
Print()
#Show How Global and Local Variable Work...
a=1
print(a)
Print()
def Print():
        b=18
        print(a)
print(b)