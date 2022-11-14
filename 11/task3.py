print("Enter how many minutes it took to complete the swimming")

# Loop until correct input is received
while True :
    swim_time = input()
    try :
        float(swim_time)
        swim_time = float(swim_time)
        break
    except :
        print("Invalid input, please try again")

print("Enter how many minutes it took to complete the cycling")
while True :
    cycling_time = input()
    try :
        float(cycling_time)
        cycling_time = float(cycling_time)
        break
    except :
        print("Invalid input, please try again")

print("Enter how many minutes it took to complete the running")
while True :
    running_time = input()
    try :
        float(running_time)
        running_time = float(running_time)
        break
    except :
        print("Invalid input, please try again")

# Add all the times together
total_time = swim_time + cycling_time + running_time

# Check the total time against the table and print the award
if total_time <= 100 :
    print("You won the provincial colors!")
elif total_time > 100 and total_time <= 105 :
    print("You won the provincial half colors!")
elif total_time > 105 and total_time <= 110 :
    print("You won the provincial scroll!")
else :
    print("Sorry, you didn't win an award")