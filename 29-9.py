from flask import Flask
from flask_restful import Resource, Api

data = [132,2555,25121,21321,1231231]

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self, index):
        print(index)
   
        x = data[index]
        return {'data': x}

api.add_resource(HelloWorld, '/hello/<int:index>')
if __name__ == '__main__':
    app.run(debug=True)