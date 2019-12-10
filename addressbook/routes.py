from flask import Flask
from flask_restplus import Api, Resource

api = Api()

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
