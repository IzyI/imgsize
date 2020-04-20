from main.database import db, CRUDMixin
from passlib.apps import custom_app_context as pwd_context
from flask import current_app
from datetime import datetime


class User(CRUDMixin, db.Model):
    __tablename__ = 'user_is'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(255))
    date_create = db.Column(db.DateTime(), default=datetime.now())

    @property
    def to_json(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'date_create': self.date_create.strftime("%A, %d. %B %Y %I:%M%p"),
        }

    def check_encrypted_password(self, p):
        return pwd_context.verify(p + current_app.config['SALT'], self.password)

    @classmethod
    def encrypt_password(cls, password):
        return pwd_context.encrypt(password + current_app.config['SALT'])

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def __repr__(self):
        return f"<User-ID:{self.id} NAME: {self.name} >"
