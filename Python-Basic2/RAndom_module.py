#THIS PROGRAM SHOW THE WORKING OF RANDOM MODULE...
import random
a=random.randint(1,5)#it return a value as a<=X<=b
print(a)
b=random.randrange(1,5)#it return a value as a<=X<b
print(b)
print(random.random())#it give the random value between 0.0 and 1.0 in float
c=random.uniform(1,6)#it return a value in float as a<=X<b
print(c)
no=[1,-0,1,4,-1,-9,5,60]
d=random.choice(no)
print(d)
random.shuffle(no)
print(no)