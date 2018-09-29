from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app,supports_credentials=True)

from nc_common import panvalidation
from nc_common.panvalidation import panvali, bp_panvali


app.register_blueprint(bp_panvali)


