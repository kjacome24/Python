from flask import Flask #Importing Flas libraries and packages

app = Flask(__name__) ###We are creating an instance

@app.route('/')
def index():
    return "Hello world xxxxxxxxxxxx"

@app.route('/dojo')
def dojo():
    return "Dojo!!!"

@app.route('/dojo')
def dojof():
    return "Dojo!!!"

@app.route('/say/<name>')
def namef(name):
    return "Hello " + name

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num,name):
        return ('\n' + name + '\n') * num 

@app.route('/<string:variable>')
def undefinedx(variable):
    return f"Sorry. THere is no reponse with {variable}. Try again"

if __name__== "__main__":
    app.run(debug=True)