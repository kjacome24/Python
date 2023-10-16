from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email ####FIle is the name of the file of the model and File is the object.


@app.route('/')
def index():
    return render_template("index.html")

###The following example get the info from the form and save the record. 
@app.route('/insert_record', methods=["POST"])
def insert_record():
    if not Email.validate_entry(request.form): 
        return redirect('/')
    data = {
        "email" : request.form["email"]
    }
    Email.save(data)
    return redirect('/success')

@app.route('/success')
def registered_emails():
    emails = Email.get_all()
    return render_template("registered_emails.html",emails=emails)

############The following example destroy the session.
@app.route('/delete/<int:id>')
def delete_by_user(id):
    data = {'id': id}
    Email.delete_by_user(data)
    return redirect ('/success')



