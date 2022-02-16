from flask import Flask
from flask_restful import Api, Resource
import kmeans_model
import importlib



app = Flask(__name__)

api = Api(app)

class returnjson(Resource):
	def get(self):
		importlib.reload(kmeans_model)
		from kmeans_model import donneesjson
		return donneesjson

api.add_resource(returnjson,'/clustering')


if __name__=='__main__':
	app.run(debug=True)
