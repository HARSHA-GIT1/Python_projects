#THIS PROGRAM IS SHOWING THE WORKING OF HOW TO ENCRPYTION .....
import random
List_of_code=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encript():
    data=input('Enter Your data(Only String Type):')
    shift=random.randrange(1,11)#Give Random No for Shift
    data_string = ""
    for i in data:#Start a Loop For Gathered Data from Input
        if i in List_of_code:
            no=(List_of_code.index(i)+shift)%26#Formula=(indexofdata-shift)%26.
            #print(no,List_of_code.index(data[i]))#For Get How Shifting Work.
            data_string +=List_of_code[no]
        else:
            data_string+=i
    print('Your Encript Data Is',data_string,' And It Come From Shift No ',shift)
condition=True
while condition:
    Choice=input('Type `cyphering` For Encrpytion: ')
    Choice_Lower=Choice.lower()
    if Choice_Lower=='cyphering':
        encript()
    else:
        print('Please Type Correct Code')
    Choice1=int(input('Do You Want To Continue This Press 1 And For Exit Press 0: '))
    if Choice1==1:
        condition=True
    else:
        condition=False