prod_one = input("What would you like to add to your shopping list? ")
prod_two = input("What would you like to add to your shopping list? ")
prod_three = input("What would you like to add to your shopping list? ")

price_one = float(input(f"Please enter a price for {prod_one} to 2 decimal points "))
price_two = float(input(f"Please enter a price for {prod_two} to 2 decimal points "))
price_three = float(input(f"Please enter a price for {prod_three} to 2 decimal points "))

total_price = price_one + price_two + price_three

avg_price = round(total_price / 3)

print(f"The total of [{prod_one}], [{prod_two}] and [{prod_three}] is £{total_price}. \nThe average price is £{avg_price}")