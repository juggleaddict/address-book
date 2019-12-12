from marshmallow import Schema, fields, pprint
import datetime

class person(object):
    def __init__(self, firstName, lastName, email, phoneNumber, address, city, state):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address
        self.city = city
        self.state = state
        self.created_at = datetime.datetime.now()

class PhoneNumber(fields.Field):
    '''
    custom field for phone numbers
    '''
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        return format(int(value[:-1]), ",").replace(",", "-") + value[-1]

    def _deserialize(self, value, attr, obj, **kwargs):
        return 'TBD'

class personSchema(Schema):
    firstName = fields.Str(required=True)
    lastName = fields.Str(required=True)
    email = fields.Email()
    phoneNumber = PhoneNumber()
    address = fields.Str()
    city = fields.Str()
    state = fields.Str()
    created_at = fields.DateTime(serialize objects using marshmallow)