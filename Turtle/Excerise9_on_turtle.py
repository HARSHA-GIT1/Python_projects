#THIS PROGRAM IS PRINT A CIRCLE CHAI
import turtle,random
turtle.bgcolor("Black")
pen1=turtle.Turtle()
pen1.pensize(3)
pen1.speed(0)
pen1.screen.colormode(255)
for i in range(100):
    r=random.randrange(0,255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    pen1.pencolor(r,g,b)
    pen1.circle(200)
    pen1.lt(5)
    pen1.circle(200)
    if pen1.heading()==0.0:
        break
pen1.screen.mainloop()