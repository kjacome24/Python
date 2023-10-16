from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User 
from flask_app.models.message import Message 
from flask_bcrypt import Bcrypt

# Creación de objeto Bcrypt
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST': ##########We make sure we are entering by a post request.
        print(request.form)
        if not User.validate_entry(request.form): ###### We validate the entry in both forms
            return redirect('/')
        if request.form.get("which_form")=='register_user': ######If is the first form of regestiring. 
            data = {
            "first_name" : request.form.get("first_name"),
            "last_name" : request.form.get("last_name"),
            "email" : request.form.get("email"),
            "password" : bcrypt.generate_password_hash(request.form.get("password")),
            }
            user=User.getbyemail(data)
            if user is not None:
                flash(["Email address has been already registered!",0])
                return redirect('/')
            user=User.save(data)
            session["id"] = user.id
            session["first_name"] = user.first_name
            session["last_name"] = user.last_name
            session["email"] = user.email
            data = {'sender_id': session['id']}
            session["num_sent_messages"] = len(Message.get_all_by_sender(data))
            return redirect('/dashboard')
        elif request.form.get("which_form")=='log_in':
            data = {
            "email" : request.form.get("email"),
            "password" : request.form.get("password")
            }
            user=User.getbyemail(data)
            if user is None or  not bcrypt.check_password_hash(user.password, data['password']):
                flash(["Invalid Email/Password",1])
                return redirect('/')
            session["id"] = user.id
            session["first_name"] = user.first_name
            session["last_name"] = user.last_name
            session["email"] = user.email
            return redirect('/dashboard')
    else:
        return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    if session.get('id') == None:
        return redirect('/')
    else:
        user = User.getId(session)
        users = User.get_all()
        data = {"receiver_id":session["id"]}
        print(data)
        messages = Message.get_all_by_receiver(data)
        data = {'sender_id': session['id']}
        session["num_sent_messages"] = len(Message.get_all_by_sender(data))
        session["num_received_messages"] = len(messages)
        
        return render_template("dashboard.html", user=user,users=users,messages=messages)


@app.route('/destroy', methods=['POST'])
def log_out():
    session.clear()
    return redirect ('/')



########THe following exmple get the id from the URL as input and then uses it for the query. 
# @app.route('/users/<int:id>')
# def filter_by_user(id):
#     data = {'id': id}
#     return render_template("show_user.html",users=File.filter_email(data))


