from turtle import * 

shape("turtle")
color("red")
pensize(5)
left(30)
forward(100)
for i in range(4):
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)
    left(150)
    if i in range(3):
        forward(100)



mainloop()

