from flask import Flask,render_template,request
app=Flask(__name__)

import pickle
model=pickle.load(open(r"D:\python_project\new\model.pkl","rb"))

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/outputpage',methods=['POST'])
def outputpage():
    A1=request.form['a1']
    A2=request.form['a2']
    A3=request.form['a3']
    A4=request.form['a4']
    A5=request.form['a5']
    A6=request.form['a6']
    A7=request.form['a7']
    A8=request.form['a8']
    A9=request.form['a9']
    A10=request.form['a10']
    A11=request.form['a11']
    A12=request.form['a12']
    A13=request.form['a13']
    A14=request.form['a14']
    
    test=[[float(A1),float(A2),float(A3),float(A4),float(A5),float(A6),float(A7),float(A8),float(A9),float(A10),float(A11),float(A12),float(A13),float(A14)]]
    result=model.predict(test)
    if(result[0]==0):
        res="The person doesn't have parkinson"
    else:
        res="The person has parkinson"
    return render_template('index.html',y=res)

if __name__=='__main__':
    app.run(debug=True)

