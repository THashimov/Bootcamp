class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product 
        self.cost = cost
        self.quantity = quantity
        
    def get_country(self):
        return self.country
        
    def get_code(self):
        return self.code

    def get_product(self) :
        return self.product

    def get_cost(self):
       return int(self.cost)

    def get_quantity(self):
        return int(self.quantity)

    def __str__(self):
        return f"\n{self.country},{self.code},{self.product},{self.cost},{self.quantity}"