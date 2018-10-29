print ("Hi there, this is a superuser gateaway")
user_name = input("User name: ")
if user_name != "c4e":
    print ("You are not superuser")
else:
    pw = input ("Password: ")
    if pw != "codethechange":
        print ("Password is incorrect")
    else:
        print ("Welcome, c4e")

    