from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class status(resource): 
    def get(self): 
        try: 
            return{'data': 'Api running'}
        except:
            return {'data', error}

       
api.add_resource(status '/')

if __name__ == '__main__': 
    app.run(debug=True)
