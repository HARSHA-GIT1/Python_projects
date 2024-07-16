#THIS IS A SIMPLE PROGRAM FOR A RIDE TICKET....
Age=int(input('Enter Your Age: '))
if(Age>=3 and Age<35):
    print('You can Ride')
    if(Age<12):
        print('Your Ticket price is 150 Rupees')
        Bill=150
    elif(Age<18):
        print('Your Ticket price is 250 Rupees')
        Bill=250
    elif(Age>=18):
        print('Your Ticket price is 400 Rupees')
        Bill=400
    print(" Can you want to take a horror ride if Yes you give 100 Rupees more for Enjoying with Horror")
    Choice=input('Press Y or N')
    if(Choice=='y' or Choice=="Y"):
        Bill=Bill+100
    else:
        print('Thanks')
else:
    print('You are not eligbly for Ride')
