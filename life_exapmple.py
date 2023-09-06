###tuples

x = True
print(type(x))

y = ("zo","xo","yo")

print(len(y))

print(y[len(y)-1])

y[1] = "wo"


##Lists

l1 = []
ninjas = ["Rozen","KB","Oliver"]
print(ninjas[2])
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)
ninjas.pop()
print(ninjas)
ninjas.pop(1)
print(ninjas)

##dictionaries

Empty_dic = {}
new_person  = {'name':'john','age':'38','weight':160.2, 'wearing_glasses':False}


new_person['name'] = 'kevin'


new_person['hobbies'] = ['climbing','programing'] #you can use this to add a new entry
print(new_person)

weight = new_person.pop('weight')
print(weight)
print(new_person)

print(type(weight)) # type helps u to knwo the type of variable or value. 
print(type(new_person))

print(type(2))


print(len(new_person))
print(len('Hola chiquitas'))


x = complex(4.9) 
y = 2.5

z = x + y
print(x)


entero_a_flotante = float(35)
floatante_a_entero = int(44.2)
entero_a_complejo = complex(35)
print(entero_a_flotante)
print(floatante_a_entero)
print(entero_a_complejo)
print(type(entero_a_flotante))
print(type(floatante_a_entero))
print(type(entero_a_complejo))

#############module to use random option. 
import random

print(random.randint(2,5))


#########How to concat a non-string to a string
print("Hola " + str(42))

total = 35
user_val = "26"

total = total + int(user_val)


#####f string

primer_nombre = "Zen"
apellido = "Coder"
edad = 27
print(f"Mi nombre es {primer_nombre} {apellido} y tengo {edad} años de edad.")

####string.format()

print("Mi nombre es {} el hombre".format(primer_nombre))
print("Mi nombre es {} {} y tengo {} años de edad.".format(primer_nombre, apellido, edad))



#####%-formatting

hw = "Hola %s" % "mundo" 	# con valores literales
py = "Me encanta Python %d" % 3 
print(hw, py)


##############string upper and other functions
x = 'Hola'
y = str.upper(x)
y = str.lower(x)

y = str.isalnum(x) #devuelve un booleano dependiendo de si la longitud de la cadena es > 0 y todos los caracteres sean alfanuméricos (solo letras y números). Las cadenas que incluyen espacios y puntuación devolverán False con este método. 
print(y)



frutas = ['manzana', 'plátano', 'naranja', 'frutilla']
vegetales = ['lechuga', 'pepino', 'zanahorias']
frutas_y_vegetales = frutas + vegetales
print(frutas_y_vegetales)
ensalada = 3 * vegetales
print(ensalada)


x = [99,4,2,5,-3]
print(x[:])
# la salida sería [99,4,2,5,-3]
print(x[1:])
# la salida sería [4,2,5,-3];
print(x[:4])


a = [1,2,4,7,3,5]
print(sorted(a)) #organizes de list with sort
print(min(a)) #organizes de list with sort


print(a.index(7)) #Index devuelve la posición del índice en una lista para el parámetro dado. 


tupla_datos = ('física', 'química', 1997, 2000)
tupla_num = (1, 2, 3, 4, 5 )
tupla_letras = "a", "b", "c", "d" #You can have tuples without paretesis

print(type(tupla_letras))

perro = ("Canis Familiaris", "perro", "carnívoro", 12)

perro = perro + ("doméstico",)
print(perro)
# el resultado...
#("Canis Familiaris", "Perro", "carnívoro", 12, "doméstico")

#Bucle for with string
for x in 'Hello':
    print(x)


#Loop showing elements in a list
Listk = [1, "a", "b"]
for i in Listk:
    print(i)

#Loop using len and range
Listk = [1, "a", "b"]
for i in range(0, len(Listk)):
    print(i, Listk[i])


### loop with tuple
perro = (1, 3, 4)

for data in perro:
    print(data)

### loop with dictionary. By default it will show the key unles u force it to show the value

dick = {"Kev": "Duque", "Art":"Jacome"}

for i in dick:
    print(dick[i])

for i in dick.values(): # to print values directly
    print(i)

for i in dick.keys(): # to print values directly
    print(i)

for x, y in dick.items():
    print(x,y)    

#While loop

count = 4
while count>=1:
    print(count)
    count -= 1

else:
    print("Is done")


### sentence break

for val in "cadena":
    if val =="e":
        break
    print(val)

# Sentence continue
for val in "cadena":
    if val == "e":
        continue
    print(val)


y = 3
while y > 0:
    print(y)
    y = y - 1

else:		# solo se ejecuta en una salida limpia del bucle while (es decir, no un break)
    print("sentencia else final")
# salida: 3, 2, 1



x = 2
if x 

x=[1,2]

x += 2

print(x)


#####Functions
###Example 1
def add(a,b):
    x = a + b

    return x

New_val = add (4,2)
print(New_val)


###Example 2
def say_hello(name):
    return f"hola {name}"

yo = say_hello("Kevin")

print(yo)

###Example 3

def di_hola(nombre):
    return "Hola " + nombre
saludo = di_hola("Michael") # el valor devuelto por la función di_hola se asigna a la variable 'saludo'
print(saludo) # esto dará como resultado 'Hola Michael'

####Example 4
def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
print(sum3)


#####Example 5

def be_cheerful(name="Allan", repeat=2): #Defoult parameter
    print(f"Good morning {name}\n" * repeat)

be_cheerful("Adrien",3)
be_cheerful()

be_cheerful(repeat=5,name="Loura")
be_cheerful(repeat=5)

#####Example 6 (Kevin version to multiple values inside of a list for a second input parameter)
def multiplicar(num_list, num):
    print(num_list, num)
    y = []
    for x in num_list:
        x *= num
        y.append(x)
    return y
a = [2,4,10,16]
b = multiplicar(a,5)
print(b)
# salida:
# [2,4,10,16]

#####Example 7(platform version to multiple values inside of a list for a second input parameter)

def multiplicar(num_list, num):
    for x in range (len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiplicar(a,5)
print(b)


#5
def número_de_lagos_grandes():
    print(5)
x = número_de_lagos_grandes()
print(x)
