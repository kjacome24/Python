from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = '123456'
userslist = []


###Root were we render de main and provided values. 
@app.route('/',methods=['POST','GET'])
def main():
    if session.get("number") == None or session['validator'] == None or session['counter'] == 0:
        session['number'] = random.randint(1, 100)
        print(session['number'])
        session['validator'] = 0
        session['counter'] = 0
        return render_template('index.html',validator=session['validator'],xtimes=session['counter'],winner=session['number'])
    else:
        return render_template('index.html',validator=session['validator'],xtimes=session['counter'],winner=session['number'])


################path were we do the logic for the counter and validator
@app.route('/function',methods=['POST'])
def function():
    if session['counter'] == 4:
        session['validator'] =4
        session['counter'] += 1 
        return redirect('/')
    if request.form.get('number') == None or request.form.get('number') =='':
        session['validator'] =0
        print("No se ingreso numero")
        return redirect('/')
    else:
        if session['number'] == int(request.form.get('number')):
            print("bingo")
            session['validator'] =3
            session['counter'] += 1 
            return redirect('/')
        elif session['number'] < int(request.form.get('number')):
            print("El numero es mayor")
            session['counter'] += 1 
            session['validator']=2
            return redirect('/')
        else:
            print("el numero es menor")
            session['counter'] += 1 
            session['validator']=1
            return redirect('/')

###############Logic to storage user's info
@app.route('/users',methods=['POST'])
def create_user():
    users = {}
    print("Got Post Info")
    users['user'] = request.form.get('user')
    users['Attempts'] = session['counter']
    userslist.append(users)
    print(userslist)
    return redirect('/added_users')

####Function were we render list page and sort by the number of attempts. 
@app.route('/added_users')
def added_users():
    size = len(userslist)-1
    for ind in range(0,size): 
        print(f"Original loop {ind}--------------------------")
        min_index = ind
        for j in userslist[0:min_index+1]: 
            if userslist[min_index+1]['Attempts'] < j['Attempts']:
                print("True")
                x= userslist.pop(min_index+1)
                userslist.insert(min_index,x)
                min_index = min_index -1
            else:
                print("False")
    return render_template("list.html",userslist=userslist)


############Clear session
@app.route('/destroy_session',methods=['POST','GET'])
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
