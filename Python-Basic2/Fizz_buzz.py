#THIS PROGRAM SHOW THE WORKING OF FIZZ-BUZZ JOB INTERVIEW QUESTION...
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print('fizz-Buzz')
    elif(i%3==0):
        print('Fizz')
    elif(i%5==0):
        print('Buzz')
    else:
        print(i)