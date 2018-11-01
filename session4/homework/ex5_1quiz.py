print ("If x = 8, then what is the value of 4(x+3)?")

ans = [35,36,40,44]
for i in range (len(ans)):
    print(i+1,ans[i], sep = '.')

user_ans = input("Your choice is: ")
if user_ans == "4" or user_ans == "44" or user_ans == "4.44" or user_ans == "4. 44":
    print ("Bingo!")
else: 
    print (":(")