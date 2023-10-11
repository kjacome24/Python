from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/')
@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    return render_template("index.html",dojos=dojos)

@app.route('/dojos/<int:id>')
def get_ninjas(id):
    data = {'id':id}
    dojosninjas = Dojo.get_dojos_with_ninjas(data)
    return render_template("ninjasbydojo.html",dojosninjas=dojosninjas)


@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "dojo_name": request.form.get("dojo_name"),
    }
    Dojo.save(data)
    return redirect('/')

@app.route('/ninjas')
def create_ninjas():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html",dojos=dojos)

@app.route('/ninjas/new', methods=["POST"])
def new_ninja():
    data = {
        "dojo_id": request.form.get("dojo_id"),
        "fname": request.form.get("fname"),
        "lname": request.form.get("lname"),
        "age": request.form.get("age"),
    }
    Ninja.new_ninja(data)
    return redirect(f"/dojos/{data['dojo_id']}")



