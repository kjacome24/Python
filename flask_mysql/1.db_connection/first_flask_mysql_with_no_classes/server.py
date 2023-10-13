from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL


app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    mysql = connectToMySQL('first_flask')
    friends = mysql.query_db('select * from friends;')
    print(friends)
    return render_template("index.html",friends=friends)

@app.route('/process',methods=['POST'])
def create_user():
    pass

if __name__ == "__main__":
    app.run(debug=True)