from flask import Flask,render_template

app = Flask(__name__)


#########################1
@app.route('/')
def main():
    list_rows = []
    x=0
    for i in range(8):
        list_rows.append(x)
        if x<=0:
            x+=1
        else:
            x-=1
    return render_template("main.html",columns=8,rows=8,list_rows=list_rows,list_columns=list_rows)


################2
@app.route('/<int:rows>')
def main2(rows):
    list_rows = []
    list_columns = []
    x=0
    y=0
    for i in range(rows):
        list_rows.append(x)
        if x<=0:
            x+=1
        else:
            x-=1
    for i in range(8):
        list_columns.append(y)
        if y<=0:
            y+=1
        else:
            y-=1
    return render_template("main.html",columns=rows,rows=8,list_rows=list_rows,list_columns=list_columns)

###################3

@app.route('/<int:rows>/<int:columns>')
def main3(rows,columns):
    list_rows = []
    list_columns = []
    x=0
    y=0
    for i in range(rows):
        list_rows.append(x)
        if x<=0:
            x+=1
        else:
            x-=1
    for i in range(columns):
        list_columns.append(y)
        if y<=0:
            y+=1
        else:
            y-=1
    return render_template("main.html",columns=rows,rows=columns,list_rows=list_rows,list_columns=list_columns)

##########################4

@app.route('/<int:rows>/<int:columns>/<string:colorn>')
def main4(rows,columns,colorn):
    list_rows = []
    list_columns = []
    x=0
    y=0
    for i in range(rows):
        list_rows.append(x)
        if x<=0:
            x+=1
        else:
            x-=1
    for i in range(columns):
        list_columns.append(y)
        if y<=0:
            y+=1
        else:
            y-=1
    return render_template("main.html",columns=rows,rows=columns,list_rows=list_rows,list_columns=list_columns,colorn=colorn)

###########################5 

@app.route('/<int:rows>/<int:columns>/<string:colorn>/<string:colorn2>')
def main5(rows,columns,colorn,colorn2):
    list_rows = []
    list_columns = []
    x=0
    y=0
    for i in range(rows):
        list_rows.append(x)
        if x<=0:
            x+=1
        else:
            x-=1
    for i in range(columns):
        list_columns.append(y)
        if y<=0:
            y+=1
        else:
            y-=1
    return render_template("main.html",columns=rows,rows=columns,list_rows=list_rows,list_columns=list_columns,colorn=colorn,colorn2=colorn2)


if __name__ == "__main__": 
    app.run(debug=True) 

