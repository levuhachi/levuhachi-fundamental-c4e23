n = int(input("n= "))
for i in range(n+1):
    if i % 2 == 0:
        print("x", end = " ")
    else:
        print("*", end = " ")
print()