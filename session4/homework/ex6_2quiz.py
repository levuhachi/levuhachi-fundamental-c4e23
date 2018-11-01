# Set up "Score"
score  = 0

# Quiz 1
print ("If x = 8, then what is the value of 4(x+3)?")
ans1 = [35,36,40,44]

for index, answer1 in enumerate (ans1):
    print(index+1,answer1, sep = '.')

user_ans1 = input("Your choice is: ")

if user_ans1 == "4" or user_ans1 == "44" or user_ans1 == "4.44" or user_ans1 == "4. 44":
    print ("Bingo!")
    score = score + 1
else: 
    print (":(")

#Quiz 2

print("Estimate this answer (exact calculation not needed")
print("Jack scored these marks in 5 math tests: 49,81,72,66 and 52. What is the mean?")
ans2 = [55, 65, 75, 85]

for index, answer2 in enumerate (ans2):
    print(index+1,". About", answer2)

user_ans2 = input ("Your choice is: ")

if user_ans2 == "2" or user_ans2 == "About 65" or user_ans2 == "about 65" or user_ans2 == "2.About 65" or user_ans2== "2 . About 65":
    print("Bingo!")
    score = score + 1
else:
    print(":(")

#Final Result
print ("You correctly answer", score, "out of 2")


    
