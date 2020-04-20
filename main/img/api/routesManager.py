from . import init_api
from main.img.api.routs.upload import UploadImg
from main.img.api.routs.img import GetImg
from main.img.api.routs.zip import ZipImg

init_api.add_resource(GetImg, '/<int:id_user>/img')
init_api.add_resource(ZipImg, '/<int:id_user>/img/zip')
init_api.add_resource(UploadImg, '/<int:id_user>/img/upload')
