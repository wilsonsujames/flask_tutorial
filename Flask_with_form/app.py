from flask import Flask, redirect, url_for, render_template,request

from flask import Flask,render_template,jsonify

app = Flask(__name__)

@app.route('/',methods=[ "GET",'POST'])
def index():


    return render_template('index.html')


@app.route('/login_process',methods=[ "GET",'POST'])
def login_process_fun():
    print(request)
    print(request.form)
    print(request.form.get('inputEmail'))
    email=request.form.get('inputEmail')
    print(request.form.get('inputpass'))
    psword=request.form.get('inputpass')

    return render_template('loginSuccess.html',email=email,psword=psword)



if __name__ == "__main__":
    app.run(debug=True,threaded=True,port=5566)    