import turtle
pen1=turtle.Turtle()
for i in range(3,9):
    angle=360/i
for _ in range(i):
    pen1.forward(100)
    pen1.rt(angle)
pen1.screen.mainloop()