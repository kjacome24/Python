from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User 
from flask_app.models.thought import Thought 
from flask_bcrypt import Bcrypt
import datetime #####for date funtions
from datetime import date #####for date funtions
from dateutil.relativedelta import relativedelta #####for date funtions
from flask_app.models import user

@app.route('/dashboard')
@app.route('/thoughts')
def dashboard():
    if session.get('id') == None:
        return redirect('/')
    else:
        data = {'id':session['id']}
        thoughts = Thought.get_thought_with_likes(data)
        return render_template("thoughts.html",thoughts=thoughts)

@app.route('/new_thought', methods=['POST'])
def new_thought():
    data = {'user_id': request.form.get("user_id"),
            'new_thought': request.form.get("new_thought")
            }
    print(data)
    if not Thought.validate_entry(data):
        return redirect('dashboard')
    Thought.save(data)
    return redirect('dashboard')


@app.route('/destroy/<int:id>')
def delete_recipe(id):
    if session.get('id') == None:
        return redirect('/')
    data = {"id":id}
    Thought.destroy(data)
    return redirect('/dashboard')

@app.route('/new_like', methods=['POST'])
def user_like():
    if request.form.get("which_form")=="like":
        data = {'user_id': session['id'],
            'thought_id': request.form.get("thought_id")
            }
        print(Thought.user_like(data))
    else:
        print(request.form)
        data = {'user_id': session['id'],
            'thought_id': request.form.get("thought_id")
            }
        Thought.destroy_like(data)
    return redirect('/dashboard')













