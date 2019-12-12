import csv
import click
from addressbook.models import ContactsModel

def register_cli_commands(app):

    @app.cli.command("create-tables")
    def create_tables():
        """
        Create tables to suppor the application, this should be performed once unless the database is not persistent
        """
        models = [ContactsModel]
        for model in models:
            if not model.exists():
                model.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    
"""
    @app.cli.command("load_initial_data")
    @click.argument("init_file", type=click.Path(exists=True,resolve_path=True))
    def load_initial_data(*args, **kwargs):
        ''' 
        load a csv into the database
        ''' 
        load_data(show_progres=True, *args, **kwargs)

def load_data(file_to_load):
    #TODO load csv data into model, if using caching, use a provider here
"""

