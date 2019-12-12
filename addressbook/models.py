from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class ContactsModel(Model):
    class Meta:
        table_name = "contacts"
        host = "http://localhost:8000"
    first_name = UnicodeAttribute(hash_key=True)
    last_name = UnicodeAttribute(range_key=True)
