from flask.cli import with_appcontext
import click
from main.database import db
from main.user.model.models import User
from main.img.model.models import ImgUserCongig


@click.command()
@with_appcontext
@click.option('-n', required=True, type=str, help='name')
@click.option('-p', required=True, type=str, help='password')
def create_user(n, p):
    """Создать юзера """
    u = User.get_by_name(n)
    if u:
        u = u.update(password=User.encrypt_password(p))
        print("Обновил: ", u)
    else:
        u = User.create(name=n, password=User.encrypt_password(p))
        ImgUserCongig.create(id_user=u.id)
        print("Создал: ", u)


@click.command()
@with_appcontext
@click.option('-n', required=True, type=str, help='name')
def delete_user(n):
    """Удалить юзера """
    u = User.get_by_name(n)
    if u:
        u.delete()
        print("Удалил: ", u)
    else:
        print("Нет такого User")


#
# @click.command()
# @with_appcontext
# def populate_db():
#     #     """Заполнить тестовыми данными таблицы."""
#     fake = Faker("ru_RU")


@click.command()
@with_appcontext
def create_db():
    """Создать все таблицы"""
    db.create_all()


@click.command()
@with_appcontext
def drop_db():
    """Удалить все таблицы."""
    if click.confirm('Ты уверен?', abort=True):
        db.drop_all()


@click.command()
@with_appcontext
def recreate_db():
    """Удалить а потом создать все таблицы"""
    if click.confirm('Ты уверен?', abort=True):
        db.drop_all()
        db.create_all()
