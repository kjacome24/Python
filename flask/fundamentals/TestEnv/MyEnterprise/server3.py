from flask import Flask, render_template
app = Flask(__name__) 
@app.route('/repeat/<int:num>/<string:texto>')
def repeat(num,texto):
        return render_template("repeat.html",num=num, texto=texto)


if __name__ == "__main__": # Se asegura de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True) # Ejecutamos la aplicación en modo depuraciónarg