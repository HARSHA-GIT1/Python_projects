#Basically this program is showing the Working of __name__ variable and if __name__=='__main__'.
#(i) In Python __name__ variable Work for __main__.
#Example:-
print(__name__)
#(ii) In Python __name__ return __main__ if we execute Directly the file.
#(iii) But if  Use This file using import into another file then here __name__ return Name_of_the_file(Who import).
#(iv) So As We See in if __name__=='__main__' ,we use it for restriction or protected the important data.
#Example
'''#Case-1
print('Come From Module Demo_name')
def display(name):
    print(name)
def do():
    print('Hello')
Name=input('Enter your Name:-')
display(Name)
do()
'''
#Case-2
print('Come From Module Demo_name')
def display(name):
    print(name)
def do():
    print('Hello')
if __name__=='__main__':
    Name=input('Enter your Name:-')
    display(Name)
    do()
