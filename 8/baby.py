import datetime

current_year = datetime.datetime.now().year

dob = int(input("What year were you born? "))

if current_year - dob >= 18 :
    print("Congrats, you are old enough")
else:
    print("Sorry, you are too young")