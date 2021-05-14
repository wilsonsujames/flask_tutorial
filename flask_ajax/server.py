from flask import Flask,render_template,jsonify,request



app = Flask(__name__)

@app.route('/',methods=[ "GET",'POST'])
def index():
    a={"name":"bob","date":"12月5日","time":"23:30","peopleCount":"10位","phone":"0123456789"}

    Webray_in_flask=[]
    Webray_in_flask.append(a)

    hello_word_in_flask='hello hello hello'

    return render_template('index.html',Webray=Webray_in_flask,hello=hello_word_in_flask)



@app.route('/route_function',methods=[ "GET",'POST'])
def route_function():
    theFood = request.form.get('thefood')
    print(theFood)

    return jsonify({'validate': 'formula success','PayAmount':1500,'Rtnfood':theFood})



@app.route('/dashboard',methods=[ "GET",'POST'])
def dashboard():
    print('dashboard')

    return render_template('dashboard.html')    

@app.route('/base',methods=[ "GET",'POST'])
def base():
    print('base')

    return render_template('base.html')  


@app.route('/testsuper',methods=[ "GET",'POST'])
def testsuper():
    print('testsuper')

    return render_template('testsuper.html')  




if __name__ == "__main__":
    app.run(debug=True,threaded=True,port=5566)    