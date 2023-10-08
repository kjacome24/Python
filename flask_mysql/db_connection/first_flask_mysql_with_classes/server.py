from flask import Flask, render_template, request, redirect, session
from friend import Friend


app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html",friends=friends)

@app.route('/process',methods=['POST'])
def create_user():
    pass

if __name__ == "__main__":
    app.run(debug=True)