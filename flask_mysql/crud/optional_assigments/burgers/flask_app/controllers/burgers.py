from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.burger import Burger
from flask_app.models.restaurant import Restaurant
from flask_app.models.topping import Topping

@app.route('/')
def index():
    all_toppings = Topping.get_all()
    all_restaurants = Restaurant.get_all()
    ############THis code is just for testing
    print("---------------------------")
    data = {"id":'1'}
    x = Restaurant.get_restaurant_with_burgers(data) ########We call a function in restaurant that creates the object restaurant of the id we provide and it also creates the objects of the burguers. 
    print(x.name)######## This is the way to call the restaurant
    for i in x.burgers: #####many to many
        print(i.name)
    y = Burger.get_burger_with_toppings(data)
    print(y.name)
    for x in y.toppings:
        print(x.topping_name)
    #############End of the testing
    return render_template("index.html",all_restaurants=all_restaurants,all_toppings=all_toppings)

@app.route('/create',methods=['POST'])
def create():
    print(request.form)
    if not Burger.validate_burger(request.form):
        return redirect('/')
    if request.form.get('which_form')=="register_burger":
        data = {
            "name":request.form['name'],
            "bun": request.form['bun'],
            "meat": request.form['meat'],
            "calories": request.form['calories'],
            "restaurant_id": request.form['restaurant_id'],
            "topping_id": request.form['topping_id']
        }
        x = Burger.save(data)
        data = {
            "topping_id": request.form['topping_id'],
            "burger_id": x[0]['id']
        }
        Topping.save_topic_in_burger(data)
        return redirect('/burgers')
    elif request.form.get('which_form')=="register_restaurant":
        data = {
            "name":request.form['restaurant_name'],
        }
        Restaurant.save(data)
        return redirect('/')
    elif request.form.get('which_form')=="register_topping":
        data = {
            "topping_name":request.form['topping_name'],
        }
        Topping.save(data)
        return redirect('/')


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