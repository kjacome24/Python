from flask import Flask, render_template, request, redirect
app = Flask(__name__)


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
        return redirect('/added_users')
    else:
        return redirect('/added_users')

@app.route('/added_users')
def added_users():
    return render_template("list.html",userslist=userslist)

if __name__ == "__main__":
    app.run(debug=True)


