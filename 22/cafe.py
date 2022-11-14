menu = ["Muffin", "Biscuit", "Carrot Cake", "Tea Bag"]

stock = {"Muffin": 10, "Biscuit": 15, "Carrot Cake": 30, "Tea Bag": 300}

price = {"Muffin": 2, "Biscuit": 1, "Carrot Cake": 5, "Tea Bag": 0.5}

val_of_total_stock = 0

# Loop over each product in the cafe
# Get the stock level of each element in the dictionary using the key value of item
# Get the price for each element in the dictionary using the key value of item
# Multiple the numbers together and add them to val_of_total_stock
for item in menu :
    stock_level = stock.get(str(item))
    item_price = price.get(str(item))

    val_of_total_stock += (stock_level * item_price)

print(val_of_total_stock)