#THIS PROGRAM FOR SHOWING THE WORKING OF LOVE CALCULATOR....ga
Name1=input('Enter the First name:')
Name2=input('Enter the Second name:')
Name3=Name1.lower()+Name2.lower()
no=Name3.count('t')+Name3.count('r')+Name3.count('u')+Name3.count('e')
no2=Name3.count("l")+Name3.count('o')+Name3.count('v')+Name3.count('e')
love_score=int(str(no)+str(no2))
if(love_score>=10 and love_score<=90):
    if(love_score<30):
        print(f'Your love score is: {love_score}% with Meduim love Bond ')
    elif(love_score>=30 and love_score<=60):
        print(f'Your love score is: {love_score}% with Golden love Bond')
        print(f'Bhai esi Baat pe party de')
    elif(love_score>=60 and love_score<=80):
        print(f'Your love Score is {love_score}% with Diamond love Bond')
        print("Apna ko chaiye Bhokal wali dawat bhai")
    elif(love_score<=90):
        print(f'Your love score is: {love_score}% with Maza and Moye Moye Bond')
        print('Bhai BIll pay kar diyo')
else:
    print("BA ja gareeb pad le en kammo me na ha kuch")