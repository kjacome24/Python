from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    if session.get('total_gold') == None:
        session['total_gold']=0
    if session.get('activities') == None:
        session['activities']= []
    return render_template("index.html")

@app.route('/process_money',methods=['POST'])
def process_money():
    session['building']=request.form.get('building')
    if session['building']=="farm":
        session['earnings'] = random.randint(10,20)
        vart= datetime.datetime.now() 
        session['time'] = vart.strftime("%c")
    elif session['building']=="cave":
        session['earnings'] = random.randint(5,10)
        vart= datetime.datetime.now() 
        session['time'] = vart.strftime("%c")
    elif session['building']=="hause":
        session['earnings'] = random.randint(2,5)
        vart= datetime.datetime.now() 
        session['time'] = vart.strftime("%c")
    elif session['building']=="casino":
        session['earnings'] = random.randint(-50,50)
        vart= datetime.datetime.now() 
        session['time'] = vart.strftime("%c")
    if session['earnings']<0:
        session['validator'] = 'red'
    else:
        session['validator'] = 'green'
    session['total_gold'] += session['earnings']
    message= f"The building choosen was the {session['building']}, and the farmer earned {session['earnings']} coins on {session['time']}"
    session['activities'].insert(0,[session['validator'],message])
    print(session['activities'])
    return redirect('/')


@app.route('/destroy_session',methods=['POST'])
def destroy_session():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)