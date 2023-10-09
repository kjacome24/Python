x = lambda num: num ** 2
print(x(5))
y = lambda num1, num2: num1 + num2
print(y(5,2))

#########Lambda inside of a list
# crea una nueva lista, con una lambda como elemento
my_list = ['test_string', 99, lambda x : x ** 2]
# acceder al valor en la lista
print(my_list[2]) # imprimirá un objeto lambda almacenado en la memoria
# invocar la función lambda, pasando 5 como argumento
print(my_list[2](5))

###lamda with callback
# definir una función que tome una entrada que sea una función
def invoker(callback):
    # invocar la entrada pasar el argumento 2
    print(callback(2))
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

###within a function

def incrementor(num):
    start = num
    return lambda x: num + x
x = incrementor(2)
print(x(2))

###within map buil-in funcionality
my_arr = [1,2,3,4,5]
print(list(map(lambda x: x ** 2, my_arr)))
print(list(map(lambda x: x+2,[1,2,3,4,5,6])))