from flask_restful import Resource
import os
from main.img.model.models import Img
from flask import make_response
import zipfile
import io
import time


class ZipImg(Resource):
    def get(self, id_user):
        fileobj = io.BytesIO()
        img_array = Img.query.filter_by(id_user=id_user).all()
        with zipfile.ZipFile(fileobj, 'w') as zip_file:
            for file in img_array:
                base_path = file.path
                zip_info = zipfile.ZipInfo(base_path.split("/")[-1])
                zip_info.date_time = time.localtime(time.time())[:6]
                zip_info.compress_type = zipfile.ZIP_DEFLATED
                with open(base_path, 'rb') as fd:
                    zip_file.writestr(zip_info, fd.read())
        fileobj.seek(0)
        response = make_response(fileobj.read())
        response.headers.set('Content-Type', 'zip')
        response.headers.set('Content-Disposition', 'attachment', filename='%s.zip' % os.path.basename(base_path))
        return response
