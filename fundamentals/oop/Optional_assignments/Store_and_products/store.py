class Store:
    counter = 0
    def __init__(self,name):
        self.name = name
        self.list = []
        self.list2 = {}
    
    def add_product(self,new_product):
        self.list.append(new_product)
        self.list2[Store.counter] = new_product
        print(f"New product has been added with id: {Store.counter}")
        Store.counter += 1
    
    def sell_product(self,id):
        print("The sold product is:")
        self.list[id].print_info()
        self.list.pop(id)
        self.list2.pop(id)
    
    def inflation(self,percent_increase):
        for i in range (0,len(self.list)):
            self.list[i].update_price(percent_increase,True)
    
    def set_clearance(self,category,percent_discount):
        for q in range (0,len(self.list)):
            if self.list[q].category == category:
                self.list[q].update_price(percent_discount,False)
    
    def print_products(self):
        for x in self.list:
            print("-----------------------")
            x.print_info()
            print("-----------------------")