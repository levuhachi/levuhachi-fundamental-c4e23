from turtle import*
shape("turtle")
for i in range (1,5):
    a = i+2 
    for j in range(a):
        if a % 2 ==0: 
            color("red")
        else: 
            color("blue")
        b = 180 - (180*i)/(i+2)
        forward(100)
        left(b)
mainloop()