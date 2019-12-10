import csv
import click
from addressbook.models import AddressBookModel

def register_cli_commands(app):

    @app.cli.command("create-tables")
    def create_tables():
        models = [AddressBookModel]
        for model in models:
            if not model.exists():
                model.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)


