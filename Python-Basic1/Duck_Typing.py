#THIS PROGRAM IS HOW DUCK TYPING(Dynamically Typing) IS WORK...
class Duck:
    def Swim(self):
        print('I can Swim ,I am Duck')
    def Sound(self):
        print('Quck Quck')
class Dog:
    def Swim(self):
        print('I can Swim, I am Dog')
    def Sound(self):
        print('Bark Bark')
def Display(obj):
    obj.Swim()
    obj.Sound()
'''duck=Duck()
Display(duck)'''
#OR
dog=Dog()
Display(dog)