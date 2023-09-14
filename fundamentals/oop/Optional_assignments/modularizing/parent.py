local_val = "magical unicorns"
def square(x):
    return x * x

class User:
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        return "Hello"

if __name__ == "__main__":
    print("The file is being executed directly")
else:
    # __name__= "child"
    print("The file is being executed becasue it is imported by another file. The file is called",__name__)
print(square(5))
user = User("Kevin")
print(user.name)
print(user.say_hello())