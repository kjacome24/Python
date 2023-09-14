# Filename: server.py
from flask import Flask, render_template # Importamos la clase Flask
#render template es una funcion que permite renderizar(Es decir generar la salida que se visualizara desde el lado del cliente)

app = Flask(__name__) # Creamos una instancia de la clase Flask

@app.route('/') # Decorador de ruta
def index(): # Función que se ejecuta cuando se accede a la ruta raíz
    return "<h1>Hola Mundo Flask!!</h1>" # Devolvemos una cadena de texto

# We can add as many routes as we want

@app.route('/description')
def description():
    return "<h1>Página de descripcion</h1>"

@app.route('/contact/office/')
def contact():
    return "<h1>Datos de contacto oficina: +56 9 11111111 </h1>"

@app.route('/hola/<nombre>/<apellido>/<int:edad>')
def hola(nombre, apellido,edad):
    return "<h1>Hola {0} {1} de {2} anos </h1>".format(nombre,apellido,edad)

@app.route('/user/<nombre>/<apellido>/<int:edad>')
def user (nombre, apellido,edad):
    return render_template('user.html',nombre = nombre,apellido = apellido, edad = edad)



if __name__ == "__main__": # Se asegura de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True) # Ejecutamos la aplicación en modo depuraciónarg