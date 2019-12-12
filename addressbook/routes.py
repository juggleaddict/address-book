from flask import Flask, request
from flask_restplus import Api, Resource
import json

from addressbook.models import ContactsModel

api = Api()

@api.route('/api/v1/contacts')
class ContactsResource(Resource):

    def get(self):
        all_data = [x for x in ContactsModel.scan()]
        print(all_data)
        print(all_data[0].keys)
        return None

    def post(self):
        data = request.form['data']
        new_contact = ContactsModel(data)
        new_contact.save()

