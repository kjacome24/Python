from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = '123456'


@app.route('/',methods=['POST','GET'])
def main():
    if session.get("number") == None:
        session['number'] = random.randint(1, 100)
        print(session['number'])
        validator=0
        return render_template('index.html',validator=validator)
    else:
        if request.form.get('number') == None or request.form.get('number') =='':
            validator=0
            print("No se ingreso numero")
            return render_template('index.html',validator=validator)
        else:
            if session['number'] == int(request.form.get('number')):
                print("bingo")
                validator=3
                return render_template('index.html',validator=validator)
            elif session['number'] < int(request.form.get('number')):
                print("El numero es mayor")
                validator=2
                return render_template('index.html',validator=validator)
            else:
                print("el numero es menor")
                validator=1
                return render_template('index.html',validator=validator)


@app.route('/destroy_session',methods=['POST','GET'])
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
