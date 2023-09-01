num1 = 42 #variable declaration where the data type is a primitive number
num2 = 2.3 #variable declaration where the data type is a primitive number
boolean = True #variable declaration where the data type is a primitive boolean
string = 'Hello World' #variable declaration where the data type is a primitive string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration where the data type is a composite list. 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration where the data type is a composite Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration where the data type is a composite Tuple. 
print(type(fruit)) # This is a log statement that validate sde type of the tuple
print(pizza_toppings[1]) #log statement that accesses to the value of the second element in the list. 
pizza_toppings.append('Mushrooms') # action that adds a value in the list
print(person['name'])# Log statement that access the value of "name" in the dictionary
person['name'] = 'George' # Action that updates the value of "name" in the dictionary
person['eye_color'] = 'blue'# Action that updates the value of "eye_color" in the dictionary
print(fruit[2]) #log statement that prints the third value of the tuple 

if num1 > 45: #conditional if
    print("It's greater") # Log statement
else:#conditional else
    print("It's lower") # Log statement

if len(string) < 5: #Conditional if that validates lenght of the string
    print("It's a short word!")# Log statement
elif len(string) > 15:#Conditional elif that validates lenght of the string
    print("It's a long word!")# Log statement
else:#Conditional else
    print("Just right!")# Log statement

for x in range(5): #for loop increment
    print(x)
for x in range(2,5):#for loop increment satarting from 2 to 5
    print(x)
for x in range(2,10,3): #for loop increment from 2 to 10 with a sequence of 3
    print(x)
x = 0
while(x < 5): # While loop with increment of one until 5
    print(x)
    x += 1
pizza_toppings.pop() # deleting last value within the list
pizza_toppings.pop(1) # deleting second value within the list


print(person) #log statement for the dictionary "Person"
person.pop('eye_color') #Deleting value "Eye color" within dictinary
print(person)#log statement after deleting parameter

for topping in pizza_toppings: # For loop within list where pepperoni is the start point and olives is the end,
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): # definition of function
    for num in range(10): #for loop that from 0 to 9 that calls a print saying hello.
        print('Hello')

print_hello_ten_times() # execution of fucntion

print(x)

def print_hello_x_times(x): #defintion of fucntion with a x parameter. 
    for num in range(x): # loop from  to x
        print('Hello') #log stament

print_hello_x_times(4) #execution of fucntion within an input parameter. 

def print_hello_x_or_ten_times(x = 10): #execution of fucntion within an input parameter that will be 10 if there is no input when calling the fucntion 
    for num in range(x): #for loop from 0 to x
        print('Hello3') #log statement


print_hello_x_or_ten_times(4) #exceution of function with input


"""
Bonus section
"""

# print(num3) #NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7]) #IndexError: list index out of range
# print(boolean)
# fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'pop'
# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'append'