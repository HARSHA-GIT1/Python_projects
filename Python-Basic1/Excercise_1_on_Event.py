#THIS IS AN EXCERCISE ON EVENT LISTINERS...
import turtle
pen1=turtle.Turtle()
scr1=turtle.Screen()

def forward():
    pen1.forward(10)

def backward():
    pen1.backward(10)

def left():
    pen1.setheading(pen1.heading()+20)

def right():
    pen1.setheading(pen1.heading()+20)

def clear():
    pen1.penup()
    pen1.clear()
    pen1.home()
    pen1.pendown()
scr1.listen()
scr1.onkey(fun=forward,key="f")
scr1.onkey(fun=backward,key="b")
scr1.onkey(fun=left,key="l")
scr1.onkey(fun=right,key="r")
scr1.exitonclick()