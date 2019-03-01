import turtle

t = turtle.Turtle()

for j in range(8):
    for i in range(18):
        t.forward(20)
        t.left(20)
    t.right(45)

turtle.mainloop()
