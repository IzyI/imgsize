from main import config as cfg
from main.extensions import migrate, api, jwtm
from main.database import db
from flask import Flask, request, send_file
from flask_jwt_extended import get_jwt_identity, verify_fresh_jwt_in_request
from flask_cors import CORS
from main.img.api import apiimg
from main.commands import create_db, drop_db, recreate_db, create_user, delete_user
from main.dryRoutes import authRoute
from main.utils.routs_utils import cjreq
import time


def create_app(config=cfg.base_config, testing=False):
    """Returns an initialized Flask application."""
    node = Flask(__name__, template_folder="templates")
    node.config.from_object(config)
    node.config['TESTING'] = testing
    if node.config['CORS']:
        print(' * CORS')
        CORS(node)

    @node.route('/ping', methods=['GET'])
    def ping():
        time.sleep(5)
        return cjreq(data="pong", status_code=200)

    @node.before_request
    def before_request():
        req = request.path.split("/")
        if req[1] == 'user':
            if request.method == 'OPTIONS':
                return "", 200
            verify_fresh_jwt_in_request()
            current_user = get_jwt_identity()
            try:
                int(req[2])
            except IndexError:
                return cjreq(error_code=2100, err_msg="Не передал id_users")
            if int(current_user[0]) != int(req[2]):
                return cjreq(error_code=2100,
                             err_msg="Несовпадает id jwt и id url: " + str(current_user[0]) + "!=" + str(req[2]),
                             status_code=403)

            print("USER")
        elif req[1] == 'auth':
            print("auth")
        elif req[1] == 'ping':
            print("ping")

        else:
            print("ALL")
            return send_file(f'{str(node.root_path)[:-4]}front/dist/index.html')

    register_extensions(node)
    register_routs(node)
    register_blueprints(node)
    register_commands(node)

    return node


def register_extensions(node):
    """Register extensions with the Flask application."""
    db.init_app(node)
    migrate.init_app(node, db)
    api.init_app(node)
    jwtm.init_app(node)


def register_routs(node):
    ...
    node.add_url_rule("/auth", view_func=authRoute.Auth.as_view('auth'))


def register_blueprints(node):
    """Register blueprints with the Flask application."""
    ...
    node.register_blueprint(apiimg, url_prefix='/user')


def register_commands(app):
    """Register custom commands for the Flask CLI."""
    comand_list = [create_db, drop_db, recreate_db, create_user, delete_user]
    for command in comand_list:
        app.cli.add_command(command)
