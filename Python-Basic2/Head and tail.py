#THIS PROGRAM SHOWING THE WORKING OF A GAME OR VIRTUAL HEAD AND TAILS....
import random
data=input('Enter your choice')
result=random.randrange(0,4)
if result==1:
    print('Head comes')
    print('Congratulations you won the toss')
else:
    print('Tail comes')
    print('Sorry better lucky next timesss')
