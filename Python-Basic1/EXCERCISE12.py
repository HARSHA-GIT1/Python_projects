#THIS PROGRAM IS SHOW DAYS IN A MONTH....
Dict={'January':31,'Febuaray':28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}
def Check_Leap(Data):
    if Data%4==0:
        if Data%100==0:
            if Data%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def check(year,month):
    if Check_Leap(year):
        Dict["Febuaray"]=29
        return Dict[month]
    else:
        return Dict[month]
#Start...
Year=int(input('Enter The Year:-'))
Month=input("Enter The Month:-")
result=check(Year,Month.title())
print(Month,"Have",result,"Days")