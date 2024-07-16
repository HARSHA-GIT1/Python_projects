#THIS PROGRAM IS SHOWING THE WORKING OF DICT IN LIST....
Data=[
    {
        'Name':'Mohan',
        'Phone':9886744521,
        'Age':16,
        'Course':'C'
    },
    {
        'Name': 'Sohan',
        'Phone': 819104452,
        'Age': 19,
        'Course': 'C++'
    }
]
def AddNewData(**Data_dic):
    Data.append(Data_dic)
    print(Data[0])
    print(Data[1])
    print(Data[2])
#Start
AddNewData(Name='Harsh',Phone=9058387773,Age=20,Course='Java')