#THIS PROGRAM IS SHOWING THE WORKING OF SETS AND ITS FUNCTIONS..
'''set1={10,2,3,4,5,-1,0}
set2={1,'Hello','f',1.23345}
set3={1}
set4=set({'Set','Ko','Samajna','Aasan','Ha'})
print(set1)
print(set2)
print(set3)
print(set4)
#SETS FUNCTIONS AND ITS PROPERTIES...
#print(set1[0])#Sets is not Support indexing due to inorder...
set5={10,10,10,10,10}#Duplicate Value is not allow...
set6={1,2,1,3,1,4}
set7={1,2,3,4,2}
set8={}
set9=set({})
print(set5)
print(set6)
print(set7)
print(type(set7))
print(type(set8))
print(type(set9))
#set5[0]=1#Sets are immutable...
print(set5)
set5={1,2,3,4,5,6,7,8,9,10,11,12,13}
#set5={1,0,3,4,-1,6,7,8,9,10,11,12,13,22}
#set5={1,-1,3}#But You can change the whole set...
print(set5)
set5.add(14)
print(set5)
print(len(set5),'is length')
set5.remove(2)
print(set5)
set6.pop()#pop() delete
print(set6)
set7.clear()
print(set7)
set1.discard(-1)
print(set1)'''
#SET OPERATIONS
#Union
set10=set({-1,2,8,3,0,4})
set11=set({52,70,6})
print(set10.union(set11))
print(set11.union(set10))
print(set11.union(('hello','Namaste')))
#OR
print(set10|set11)
print(set10|{'hello','Namaste'})
#print(set10|("jai ho"))#Give Error..
#Update
set12={'hello','jai hind','Ram Ram'}
set13={'kamcho','Bonjo','Namaste'}
set12.update(set13)#Because it not return any value like sort and it is use to update a set..
print(set12)
#Intersection
set14={'harsh','vardhan',"Gupta"}
set15={'Harsh','Vardhan','Gupta'}
print(set14.intersection(set15))
print(set14 & set15)
print(set14.intersection(['gupta']))
#print(set14 & ['Gupta'])
set14.intersection_update(set15)
print(set14)
#Difference
set16={'Harsh','Ram','Jiya','Sohan','Kunal'}
set17={'Sohan','Ram','Harsh','Rahul','Anshika'}
set18={'Bass ','500','me'}
print(set16.difference(set17,set18))
print(set17.difference(set16,set18))
print(set16 - set17-set18)
print(set17 - set16-set18)
#Symetric_difference
print(set16.symmetric_difference(set17))
print(set17.symmetric_difference(set18))
#print(set16.symmetric_difference(set17,set18))#Error
print(set16 ^ set17 ^ set18)
#Update
set16.difference_update(set17)
print(set16)
set16.symmetric_difference_update(set17)
print(set16)
#Other Operations
set19={1,2,3,4,-1,90,111,23,-12,0}
set20={1,3,-1,111,0}
print(set19.isdisjoint(set20))
print(set20.isdisjoint(set19))
print(set20.issubset(set19))
print(set19.issubset(set20))
print(set19 <= set20)
print(set20 <= set19)
print(set19 >= set20)
print(set20 >= set19)
set19.pop()
print(set19)
#del set19
#print(set19)