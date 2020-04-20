from flask import make_response
import json
from flask import current_app as app


def cpreqerror(par_dict, check_val=False):
    for i in par_dict:
        if par_dict[i] == check_val:
            return "Нет параметра: " + str(i)
        try:
            if len(par_dict[i]) < 2:
                return f"Параметр {str(i)} Слишком короткий"
        except TypeError:
            ...
    else:
        return False


def dict_check(d, check_val):
    """возвращает пустой dict если  все значения равняются check_val
    """
    return dict((k, v) for k, v in d.items() if v != check_val)


def cjreq(data=False, meta=False, error_code=0, err_msg=False, status_code=200):
    """
    Формирует JSON массив в для АПИ
    """
    json_data = {}
    if data is False or data is None:
        json_data["data"] = data
    if meta:
        json_data["meta"] = meta
    if error_code >= 2000:
        json_data["error-code"] = int(error_code)
    if err_msg:
        json_data["error-message"] = err_msg
    json_data = json.dumps(json_data, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
    m = make_response(json_data, status_code, )
    m.mimetype = 'application/json'
    return m


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
