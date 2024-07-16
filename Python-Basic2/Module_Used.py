#THIS PROGRAM IS SHOWING THE WORKING OF PREDIFINE AND USERDEFINE(MODULE_DATA) WORKING...
'''import math,random
#print(help('random'))
#OR
print(help('math'))
'''
#User Define
'''import Module_Data
print(Module_Data.Sum(3,4))'''
#Or
#from Module_Data import *
#Or
#YOU CAN ALSO IMPORT A PARTICULAR METHOD FROM A MODULE
'''
from Module_Data import Sum
#print(Multiple(2,3))
a=2
print(a)
#print(Module_Data.a)#Here I get Error But When Go to Case-2
print(Sum(2,3))
'''
#Case -2
import Module_Data
#print(Multiple(2,3))
a=2
print(a)
print(Module_Data.a)
print(Module_Data.Sum(2,3))
