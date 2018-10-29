s = input("enter a text: ")
if (not s.isdigit()) and (not s.islower()) and (not s.isupper()):
    print ("Contains both")
else:
    print ("Not Ok")


##s.islower -- all factors inside s are LOWER CASE