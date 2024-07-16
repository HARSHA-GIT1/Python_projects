#THIS PROGRAM IS SHOWING THE WORKING OF NESTED DICT(MULTIPLE ALSO) AND LIST...
data_dict={
    'Harsh':'Men',
    'Animal':{
        'Tiger':'Dangerous',
        'Cow':'Sweet and Simple'
    },
    'Birds':{
        'Seasonal':{
                    'Bluethroat':'Medium',
                    'Greater':'Large',
                    'Northern':'Small'
                    },
        'Regional':{
            'Asian Koel':'Sweet',
            'Green Imperial pigeon':'Silent',
            'Asian Emerald Cuckoo':'Dangerous'
        }
    },
    'cars':['Gt Mustang','BMW-Z Series','Phantom','Doge','Alto-800(Customized)']
}
for i in data_dict:
    print(i, data_dict[i])
print(data_dict['Animal'])
print(data_dict['Animal']['Tiger'])
print(data_dict['cars'])
print(data_dict['Birds']['Seasonal'])
print(data_dict.get('cars'))
#You can also Pass dictionaries in list..
List=[
    {'Phone':9082323323,'Age':19,'Address':'Khirwa'},
    {'Phone':8922323883,'Age':20,'Address':'Banbasa'}
]
print(List)
print(List[0])
print(List[1])
print(List[0]['Phone'])