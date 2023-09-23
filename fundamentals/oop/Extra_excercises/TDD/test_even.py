# importar el marco de prueba de Python
import unittest
# nuestra "unidad"
# esto es en lo que estamos ejecutando nuestra prueba
def isEven(n):
    if n % 2 == 0:
       return True
    else:
       return False
# nuestras "pruebas unitarias"
# inicializado creando una clase que hereda de unittest.TestCase
class IsEvenTests(unittest.TestCase):
    # cada método de esta clase es una prueba que se ejecutará
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        # otra forma de escribir lo de arriba es
        self.assertTrue(isEven(2))
        self.assertIs(isEven(2), "True")
    def testThree(self):
        self.assertEqual(isEven(3), False)
        # otra forma de escribir lo de arriba es
        self.assertFalse(isEven(3))
    # cualquier tarea que quieras ejecutar antes de que se ejecute cualquier método anterior, ponlas en el método setUp
    def setUp(self):
        # agregar las tareas setUp
        print("running setUp")
    # cualquier tarea que quieras ejecutar después de que se ejecuten las pruebas, ponlas en el método tearDown
    def tearDown(self):
    # agrega las tareas de tearDown
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras pruebas

