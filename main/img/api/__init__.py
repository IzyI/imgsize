from flask import Blueprint
from flask_restful import Api

apiimg = Blueprint('apiimg', __name__)
init_api = Api(apiimg)

from . import routesManager
