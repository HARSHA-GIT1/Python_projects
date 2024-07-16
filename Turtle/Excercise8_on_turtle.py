#THIS PROGRAM IS BASICALLY HOW PRINT A STAR CIRCLE
import turtle
turtle.bgcolor("Black")
turtle.shape("triangle")
turtle.screensize(3000,4000)
pen1=turtle.Turtle()
pen1.pensize(3)
pen1.color("red")
pen1.fillcolor("Yellow")
pen1.speed(0)
pen1.goto(-450,0)
pen1.begin_fill()

for i in range(200):
    pen1.forward(900)
    pen1.lt(170)
    if pen1.heading()==0.0:
        break
pen1.end_fill()
pen1.screen.mainloop()