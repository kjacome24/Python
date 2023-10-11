from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.burger import Burger
from flask_app.models.restaurant import Restaurant

@app.route('/')
def index():
    
    all_restaurants = Restaurant.get_all()
    print("---------------------------")
    data = {"id":'1'}
    x = Restaurant.get_restaurant_with_burgers(data) ########We call a function in restaurant that creates the object restaurant of the id we provide and it also creates the objects of the burguers. 
    print(x.name)######## This is the way to call the restaurant
    for i in x.burgers:
        print(i.name)
    return render_template("index.html",all_restaurants=all_restaurants)

@app.route('/create',methods=['POST'])
def create():
    data = {
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories'],
        "restaurant_id": request.form['restaurant_id']

    }
    Burger.save(data)
    return redirect('/burgers')


@app.route('/burgers')
def burgers():
    return render_template("results.html",all_burgers=Burger.get_all())


@app.route('/show/<int:burger_id>')
def detail_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("details_page.html",burger=Burger.get_one(data))

@app.route('/edit_page/<int:burger_id>')
def edit_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("edit_page.html", burger = Burger.get_one(data))

@app.route('/update/<int:burger_id>', methods=['POST'])
def update(burger_id):
    data = {
        'id': burger_id,
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.update(data)
    return redirect(f"/show/{burger_id}")

@app.route('/delete/<int:burger_id>')
def delete(burger_id):
    data = {
        'id': burger_id,
    }
    Burger.destroy(data)
    return redirect('/burgers')