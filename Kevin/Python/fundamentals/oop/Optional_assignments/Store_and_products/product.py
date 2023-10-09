class Product:
    def __init__(self,product_name,price,category):
        self.product_name = product_name
        self.price = price
        self.category = category
    
    def update_price(self,percentage_update,is_high):
        if is_high:
            self.price = self.price + (percentage_update * self.price)
        else:
            self.price = self.price - (percentage_update * self.price)
    
    def print_info (self):
        print(f"Product name: {self.product_name} \nProduct price: {self.price} \ncategory: {self.category}")
    