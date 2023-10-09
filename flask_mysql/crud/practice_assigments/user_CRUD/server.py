from flask import Flask, render_template, request, redirect, session
from users import User


app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
@app.route('/users')
def list_users():
    users = User.get_all()
    print(users)
    return render_template("users.html",users=users)

@app.route('/users/new')
def create_user_form():
    return render_template("new_user.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    last_id= User.last_id()
    last_id= int(last_id[0]['id'])+1
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    User.save(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect(f"/users/{last_id}")

@app.route('/users/<int:id>')
def filter_by_user(id):
    data = {'id': id}
    return render_template("show_user.html",users=User.filter_email(data))

@app.route('/users/<int:id>/destroy')
def delete_by_user(id):
    data = {'id': id}
    User.delete_by_user(data)
    return redirect ('/users')

@app.route('/users/<int:id>/edit')
def edit_by_user(id):
    data = {'id': id}
    return render_template("edit_user.html",users=User.filter_email(data))

@app.route('/users/<int:id>/update', methods=["POST"])
def update_users(id):
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "id": id,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    User.update_user(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect(f"/users/{id}")

if __name__ == "__main__":
    app.run(debug=True)