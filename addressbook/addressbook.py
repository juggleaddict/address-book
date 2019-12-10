from flask import Flask

from addressbook.routes import api
from addressbook._cli import register_cli_commands

app = Flask(__name__)
api.init_app(app)
register_cli_commands(app)

if __name__ == '__main__':
    app.run(debug=True)