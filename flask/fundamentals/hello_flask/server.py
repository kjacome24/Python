from flask import Flask, render_template ### with this line we are able to use the modules and packages of flask
app = Flask(__name__)  #We are calling the class Flask and creating an object called app


@app.route('/')###THis decorator links the route with the following fucntion
def hello_world():
    return render_template("index.html")

@app.route('/success')
def success():
    return "success"

@app.route('/hola/<name>')
def hola(name):
    print(name)
    return "Hola " + name

@app.route('/users/<username>/<id>')
def show_user_profile(username,id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/extra/<string:name>/<int:num>')
def extra(name,num):
    return f"Hello {name}*"*num

@app.route('/main/<string:name>/<int:num>')
def main(name,num):
    return render_template("hello.html",num=num,name=name)

if __name__=="__main__": ###This function basically makes sure that the module is being executed directly and not from another file. 
    app.run(debug=True)