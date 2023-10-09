from store import Store
from product import Product

x = Store("Kevin's store")

x.add_product(Product("shampoo",1000,"cleaning"))
x.add_product(Product("shampoo2",1000,"cleaning"))
x.add_product(Product("Sauceges",1000,"food"))
x.sell_product(0)
x.inflation(0.02)
x.set_clearance("cleaning",0.02)
x.print_products()
print(x.list2)