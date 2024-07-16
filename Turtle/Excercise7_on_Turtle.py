import turtle,random
turtle.bgcolor("Black")
turtle.shape("turtle")
pen1=turtle.Turtle()
Colour=["red","Blue","Green","Yellow","White","Pink","Brown","Blue4"]
Angle=[90,40,34,67,89,120,32,55,33,78,99,110,21,25,29]
Goto_X=[20,55,66,76,33,42,33,98]
Goto_Y=[30,40,50,70,80,74,33,20]
for i in range(200):
    pen1.speed(3)
    pen1.hideturtle()
    pen1.pendown()
    pen1.pensize(10)
    pen1.color(random.choice(Colour))
    pen1.forward(150)
    pen1.goto(random.choice(Goto_X),random.choice(Goto_Y))
    if i%2==0:
        pen1.lt(random.choice(Angle))
    else:
        pen1.rt(random.choice(Angle))
    pen1.up()
    pen1.showturtle()
pen1.screen.mainloop()