class SLNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Slist:
    counter = 0
    def __init__(self):
        self.head = None
    
    def addtofront(self,val):
        new_node = SLNode(val)### creation of new node
        new_node.next = self.head #### Pointing to original self.head as new next path. 
        self.head = new_node ###Assigning new node as self.head to indicate that this is the first value.
        return self
    
    def addtoback(self,val):
        if self.head == None:
            self.addtofront(val)
        else:
            new_node = SLNode(val)
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next =  new_node
        return self
    
    def insert_att(self,val,n):
        if self.head == None or n == 0:
            self.addtofront(val)
        else:
            runner = self.head
            while runner != None: 
                if (n-1) == Slist.counter: 
                    new_node = SLNode(val)
                    new_node.next = runner.next
                    runner.next = new_node
                runner = runner.next
                Slist.counter += 1
        if n > Slist.counter:
            self.addtoback(val)
        return self
    
    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.val)
            runner = runner.next
        return self
    
    def remove_from_front(self):
        if self.head == None:
            print("There is nothing to remove. Empty list")
        else:
            self.head = self.head.next
        return self
    
    def remove_from_back(self):
        if self.head == None:
            print("There is nothing to remove. Empty list")
        else:
            runner = self.head
            if runner.next == None:
                self.head = None
            while runner.next.next != None:
                runner = runner.next
            runner.next = None
        return self
    
    def remove_val(self,val):
        if self.head.val == val:
            self.remove_from_front()
        else:
            runner = self.head
            while runner.next != None:
                if runner.next.val == val:
                    if runner.next.next != None:
                        runner.next = runner.next.next
                runner = runner.next
        if runner.val == val:
            self.remove_from_back()
        return self



my_slinklist = Slist()
my_slinklist.addtofront(1)
my_slinklist.addtofront(2).addtoback(3).addtoback(4)
my_slinklist.insert_att(5,0).remove_from_back().remove_from_front().remove_val(3)

my_slinklist.print_values()