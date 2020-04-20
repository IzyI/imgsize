from flask import request
from flask_restful import Resource
from main.utils.routs_utils import cjreq, allowed_file
from flask import current_app as app
from datetime import datetime
import os
from main.img.model.models import ImgUserCongig, Img
import subprocess


class UploadImg(Resource):

    def post(self, id_user):
        files_array = request.files
        if len(files_array) == 0:
            return cjreq(status_code=400, error_code=2100, err_msg='No file part in the request')
        iuc = ImgUserCongig.query.filter_by(id_user=id_user).first()
        if not iuc:
            return cjreq(error_code=2100, err_msg="Такого юзера не существует")
        count = iuc.count
        limit = iuc.limit
        try:
            lastidfileid = Img.query.order_by(Img.id.desc()).first().id
        except AttributeError:
            lastidfileid = 0
        for f in files_array:
            file = files_array[f]
            if not (file and allowed_file(file.filename)):
                return cjreq(status_code=400, error_code=2100, err_msg='Разрешены разрешения png, jpg, jpeg')
            if count >= limit:
                return cjreq(error_code=2100, err_msg="У вас закончился лимит по изображениям")
            filename = file.filename
            try:
                type_img = filename.split('.')[-1]
            except:
                return cjreq(error_code=2100, err_msg="В файле нет расширения  .png, .jpg, .jpeg")
            now_date = datetime.now().strftime("%d%b_%H_%M_%S")
            path_tmp = os.path.join(app.config['UPLOAD_FOLDER'],
                                    f"imgsize_{lastidfileid}_{id_user}_{now_date}_tmp.{type_img}")
            path = os.path.join(app.config['UPLOAD_FOLDER'], f"imgsize_{lastidfileid}_{id_user}_{now_date}.{type_img}")
            file.save(path_tmp)

            s_call = subprocess.call(
                f"cjpeg -quality 60 -optimize -progressive -outfile {path} {path_tmp}".split(" "))
            if s_call != 0:
                return cjreq(error_code=2100, err_msg="Не смог сжать файл")
            old_size = float("{0:.2f}".format(os.path.getsize(path_tmp) / 1024))
            new_size = float("{0:.2f}".format(os.path.getsize(path) / 1024))
            os.remove(path_tmp)
            imgc = Img.create(
                id_user=id_user,
                path=path,
                name=filename,
                old_size=old_size,
                new_size=new_size
            )
            count += 1
            lastidfileid = imgc.id
            iuc.update(
                count=count
            )

        return cjreq(status_code=200, data='File successfully uploaded')
