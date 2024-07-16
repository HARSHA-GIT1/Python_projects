#THIS PROGRAM IS SHOWING THE WORKING OF HIGH_ORDER FUNCTIONS...
#HIGH_ORDER-FUNCTIONS:-[The Functions Which Take And Return A Function
#As a Parameter.]
#case-1
def add(a,b):
    return a+b
print(add(2,3))
print(add)
#OR
Addition=add#Because in python all things considered as object.
print(Addition(2,3))
print(Addition)

#case-2
'''def sound(parameter):
    print("This Sound Be Like",parameter)
def display(other_def_func,parameter):
    print("Comes from Display")
    #other_def_func(parameter)
    return sound()
display(sound,"Sweet")'''
#Case-3
def say1():
    print("Ram Ram")
def say2():
    print("Jai Shri Ram")
def display():
    return say1()
display()