#This Program Is an Example Of Showing How Methods Works..
class Name:
    Following=0
    List1=[]
    List2=[]
    Follower=0
    def following(self,name):
        self.Following+=1
        self.List1.append(name)
    def follower(self,name):
        self.Follower+=1
        self.List2.append(name)
Payal=Name()
Payal.follower('Akash')
Rahul=Name()
Rahul.following('Kushi')
Payal.following('Jatin')
print(Payal.Follower,Rahul.Following,Payal.Following)
print(Payal.List2,Rahul.List1)#There is List Working For Both objects at Same memory.
