#This program is print multiple colorful circle or dots on screen...
import turtle,random
pen1=turtle.Turtle()
turtle.bgcolor("Black")
turtle.colormode(255)
pen1.speed(0)
for i in range(200):
    x = random.randrange(-1000, 1000)
    y = random.randrange(-1000, 1000)
    pen1.pendown()
    r = random.randrange(0,255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    pen1.fillcolor(r,g,b)
    pen1.begin_fill()
    pen1.circle(20)
    pen1.end_fill()
    pen1.penup()
    pen1.goto(x,y)

pen1.screen.mainloop()