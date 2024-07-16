Year=int(input('Enter the year: '))
if Year%4==0:
    if Year%100==0:
        if Year%400==0:
            print('Given Year is Leap Year')
        else:
            print('Given Year is not a Leap Year')
    else:
        print('Given Year is  a Leap Year')
else:
    print('Given Year is not a Leap Year')