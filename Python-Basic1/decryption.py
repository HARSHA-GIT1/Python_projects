#THIS PROGRAM IS SHOWING THE WORKING OF DECRYPTION....
List_of_code=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def Decript():
    data=input('Enter The Data:')
    Shift=int(input('Please Enter The Shift No:'))
    data_string = ""
    for i in data:
        if i in List_of_code:
            no=(List_of_code.index(i)-Shift)%26
            data_string+=List_of_code[no]
        else:
            data_string+=i
    print('Your Decript Data is:',data_string)
condition=True
while condition:
    Choice=input('Type `Shyam Wahi` For Decrpytion: ')
    Choice_Lower=Choice.lower()
    if Choice_Lower=='shyam wahi':
        Decript()
    else:
        print('Please Type Correct Code')
    Choice1=int(input('Do You Want To Continue This Press 1 And For Exit Press 0: '))
    if Choice1==1:
        condition=True
    else:
        condition=False