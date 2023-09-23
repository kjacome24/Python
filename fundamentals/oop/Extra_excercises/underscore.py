class Underscore:
    def filter(self, iterable, callback):
        self.listf = []
        for i in range(len(iterable)):
            if callback(iterable[i]):
                self.listf.append(iterable[i])
        return self.listf
    
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i]) 
        return iterable
    
    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if callback(iterable[i]):
                return iterable[i]
    
    def reject (self, iterable, callback): 
        self.listf = []
        for i in range(len(iterable)):
            if not callback(iterable[i]):
                self.listf.append(iterable[i])
        return self.listf

_ = Underscore()

evens =_.map([1,2,3], lambda x: x*2)
print(evens)

evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)

evens = _.find([1,2,3,4,5,6], lambda x: x>4)
print(evens)

evens = _.reject([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [1,3,5]
print(evens)


