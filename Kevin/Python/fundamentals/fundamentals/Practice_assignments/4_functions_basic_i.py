#1 This function will return 5 when number_of_food_groups is called. 
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2 This function will give u an error because "number_of_days_in_a_week_silicon_or_triangle_sides()" has not been declared. 
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3 This function will return 5 because once there is a return the code will not go through the next line and the function will be over. 
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4 This function will simply return 5 without the print of 10. 
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5 This function will print 5 and none, due to the lack of return function. 
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#6 This function does not have a return function therefore the print that is out of it wont work
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))


#7 This function will concatenate 2 and 5 to get 25
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8 THe function will print the value 100 and then will return 10. 
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 THis code will run a function 3 times where 2 is less than 3 therefore will print out 7 and the 5 is more than 3 therefore will print out 14 and finally the summary of the numbers is 21. 
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 THis block will simply sum 2 numbers and will escape the 10 return. 
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 THis code just assign a value of 500 to b and then during the ejecution of the function override it for 300 and then will return to his original value 500.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12 Even though we have a return the return is not being assign to the variable b, therefore we will have a similar behaviro than the excercise above.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13 THis excercise will finally override the value of b for 300. 
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 We are jus calling 2 funtioncs that prints out numbers 1, 3 and 2
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 we have a print(1), then we called bar() that prints a 3 and returns a 5, therefor x will take this value and will be printed out
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)