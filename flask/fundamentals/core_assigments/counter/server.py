from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '123456'

counter = [0]

@app.route('/',methods=['POST','GET'])
def main():
    if session.get("counter") == None:
        session['counter'] = 0
    else:
        session['counter'] += 1
    print(session['counter'])
    return render_template('index.html',times=session['counter'] )

@app.route('/plus2',methods=['POST','GET'])
def plus2():
    session['counter'] += 1
    return redirect('/')




@app.route('/destroy_session',methods=['POST','GET'])
def logout():
    # Esta función será encargada de eliminar/liberar la sesión activa
    # forma correcta de liberar sesión
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
