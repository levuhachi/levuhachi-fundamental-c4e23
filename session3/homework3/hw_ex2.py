print ("Hi there, this is a superuser gateaway")
user_name = input("User name: ")
while True:
    if user_name != "c4e":
        print ("You are not superuser")
        user_name = input("User name: ")
    else:
        pw = input ("Password: ")
        if pw != "codethechange":
            print ("Password is incorrect")
        else:
            print ("Welcome, c4e")
        break
