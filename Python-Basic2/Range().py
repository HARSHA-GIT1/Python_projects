#THIS PROGRAM SHOW THE WORKING OF RANGE FUNCTION....
'''for i in range(5):
    print(i)

a=range(10)
for i in a:
    print(i)

for i in range(0,5):
    print(i)

for i in range(0,10,3):
    print(i)

for i in range(0,5,-1):
    print(i)

for i in range(5,0,-1):
    print(i)'''
#THIS IS FOUND THE SUM OF 1 to 100
sum=0
for i in range(1,101):
    sum+=i
print('Sum of 100 No is: ',sum)
#THIS IS FOUND THE SUM OF EVEN NO
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
        print(i)
print('Sum of Even no Between 1 to 100 is: ',sum)