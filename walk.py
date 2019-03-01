import turtle

# create turtle
t = turtle.Turtle()

# set colors
colors = ['green']
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
turtle.mainloop()
