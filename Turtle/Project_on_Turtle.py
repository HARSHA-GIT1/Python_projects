#{WELCOME TO THIS PROJECT}
#THIS PROJECT IS BASED ON RACE ON TURTLE
import turtle,random
def Race(list):
    condition=True
    while condition:
        for i in list:
            distance=random.randrange(1,20)
            turtle.forward(distance)
            x,y=turtle.pos()
            if y>=800//2:
                print("The Winner is",i.color())
            condition=False
def Make_Turtle(no):
    s1=turtle.Screen()
    s1.setup(width=800,height=800)
    s1.colormode(255)
    x_space=400//no+1
    List_of_turtle=[]
    for i in range(no):
        r = random.randrange(0, 255)#FOR PEN COLOUR
        g = random.randrange(0, 255)
        b = random.randrange(0, 255)
        new_turtle=turtle.Turtle()
        new_turtle.penup()
        new_turtle.shape("turtle")
        new_turtle.pencolor(r,g,b)
        new_turtle.lt(90)
        new_turtle.forward(100)
        new_turtle.goto(-800//2+(i*x_space),-800//2)
        List_of_turtle.append(new_turtle)
        Race(List_of_turtle)
    s1.exitonclick()
def Turtle_main():
    print("Welcome To Turtle Race")
    no_of_turtles=int(input("Enter The No's Of Turtles:-"))
    if 2<=no_of_turtles<=10:
       Make_Turtle(no_of_turtles)
       exit()
    else:
         print("You Have Only Entered The No Between (2,10)")
Condition=True
while Condition:
    Turtle_main()