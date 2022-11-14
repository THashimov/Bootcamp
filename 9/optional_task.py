sales_salary = int(2000)
sales_commission = float(0.08)

manager_salary = int(40)

# Using a while loop to ensure we repeat until there is a valid input
while True :
    type_of_worker = input("Are you a salesperson or manager? Select with M or S\n")
    if type_of_worker.upper() == 'M' :
        while True :
            hours = int(input("How many hours did you work this month?\n"))
            if hours >= 0 :
                print(f"You will get paid £{manager_salary * hours}")
                break
        break
    if type_of_worker.upper() == 'S' :
        while True :
            gross_sales = float(input("What is the amount of gross sales you have made this month?\n"))
            if gross_sales >= 0 :
                # Round value to decimal places 
                total_pay = round(sales_salary + (gross_sales * sales_commission), 2)
                print(f"You will get paid £{total_pay}")
                break
        break