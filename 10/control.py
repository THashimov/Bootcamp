print("Please enter your age")

while True :
    age = input()
    try : 
        int(age)
        age = int(age)
        break
    except :
        print("Invalid input, please try again")

if age >= 18 :
    print("You are old enough")
elif age > 16 and age < 18 :
    print("Almost there!")
else :
    print("Sorry, you are too young")
