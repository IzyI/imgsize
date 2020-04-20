from main.database import db, CRUDMixin
from datetime import datetime


class Img(CRUDMixin, db.Model):
    __tablename__ = 'img_is'
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String())
    name = db.Column(db.String())
    old_size = db.Column(db.String())
    new_size = db.Column(db.String())
    id_user = db.Column(db.Integer, db.ForeignKey('user_is.id', ondelete='CASCADE'))
    date_create = db.Column(db.DateTime(), default=datetime.now())

    @property
    def to_json(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'path': self.path.split("main")[-1],
            'name': self.name,
            'old_size': self.old_size,
            'new_size': self.new_size,
            "id_user": self.id_user,
            "date_create": self.date_create.strftime("%d.%m.%Y %H:%M:%S"),

        }

    def __repr__(self):
        return f"<Img-ID:{self.id} NAME: {self.name} >"


class ImgUserCongig(CRUDMixin, db.Model):
    __tablename__ = 'img_user_config_is'
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user_is.id', ondelete='CASCADE'))
    count = db.Column(db.Integer, default=0)
    limit = db.Column(db.Integer, default=20)

    @property
    def to_json(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'id_user': self.id_user,
            'count': self.count,
            "limit": self.limit
        }

    def __repr__(self):
        return f"<Img-User-Config-ID:{self.id} id_user: {self.id_user} >"
