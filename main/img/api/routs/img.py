from flask_restful import Resource
from main.utils.routs_utils import cjreq
from main.img.model.models import Img
import os
from threading import Thread


class DeleteFileThread(Thread):
    """
    Пример многопоточной загрузки файлов из интернета
    """

    def __init__(self, array):
        Thread.__init__(self)
        self.array_path = array

    def run(self):
        for i in self.array_path:
            try:
                os.remove(i)
            except:
                # поставить логирование
                ...


class GetImg(Resource):
    def get(self, id_user):
        array_img = Img.query.filter_by(id_user=id_user).order_by(Img.id.desc()).all()
        data = []
        for i in array_img:
            data.append(i.to_json)
        return cjreq(status_code=200, data=data)

    def delete(self, id_user):
        array_img = Img.query.filter_by(id_user=id_user).order_by(Img.id.desc()).all()
        path = []
        for i in array_img:
            path.append(i.path)
            i.delete()
        DeleteFileThread(path).start()
        return cjreq(status_code=200, data=True)
