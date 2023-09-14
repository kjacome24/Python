# Filename: server.py

from flask import Flask # Importamos la clase Flask

app = Flask(__name__) # Creamos una instancia de la clase Flask

@app.route('/') # Decorador de ruta
def index(): # Función que se ejecuta cuando se accede a la ruta raíz
    return "<h1>Hola Mundo Flask!!</h1>" # Devolvemos una cadena de texto

@app.route('/success')
def success():
    return "success"

if __name__ == "__main__": # Se asegura de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True) # Ejecutamos la aplicación en modo depuración