from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User 
from flask_app.models.thought import Thought 
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST': ##########We make sure we are entering by a post request.
        print(request.form)
        print("Here we are 1")
        if not User.validate_entry(request.form): ###### We validate the entry in both forms
            return redirect('/')
        print("Here we are 2")
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
            return redirect('/thoughts')
        elif request.form.get("which_form")=='log_in':
            print("Here we are 3")
            data = {
            "email" : request.form.get("email"),
            "password" : request.form.get("password")
            }
            print("Here we are 4")
            user=User.getbyemail(data)
            print("Here we are 5")
            if user is None or  not bcrypt.check_password_hash(user.password, data['password']):
                flash(["Invalid Email/Password",1])
                print("Here we are 6")
                return redirect('/')
            session["id"] = user.id
            session["first_name"] = user.first_name
            session["last_name"] = user.last_name
            session["email"] = user.email
            return redirect('/thoughts')
    else:
        return render_template("index.html")


@app.route('/destroy', methods=['GET', 'POST'])
def log_out():
    session.clear()
    return redirect ('/')

@app.route('/users/<int:id>')
def user_thoughts(id):
    if session.get('id') == None:
        return redirect('/')
    else:
        data = {"id": id}
        user_with_thoughts = User.get_user_with_thoughts(data)
        return render_template("user_thoughts.html",user_with_thoughts=user_with_thoughts)