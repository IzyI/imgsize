# -*- coding: utf-8 -*-
from main import create_app
from main.user.model.models import User
from main.img.model.models import Img
from main.database import db
from sqlalchemy import func
from pprint import pprint
from sqlalchemy.orm import aliased
from sqlalchemy import and_, or_, case
from datetime import datetime, timedelta

node = create_app()


# Декоратор app.shell_context_processor регистрирует функцию как функцию контекста оболочки. Когда запускается команда
# flask shell, она будет вызывать эту функцию и регистрировать элементы, возвращаемые ею в сеансе оболочки.
@node.shell_context_processor
def make_shell_context():
    # return {}
    return {
        'datetime': datetime,
        'timedelta': timedelta,
        'aliased': aliased,
        'and_': and_,
        'or_': or_,
        'case': case,
        'pprint': pprint,
        'func': func,
        'db': db,
        'User': User,
        "Img": Img
    }
