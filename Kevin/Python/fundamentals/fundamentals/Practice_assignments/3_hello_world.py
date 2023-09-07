# 1. TAREA: imprime "Hola, mundo"
print("Hello world" )
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Kevin"
print( "Hello,",name )	# con una coma
print( "Hello, " + name)	# con un +
# 3. imprimir "Hola 42!" con el número en una variable
name = 42
print( "Hello" , name )	# con una coma
print( "Hello " + str(name) )	# con una +	-- este debería arrojar un error!
# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love eating {} and {}".format(fave_food1,fave_food2) ) # con .format()
print(f"I love eating {fave_food1} and {fave_food2}") # con una cadena f
print("I love eating %s" % fave_food1, "and %s" % fave_food2) #%-formatting

#matrix dictionary with tuples
info1 = ("Kevin Jacome", "33 years old", "77kg")
info2 = ("Andres urrego", "27 years old", "82kg")
dict1 = { "01":info1, "02":info2
}
print(dict1.items())
print(dict1["01"])

##how to add values to the dictionary from 0
capitales = {} # crea un diccionario vacío y luego agrega valores
capitales["svk"] = "Bratislava"# this applies for new variables or if the var already exists then will overwrite it. 
capitales["deu"] = "Berlin"
capitales["dnk"] = "Copenhagen"
print(capitales)

# capitales.pop('svk')
del capitales['svk'] # this is an option that does the same job than pop without returning the deleted value.
print(capitales)


####Dictionaries
contexto = {'preguntas': 
            [
    { 'id': 1, 'content': '¿Por qué hay luz en el refrigerador y no en el congelador?'},
    { 'id': 2, 'content': '¿Por qué las ovejas no se encogen cuando llueve?'},
    { 'id': 3, 'content': '¿Por qué se llaman apartamentos cuando están todos pegados?'},
    { 'id': 4, 'content': '¿Por qué los autos conducen en la autopista y se estacionan en la entrada?'}
]}



print(contexto['preguntas'][1]["content"]) #This is the way on how to access to the nested dictionary
print(contexto2[1]["content"])



people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
        2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
print(people)
people[3] = {}
print(people)
people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people[3])