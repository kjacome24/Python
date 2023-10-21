from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User 
from flask_app.models.sighting import Sighting 
from flask_bcrypt import Bcrypt
import datetime #####for date funtions
from datetime import date #####for date funtions
from dateutil.relativedelta import relativedelta #####for date funtions
from flask_app.models import user

@app.route('/sightings')
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if session.get('id') == None:
        return redirect('/')
    else:
        data = {'id':session['id']}
        sightings = Sighting.get_sightins_with_likes(data)
        return render_template("dashboard.html", user=user,x=sightings)

@app.route('/new_sighting', methods=['GET', 'POST'])
def new_sighting():
    if session.get('id') == None:
        return redirect('/')
    return render_template("new_sighting.html")


@app.route('/create_sighting', methods=["POST"])
def create_update_sighting():
    if session.get('id') == None:
        return redirect('/')
    else:
        print(request.form)
        if not Sighting.validate_entry(request.form):
            if request.form.get("which_form")=="crea_new":
                return redirect('new_sighting')
            else:
                sighting_id = request.form.get("id")
                return redirect(f'/sightings/edit/{sighting_id}')
        data = {
                "location" : request.form.get("location"),
                "description" : request.form.get("description"),
                "date_of_sighting" : request.form.get("date_of_sighting"),
                "number_of_sesquatches" : request.form.get("number_of_sesquatches"),
                "user_id": session['id']
        }
        if request.form.get("which_form")=="crea_new":
            Sighting.save(data)
        else:
            data['id'] = request.form.get("id")
            print(data)
            Sighting.update(data)
    return redirect('/dashboard')


@app.route('/sighting/edit/<int:id>')
def edit_sighting(id):
    if session.get('id') == None:
        return redirect('/')
    data = {"id":id}
    sighting= Sighting.get_one(data)
    x = str(sighting.date_of_sighting)
    x = x[0:10]
    sighting.date_of_sighting = x
    print(sighting.date_of_sighting)
    return render_template("edit_sighting.html",sighting=sighting)


@app.route('/sighting/<int:id>/destroy')
def delete_sighting(id):
    if session.get('id') == None:
        return redirect('/')
    data = {"id":id}
    Sighting.destroy(data)
    return redirect('/dashboard')

@app.route('/sighting/<int:id>')
def view_sighting(id):
    if session.get('id') == None:
        return redirect('/')
    data = {"sighting_id":id,
            "id": session["id"]}
    sighting=Sighting.get_sightings_with_users(data)
    return render_template("view_sighting.html",sighting=sighting)


@app.route('/remove_skeptical', methods=['GET', 'POST'])
def remove_skeptical():
    data = {
        "user_id" : request.form.get("user_id"),
        "sighting_id" : request.form.get("sighting_id")
    }
    Sighting.remove_skeptical(data)
    return redirect(f"/sighting/{data['sighting_id']}")

@app.route('/add_skeptical', methods=['GET', 'POST'])
def add_skeptical():
    data = {
        "user_id" : request.form.get("user_id"),
        "sighting_id" : request.form.get("sighting_id")
    }
    Sighting.add_skeptical(data)
    return redirect(f"/sighting/{data['sighting_id']}")