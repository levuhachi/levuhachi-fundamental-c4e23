items = ["T-shirt","Sweater"]

grt = input("Welcome to our shop, what do you want (C, R, U, D)? ")

while True:
    
    if grt == "r" or grt == "R":
        print("Our items: ", end = ' ')
        print(*items, sep = ', ')
        grt = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    
    elif grt == "c" or grt == "C":
        new_item = input("Enter new item: ")
        items.append(new_item)
        print ("Our new items: ", end = ' ')
        print (*items, sep = ', ')
        grt = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    
    elif grt == "u" or grt == "U":
        ud = int(input ("Update position? (in number): "))
        #while not ud.isdigit():
        #    print ("Please enter a number")
        #    ud = input("Update position? ")
        while ud > len(items):
            ud = input("Update position? (in number): ")
        
        new_item2 = input("Enter new item: ")
        items[ud-1] = new_item2
        print("Our new items: ", end = ' ')
        print(*items, sep = ', ')
        grt = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    
    elif grt == "d" or grt == "D":
        omit = int(input("Delete position?(in number) "))
        while omit > len(items):
            omit = input ("Delete position?(in number) ")
        items.pop(omit-1)
        print ("Our new items: ", end = ' ')
        print (*items, sep = ', ')
    
    else:
        grt = input("Welcome to our shop, what do you want (C, R, U, D)? ")
        break