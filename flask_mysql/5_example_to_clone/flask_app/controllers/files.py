from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.file import File ####FIle is the name of the file of the model and File is the object.


@app.route('/')
def index():
    return render_template("index.html")

###The following example get the info from the form and save the record. 
# @app.route('/create_user', methods=["POST"])
# def create_user():
#     if not File.validate_entry(request.form): 
#         return redirect('/users/new')
#     data = {
#         "fname": request.form["fname"],
#         "lname" : request.form["lname"],
#         "email" : request.form["email"],
#     }
#     File.save(data)
#     return redirect('/')


########THe following exmple get the id from the URL as input and then uses it for the query. 
# @app.route('/users/<int:id>')
# def filter_by_user(id):
#     data = {'id': id}
#     return render_template("show_user.html",users=File.filter_email(data))

############The following example destroy the session.
# @app.route('/users/<int:id>/destroy')
# def delete_by_user(id):
#     data = {'id': id}
#     User.delete_by_user(data)
#     return redirect ('/users')


