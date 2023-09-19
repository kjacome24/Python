class DLNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class Dlist:
    counter = 0
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addtofront(self,val):
        new_node = DLNode(val)### creation of new node
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev =  new_node
            new_node.next = self.head
            self.head = new_node
        return self
    
    def addtoback(self,val):
        if self.head == None and self.tail == None:
            self.addtofront()
        else:
            new_node = DLNode(val)### creation of new node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return self
    
    def insert_at(self,val,n):
        if n == 0:
            self.addtofront(val)
        else:
            runner = self.head
            while runner != None:
                if Dlist.counter == (n-1):
                    new_node = DLNode(val)
                    new_node.prev = runner
                    new_node.next = runner.next
                    runner.next = new_node
                    if runner.next.next != None:
                        runner.next.next.prev = new_node
                runner = runner.next
                Dlist.counter += 1
        print(Dlist.counter)
        if Dlist.counter < n:
            self.addtoback(val)



    def print_values(self):
        runner = self.head
        while (runner != None):
            print(f"The node {runner.val} ({runner}) is priviusly connected to {runner.prev} and pointing to the {runner.next}")
            print("---------------------------------")
            runner = runner.next
        return self

my_dlist = Dlist()
my_dlist.addtofront("Duque")
my_dlist.addtofront("Jacome")
my_dlist.addtofront("Arturo")
my_dlist.addtofront("kevin")
my_dlist.insert_at("rey",2)
my_dlist.print_values()
