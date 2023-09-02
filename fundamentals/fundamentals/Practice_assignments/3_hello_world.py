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