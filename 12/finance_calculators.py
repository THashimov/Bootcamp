import math

# Get the initial value. This works for investments and bonds
def get_initial_val() :
    while True :
        deposit = input()
        try :
            # only return if the value is positive as negative values cannot be handles
            if float(deposit) >= 0 :
                deposit = float(deposit)
                return deposit
            else :
                print("Invalid input. Please try again")
        except :
                print("Invalid input. Please try again")

# Get interest rate
def get_interest_rate() :
    while True :
        interest_rate = input()
        # Check for a % and remove it if there is one
        if interest_rate[len(interest_rate) - 1] == '%' :
                interest_rate = interest_rate[:-1]
        try :
            # Then try to cast the value to a float and check it's less than 100 
            # This will run the exception if we are unable to convert the value to a float
            if float(interest_rate) < 100.0 :
                interest_rate = float(interest_rate) / 100
                return interest_rate
            else :
               print("Invalid input, try again")
        except :
            print("Invalid input, please try again")

# Get time period for investment or bond repayment
def time_period() :
    while True :
        time_period = input()
        try :
            if float(time_period) >= 0 :
                time_period = float(time_period)
                return time_period
            else :
                print("Invalid input. Please try again")
        except :
            print("Invalid input. Please try again")

def amount_in_pot(deposit, interest_rate, years_saving) :
    # Ask user to chose between a simple and compound calculation, repeat until input is valid
    # Once input is valid, print the result 
    while True :
        interest = input()
        if interest.upper() == "S" :
            return float(deposit) * (1 + float(interest_rate) * float(years_saving))
        elif interest.upper() == "C" :
            return float(deposit) * math.pow((1 + float(interest_rate)), float(years_saving))
        else :
            print("Invalid choice, try again")

def monthly_repayment(interest_rate, house_val, num_on_months) :
    return (interest_rate * house_val) / (1 - (math.pow((1 + interest_rate), -num_on_months)))


print("Chose either 'investment' or 'bond from the menu below to proceed: \n\n")
print("Investment  -  To calculate the amount of interest you'll earn on your investment")
print("Bond        -  To calculate the amount you'll have to pay on a home loan")
        
# Loop until the user inputs a valid response
# Save the response as uppercase and break the loop
while True :
    choice = input()
    if choice.upper() == "INVESTMENT" :
        choice = choice.upper()
        break
    elif choice.upper() == "BOND" :
        choice = choice.upper()
        break
    else :
        print("Invalid choice, try again")



if choice == 'INVESTMENT' :
    print("Please enter your initial deposit")
    deposit = get_initial_val()

    print("Please enter the expected rate of growth")
    interest_rate = get_interest_rate()

    print("How many years do you plan to invest for?")
    time_period = time_period() 

    print("Would you like a simple or compound calculation? Use S for simple or C for compound")
    amount_in_pot = amount_in_pot(deposit, interest_rate, time_period)
    print(round(amount_in_pot, 2))

else : 
    print("Please enter the value of the house")
    house_val = get_initial_val()

    print("Please enter the annual interest rate")
    interest_rate = get_interest_rate() / 12

    print("How many months will you repay the bond over?")
    time_period = time_period() 
    print(time_period)

    monthly_repayment = monthly_repayment(house_val, interest_rate, time_period)
    print(round(monthly_repayment, 2))