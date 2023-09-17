class Mathdojo:
    def __init__(self):
        self.result = 0
    
    def add(self,num,*nums):
        self.result +=  num
        for i in nums:
            self.result += i
        return self
    
    def subtract(self,num,*nums):
        self.result -=  num
        for x in nums:
            self.result -= x
        return self


md = Mathdojo()

x = md.add(2).add(2,5,1).add(1,1,1,1).subtract(3,2).subtract(1,1).subtract(1,2).result
print(x)