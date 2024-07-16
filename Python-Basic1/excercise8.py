#This Program is for calculate the no of cans is required for paint the wall....
#Here 1 can = 7 mt^2 area.
import math
def Calculate(a,b,c=7):
    area=a*b
    no=math.ceil(area/c)
    print(no,' is required for paint the wall')
Height=int(input('Enter The Height Of Wall(in mt):'))
Width=int(input('Enter The Width of Wall(in mt):'))
Calculate(Height,Width)