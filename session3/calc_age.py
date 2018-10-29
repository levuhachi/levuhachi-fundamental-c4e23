yob_str=input("Sinh nam? ")
#if not yob_str.isdigit():
#    print("Not ok")
#    yob_str=input("Sinh nam?")

while not yob_str.isdigit():
    print("Not ok")
    yob_str=input("Sinh nam?")
yob = int(yob_str)
age = 2018 - yob
print (age)
