print("Enter your weight in Kg")

# Loop until the weight is a number
while True :
    weight = input()
    try :
        float(weight)
        weight = float(weight)
        break
    except :
        print("Invalid input, please try again. Please enter only a number")

print("Please enter your heigh in Meters")

# Loop until the weight is a number
while True :
    height = input()
    try :
        float(height)
        height = float(height)
        break
    except :
        print("Invalid input, please try again. Please enter only a number")


bmi = weight / pow(height, 2)

if bmi >= 30 :
    print(f"Your BMI is {bmi} You are obese")
elif bmi >= 25 :
    print(f"Your BMI is {bmi} You are overweight")
elif bmi >= 18.5 :
    print(f"Your BMI is {bmi} You are normal")
else :
    print(f"Your BMI is {bmi} You are underweight")