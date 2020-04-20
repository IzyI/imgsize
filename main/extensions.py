from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager

# миграции
migrate = Migrate()
# restfull
api = Api()
jwtm = JWTManager()
