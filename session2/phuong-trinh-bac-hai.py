a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

d = b*b - 4 * a * c
print(d)
if d < 0:
    print ("Vo nghiem")
elif d>0: 
    x1 = (-b+(d**0.5))/(2*a)
    x2 = (-b-(d**0.5))/(2*a)
    print("Co 2 nghiem ",x1,"va",x2)
else:
    x = -b/(2*a)
    print("Co 1 nghiem ",x)

#notes: neu muon xet gia tri bang 0, thi phai co 2 dau bang "==", dau khac "!="