from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User 
from flask_app.models.recipe import Recipe 
from flask_bcrypt import Bcrypt
import datetime #####for date funtions
from datetime import date #####for date funtions
from dateutil.relativedelta import relativedelta #####for date funtions
from flask_app.models import user

@app.route('/recipes')
@app.route('/dashboard')
def dashboard():
    if session.get('id') == None:
        return redirect('/')
    else:
        user = User.getId(session)
        recipes=Recipe.get_all()
        return render_template("dashboard.html", user=user,x=recipes)

@app.route('/new_recipe')
def new_recipe():
    if session.get('id') == None:
        return redirect('/')
    return render_template("new_recipe.html")


@app.route('/create_recipe', methods=["POST"])
def create_update_recipe():
    if session.get('id') == None:
        return redirect('/')
    else:
        print(request.form)
        if not Recipe.validate_entry(request.form):
            if request.form.get("which_form")=="crea_new":
                return redirect('new_recipe')
            else:
                recipe_id = request.form.get("id")
                return redirect(f'/recipes/edit/{recipe_id}')
        data = {
                "name" : request.form.get("name"),
                "description" : request.form.get("description"),
                "instructions" : request.form.get("instructions"),
                "date_cooked" : request.form.get("date_cooked"),
                "under_30_min" : request.form.get("under_30_min"),
                "user_id": session['id']
        }
        if request.form.get("which_form")=="crea_new":
            Recipe.save(data)
        else:
            data['id'] = request.form.get("id")
            print(data)
            Recipe.update(data)
    return redirect('/dashboard')


@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if session.get('id') == None:
        return redirect('/')
    data = {"id":id}
    recipe= Recipe.get_one(data)
    x = str(recipe.date_cooked)
    x = x[0:10]
    print(x)
    recipe.date_cooked = x
    return render_template("edit_recipe.html",recipe=recipe)


@app.route('/recipes/<int:id>/destroy')
def delete_recipe(id):
    if session.get('id') == None:
        return redirect('/')
    data = {"id":id}
    Recipe.destroy(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def view_recipe(id):
    if session.get('id') == None:
        return redirect('/')
    data = {"id":id}
    recipe=Recipe.get_recipies_with_users(data)
    return render_template("view_recipe.html",recipe=recipe)
