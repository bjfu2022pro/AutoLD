from flask import (Blueprint, jsonify, 
                    request)
import threading
import sys, os
from algorithm import cls, regress

import datetime

sys.path.append("..") 
import util_instance
import util_dataset


bp = Blueprint("instance", __name__, "/")


@bp.route('/run_instance', methods=['post', 'get'])
def run_instance():
    in_id = request.values.get('id')

    result = util_instance.find_instance_byid(in_id)
    email = result[0][1]
    al_id = result[0][2]
    data = util_dataset.finde_dataset(result[0][3])
    data_path = data[0][4]
    state = result[0][8]
    if state == '0':
        ntime = str(datetime.datetime.now()).split(".")[0]
        ntime = datetime.datetime.strptime(ntime, '%Y-%m-%d %H:%M:%S')
        util_instance.update_info(in_id, ntime, 'begin_time')
        util_instance.update_info(in_id, 1, 'state')

        t0 = threading.Thread()
        if al_id == '1':
            t0 = threading.Thread(target=regress, args=(data_path, email, result[0][0]))  
        elif al_id == '2':
            t0 = threading.Thread(target=cls, args=(data_path, email, result[0][0]))
        t0.start()
        return jsonify({'code':200})
    elif state == '1':
        return jsonify({'code':300})
    elif state == '2':
        return jsonify({'code':400})
    else:
        return jsonify({'code':500})


@bp.route('/model_download', methods=['GET', 'POST'])
def model_download():
    in_id = request.values.get('id')

    result = util_instance.find_instance_byid(in_id)
    email = result[0][1]
    al_id = result[0][2]
    state = result[0][8]

    if state == '2':
        path = f'C:\\model\\{email}\\{al_id}\\model.pkl'
        if os.path.exists(path):
            return jsonify({'code':200, 'path':path})
        else:
            return jsonify({'code':300, 'path':''})
    else:
        return jsonify({'code':300, 'path':''})