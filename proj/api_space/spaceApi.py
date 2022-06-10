
# python3 - space_api.py
# This is a test run for restful api's using Flask 
# This api wil be in charge of trasnfering the launch data
# for my space launch app 
# run this code with
# FLASK_APP=spaceApi.py flask run 

from flask import Flask, jsonify

app = Flask(__name__)

@app.before_request
def before():
    print("this is executed before each request")

@app.route('/', methods=['GET', 'POST'])
def space_launch(): 
    return jsonify({'name':'Jimit',
                    'address': 'India'})

if __name__ == "-__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
