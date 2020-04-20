from flask import request
from flask_jwt_extended import create_access_token
from flask.views import MethodView
from main.user.model.models import User
from main.utils.routs_utils import cpreqerror, cjreq


class Auth(MethodView):

    def get(self):
        name = request.args.get('name', False)
        password = request.args.get('password', False)
        error2011 = cpreqerror({"password": password, "name": name})
        if error2011:
            return cjreq(error_code=2011, err_msg=error2011)

        name = str(name).replace(" ", '')
        password = str(password).replace(" ", '')

        user = User.get_by_name(name)

        if user:
            if user.check_encrypted_password(password):
                access_token = create_access_token(identity=[user.id], fresh=True)
                return cjreq(data=user.to_json, meta={"access_token": access_token})
            else:
                return cjreq(status_code=403, err_msg="Немогу нечего сказать")
        else:
            return cjreq(status_code=404, err_msg='Аккаунта не существует')
