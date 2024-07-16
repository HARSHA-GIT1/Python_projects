#THIS PROGRAM IS SHOWING THE WORKING OF EVENT LISITNERS...
#EVENT-LISITNERS= Control The Turtle According to key(UP, DOWN, LEFT, RIGHT).
import turtle
pen1=turtle.Turtle()
scr1=turtle.Screen()
pen1.speed(0)
def up():
    pen1.setheading(90)#pen1.lt(90)
    #pen1.forward(5)
def down():
    pen1.setheading(270)#pen1.lt(90)
    #pen1.forward(5)
def right():
    pen1.setheading(0)#pen1.lt(90)
    #pen1.forward(5)
def left():
    pen1.setheading(180)#pen1.lt(90)
    #pen1.forward(5)
def clear():
    pen1.clear()
    pen1.penup()
    pen1.home()
    pen1.pendown()
def space():
    pen1.forward(10)
scr1.listen()#Use for getting the focus of Screen...
scr1.onkey(fun=up,key="Up")
scr1.onkey(fun=down,key="Down")
scr1.onkey(fun=left,key="Left")
scr1.onkey(fun=right,key="Right")
scr1.onkey(fun=clear,key="c")
scr1.onkey(fun=space,key="f")
scr1.exitonclick()