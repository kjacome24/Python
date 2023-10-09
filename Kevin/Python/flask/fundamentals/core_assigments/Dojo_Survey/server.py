from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '123456'

@app.route('/',methods=['POST','GET'])
def index():

    return render_template("index.html")

@app.route('/process',methods=['POST'])
def create_user():
    print(request.form)
    if request.form.get('name') == '':
        return redirect('/')
    if request.form.get('authorization') == None:
        return redirect('/')
    if request.form.get('GenderIdentity') == None:
        return redirect('/')
    session['authorization'] = request.form['authorization']
    session['name'] = request.form['name']
    session['GenderIdentity'] = request.form['GenderIdentity']
    session['location'] = request.form['location']
    session['favoritelanguage'] = request.form['favoritelanguage']
    session['Comments'] = request.form['Comments']
    return redirect('/result')

@app.route('/result')
def added_users():
    return render_template("Submitted_info.html",name=session['name'],genderidentity=session['GenderIdentity'], location=session['location'],favoritelanguage=session['favoritelanguage'],comments=session['Comments'])

if __name__ == "__main__":
    app.run(debug=True)
