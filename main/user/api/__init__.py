from flask import Blueprint
from flask_restful import Api

apiuser = Blueprint('apiuser', __name__)
init_api = Api(apiuser)

from . import routesManager
