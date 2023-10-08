from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '123456'

userslist = []
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users',methods=['POST'])
def create_user():
        if request.form['which_form'] == 'register': 
            users = {}
            session['name'] = request.form.get('name')
            session['email'] = request.form.get('email')
            session['password'] = request.form.get('password')
            users['name'] = request.form.get('name')
            users['email'] = request.form.get('email')
            users['password'] = request.form.get('password')
            userslist.append(users)
            print(userslist)
            return redirect('/dashboard')
        elif request.form['which_form'] == 'login':
            for i in userslist:
                if i['email'] == request.form.get('email') and i['password'] == request.form.get('password'):
                    session['name'] = i['name']
                    session['email'] = request.form.get('email')
                    session['password'] = request.form.get('password')
                    return redirect('/dashboard')
            return redirect('/')

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html",name_on_template=session['name'], email_on_template=session['email'])

@app.route('/added_users')
def added_users():
    return render_template("list.html",userslist=userslist)

@app.route('/destroy_session',methods=['POST','GET'])
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


