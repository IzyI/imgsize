import os


class base_config(object):
    SITE_NAME = os.environ.get('APP_NAME', 'IMG SIZE ')

    UPLOAD_FOLDER = os.path.abspath(os.curdir) + '/main/uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5433)
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'antdbuser')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'viva_ldiF56')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'antdb')

    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        POSTGRES_USER,
        POSTGRES_PASSWORD,
        POSTGRES_HOST,
        POSTGRES_PORT,
        POSTGRES_DB
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CORS = True

    JWT_SECRET_KEY = "x5u4rU$REJfdf6G^Fvb"
    JWT_ACCESS_TOKEN_EXPIRES = 604800
    SALT = "348g465hbgr%^&*3d4v__&"
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mcs9#tjrs34a4u5sud6fyfu$@eefel$rq^z')

    LISTSIZE = 20
