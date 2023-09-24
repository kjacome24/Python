from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("playground.html",num=0)

@app.route('/play')
def play():
    return render_template("playground.html",num=3,coloru="#9fc5f8")

@app.route('/play/<int:num>')
def play2(num):
    return render_template("playground.html",num=num,coloru="#9fc5f8")

@app.route('/play/<int:num>/<string:coloru>')
def play3(num,coloru):
    return render_template("playground.html",num=num,coloru=coloru)

if __name__=="__main__": ###This function basically makes sure that the module is being executed directly and not from another file. 
    app.run(debug=True)