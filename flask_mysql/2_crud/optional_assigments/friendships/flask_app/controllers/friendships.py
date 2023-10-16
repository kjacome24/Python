from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.friendship import Friendship
from flask_app.models.user import User

@app.route('/')
@app.route('/friendships')
def index():
    users_and_friends= User.get_users_with_friends()
    usersf = User.get_all()
    return render_template("authors.html",users_and_friends=users_and_friends,usersf=usersf)

@app.route('/add_friendships_users', methods=["POST"])
def add_friendships_users():
    if request.form.get("which_form")=="add_user":
        data = {"first_name": request.form.get("first_name"),
                "last_name": request.form.get("last_name")}
        User.save(data)
    elif request.form.get("which_form")=="add_friendship":
        data = {"user_id": request.form.get("user_id"),
            "friend_id": request.form.get("friend_id")}
        x = Friendship.check_friendship(data)
        if x[0]['count']==0:
            Friendship.new_friendship(data)
        else:
            print("Friendship already exists")
    return redirect ('/friendships')