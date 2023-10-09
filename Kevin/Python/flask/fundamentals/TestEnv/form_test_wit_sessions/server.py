from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '123456'

userslist = []
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users',methods=['POST','GET'])
def create_user():
    if request.method == "POST":
        users = {}
        print("Got Post Info")
        users['name'] = request.form.get('name')
        users['email'] = request.form.get('email')
        userslist.append(users)
        # print(request.form)
        print(userslist)
        session['username'] = request.form['name']
        session['useremail'] = request.form['email']
        return redirect('/added_users')
    else:
        return redirect('/added_users')

@app.route('/added_users')
def added_users():
    return render_template("list.html",name_on_template=session['username'], email_on_template=session['useremail'])

if __name__ == "__main__":
    app.run(debug=True)


