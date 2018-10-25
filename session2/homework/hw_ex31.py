h0 =int(input("height(cm)= "))
m = int(input("weight(kg)= "))
h = h0 / 100
bmi =  m / (h*h)
print ("your BMI is ",bmi)
if bmi < 16:
    print ("You are Severely underweight")
elif 16 <= bmi < 18.5:
    print ("You are Underweight")
elif 18.5 <= bmi <25:
    print("You are Normal")
elif 25 <= bmi <30:
    print("You are Overweight")
else:
    print("You are Obese")
