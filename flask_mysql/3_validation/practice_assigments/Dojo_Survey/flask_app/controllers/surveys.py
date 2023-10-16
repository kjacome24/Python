from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.survey import Survey


@app.route('/',methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def create_user():
    print(request.form)
    if not Survey.validate_survey(request.form):
        return redirect('/')
    session['authorization'] = request.form.get('authorization')
    session['name'] = request.form.get('name')
    session['GenderIdentity'] = request.form.get('GenderIdentity')
    session['location'] = request.form.get('location')
    session['favoritelanguage'] = request.form.get('favoritelanguage')
    session['Comments'] = request.form.get('Comments')
    data = {
        "name" : request.form['name'],
        "gender_identity" : request.form['GenderIdentity'],
        "location" : request.form['location'],
        "favorite_language" : request.form['favoritelanguage'],
        "comments" : request.form['Comments']
    }
    Survey.new_survey(data)
    return redirect('/result')

@app.route('/result')
def added_users():
    return render_template("Submitted_info.html",name=session['name'],genderidentity=session['GenderIdentity'], location=session['location'],favoritelanguage=session['favoritelanguage'],comments=session['Comments'])