# This is not used anywhere?
price_of_pkg = int(input("Please enter the price of the package you would like to send "))

dist = int(input("How far, in Km, would you like to send the package? "))

# All of these loops ensure a valid input. They keep running until the conditional is true
# We convert all input to uppercase so that any lowercase inputs are also accepted
while True :
    transport_type = input("Would you like to send by air (£0.36km) or freight (£0.25km)? Select with A or F ")
    if transport_type.upper() == 'A' :
        transport_type = 0.36
        break
    elif transport_type.upper() == 'F' :
        transport_type = 0.25
        break

while True :
    insurance = input("Would you like full insurance at £50 or limited insurance at £25? Select with F or L ")
    if insurance.upper() == 'F' :
        insurance = 50
        break
    elif insurance.upper() == 'L' :
        insurance = 25
        break

while True :
    gift = input("Would you like to gift wrap it for £15? Select with Y or N ")
    if gift.upper() == 'Y' :
        gift = 15
        break
    else :
        gift = 0
        break

while True :
    priority = input("Would you like priority delivery at £100 or standard delivery at £20? Select with P or S ")
    if priority.upper() == 'P' :
        priority = 100
        break
    elif priority.upper() == 'S' :
        priority = 20
        break

# Calculate total price
total_price = dist * int(transport_type) + int(insurance) + int(gift) + int(priority)

print(total_price)