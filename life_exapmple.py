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