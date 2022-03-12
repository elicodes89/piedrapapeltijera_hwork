from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from controllers import controller

if __name__ == '__main__':
    app.run(debug=True)