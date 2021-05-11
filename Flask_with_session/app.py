from flask import Flask, session, redirect, url_for, request,jsonify
import os 

app = Flask(__name__)

app.secret_key = os.urandom(20)


@app.route('/')
def index():
    session['username'] ='bob'
    session['weight'] ='60kg'
    session['height'] ='172cm'

    return jsonify({'status':'using session success'})

@app.route('/getinfo')
def getinfo():
    print(session)
    # 這裡可以發現session資料為字典型態
    username=session.get('username')
    weight=session.get('weight')
    height=session.get('height') 
    return jsonify({'username':username,'weight':weight,'height':height})


if __name__ == '__main__':
    app.run(debug=True, port=8591)