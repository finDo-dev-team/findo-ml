from flask import Flask
from flask_restful import Api, Resource
from kmeans_model import donneesjson

app = Flask(__name__)

api = Api(app)

class returnjson(Resource):
	def get(self):
		return donneesjson

api.add_resource(returnjson,'/clustering')


if __name__=='__main__':
	app.run(debug=True)
