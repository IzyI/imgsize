import os
from main.user.model.models import User
from main.img.model.models import Img, ImgUserCongig
from serve import node


def main():
    path = "/root/imgsize/main/uploads/"
    with node.app_context():
        user_array = User.query.all()
        for u in user_array:
            id_user = u.id
            img_array = Img.query.filter_by(id_user=id_user).all()
            for i in img_array:
                try:
                    img_name = i.path.split('/')[-1]
                    os.remove(f"{path}{img_name}")
                except:
                    # поставить логирование
                    ...
                i.delete()
            iuc = ImgUserCongig.query.filter_by(id_user=id_user).first()
            iuc.count = 0
            iuc.save()


if __name__ == '__main__':
    main()
