import turtle

# create turtle
t = turtle.Turtle()

t.shape('turtle')
t.shapesize(5, 5, 5)

t.begin_fill()
t.pensize(10)
# set colors
colors = ['red','yellow']
t.begin_fill()

for j in range(8):

    t.color(colors[j % 2])
    for i in range(18):
<<<<<<< HEAD
        t.forward(25)
        t.left(20)
    t.right(45)

t.end_fill()
colors = ['green']
=======
        t.forward(20)
        t.left(20)
    t.right(45)


t.pensize(0)
t.forward(50)
t.right(90)
t.forward(20)
t.left(90)

t.pensize(10)

colors = ['darkgreen']
t.begin_fill()
>>>>>>> 880c066e1df2ae4239483135d2892a0ee7c33297
t.color(colors[0])
t.left(90)
for i in range(9):
    t.forward(25)
    t.left(20)
t.forward(25)
t.left(90)
t.forward(180)

t.left(90)
for i in range(9):
    t.forward(7)
    t.left(20)
t.forward(6)
for i in range(9):
    t.forward(3)
    t.right(20)
t.left(90)
t.forward(100)
t.left(90)
for i in range(9):
    t.forward(3)
    t.right(20)
t.forward(6)
t.end_fill()
turtle.mainloop()
