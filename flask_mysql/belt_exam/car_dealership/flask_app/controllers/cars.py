from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User 
from flask_app.models.car import Car 
from flask_bcrypt import Bcrypt
import datetime #####for date funtions
from datetime import date #####for date funtions
from dateutil.relativedelta import relativedelta #####for date funtions


###############Dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if session.get('id') == None:
        return redirect('/')
    else:
        cars = Car.get_all()
        return render_template("dashboard.html", cars=cars)

###############Show cars
@app.route('/show/<int:id>')
def new_Car(id):
    if session.get('id') == None:
        return redirect('/')
    data = {'id':id}
    car = Car.get_one(data)
    return render_template("show_Car.html",car=car)



###############Edit existing cars
@app.route('/edit/<int:id>')
def edit_car(id):
    if session.get('id') == None:
        return redirect('/')
    data = {"id":id}
    car = Car.get_one(data)
    return render_template("edit_car.html",car=car)

@app.route('/edit/processing', methods=['POST'])
def edit_car_form():
    data = {"price":request.form.get("price"),
            "model":request.form.get("model"),
            "make":request.form.get("make"),
            "year":request.form.get("year"),
            "description": request.form.get("description"),
            "car_id": request.form.get("car_id")
            }
    if not Car.validate_entry(data):
        return redirect(f"/edit/{data['car_id']}")
    Car.update(data)
    return redirect("/dashboard")

###############New car for sale
@app.route('/new', methods=['GET', 'POST'])
def add_car():
    if session.get('id') == None:
        return redirect('/')
    return render_template("new_car.html")


@app.route('/new/add', methods=['POST'])
def add_car_form():
    data = {"price":request.form.get("price"),
            "model":request.form.get("model"),
            "make":request.form.get("make"),
            "year":request.form.get("year"),
            "description": request.form.get("description"),
            "user_id" : session["id"]
            }
    if not Car.validate_entry(data):
        return redirect("/new")
    Car.save(data)
    return redirect("/dashboard")
#######################purchase


@app.route('/new_purchase', methods=['POST'])
def new_purchase():
    data = {
        "user_id" : request.form.get("user_id"),
        "car_id" : request.form.get("car_id")
    }
    Car.add_purchase(data)
    return redirect(f"/user/{session['id']}")

#######################Delete car



@app.route('/destroy_car/<int:id>')
def destroy_car(id):
    if session.get('id') == None:
        return redirect('/')
    data = {"id": id}
    Car.destroy(data)
    return redirect("/dashboard")



