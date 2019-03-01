import turtle

# create turtle
t = turtle.Turtle()

t.begin_fill()
t.pensize(10)
# set colors
colors = ['red', 'blue']

for j in range(8):
    t.color(colors[j % 2])
    for i in range(18):
        t.forward(25)
        t.left(20)
    t.right(45)

t.end_fill()

turtle.mainloop()
