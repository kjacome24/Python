##########List
class Slist:
    counterl = 0
    def __init__(self):
        self.head = None
    
    def addtofront(self,val):
        #create a node with the give value
        new_node = SLNode(val)
        #set the new node's next to the current head
        new_node.next = self.head
        #set the list's head to the new node
        self.head = new_node
        return self
    
    def add_to_back(self,val):
        if self.head == None: #code in case the list is empty
            self.addtofront(val)
            return self
        new_node = SLNode(val) ##adding to back
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    
    def insert_at(self,val,n):
        if self.head == None or n == 0:
            self.addtofront(val)
            return self
        else:
            runner = self.head
            while runner != None:
                if (n-1) == Slist.counterl:
                    new_node = SLNode(val)
                    new_node.next = runner.next ###With this we are saying to the new node which is the "Next" rout.
                    runner.next = new_node ##with this we are saying to the previous node that now he need to go nex to this node. 
                runner = runner.next
                Slist.counterl += 1
        if n > Slist.counterl:
            self.add_to_back(val)
        return self
    
    def remove_from_front(self):
        if self.head == None:
            print("The linked list is empty already")
        else:
            self.head = self.head.next
        return self
    
    def remove_from_back(self):
        if self.head == None:
            print("The linked list is empty already")
        else:
            runner = self.head
            if runner.next == None:
                self.head = None
            else:
                while runner.next.next != None:
                    runner = runner.next
                runner.next = None 
        return self
    
    def remove_val(self,val):
        runner = self.head
        if runner.value == val:
            self.head = runner.next
        else:
            while runner.next != None:
                if runner.next.value == val:
                    if runner.next.next != None:
                        runner.next = runner.next.next
                runner = runner.next
        if runner.value == val:
            self.remove_from_back()
        return self
    
        
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self


###############Node
class SLNode:
    def __init__(self,val):
        self.value = val
        self.next = None

my_list = Slist()
my_list.add_to_back("arturo").add_to_back("Jacome").add_to_back("Duque")
my_list.insert_at("kevin",0)
my_list.remove_from_back().remove_from_back().remove_from_back().remove_from_back().remove_from_back()
my_list.print_values()