def hotel_cost(num_nights) :
    return num_nights * 100

def plane_cost(flying_to) :
    if flying_to.lower() == "spain" :
        return 100
    if flying_to.lower() == "japan" :
        return 1000
    if flying_to.lower() == "canada" :
        return 500
    if flying_to.lower() == "russia" :
        return 100000
    if flying_to.lower() == "scotland" :
        return 200
    else :
        return 0

def car_rental(num_of_days) :
    return num_of_days * 50

def holiday_cost(num_nights, flying_to, num_of_days) :
    total_cost = hotel_cost(num_nights) + plane_cost(flying_to) + car_rental(num_of_days)

    print(f"You will be flying to {flying_to} at a cost of £{plane_cost(flying_to)}")
    print(f"You will be staying in the grand deluxe hotel for a total of {num_nights} night, costing {hotel_cost(num_nights)}")
    print(f"You will be renting a nissan micra for {num_of_days} days, costing {car_rental(num_of_days)}")
    print(f"The total cost for this luxurious holiday is £{total_cost}")

# Ask the user to enter some information about the holiday they want
# Enter a loop to ensure the users enters valid data
# Use a try catch to cast numbers to integers
# Use an if statement to check if the destination is valid
print("Where would you like to fly to?")
while True :
    flying_to = input()
    if flying_to.lower() == "spain" or flying_to.lower() == "japan" or flying_to.lower() == "canada" or flying_to.lower() == "russia" or flying_to.lower() == "scotland" :
        print("How many nights would you like to stay at the grand deluxe hotel?")
        while True :
            num_nights = input()
            try :
                int(num_nights)
                break
            except :
                print("Invalid input, please enter a number")
        print("How many days do you need car hire for?")
        while True :
            num_of_days = input()
            try :
                int(num_of_days)
                break
            except :
                print("Invalid input, please enter a number")
        break
    else :
        print("Sorry, we only fly to Spain, Japan, Canada, Russia and Scotland")

holiday_cost(int(num_nights), flying_to, int(num_of_days))