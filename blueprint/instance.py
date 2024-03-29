
from flask import (Blueprint, jsonify,  request)
import threading
import sys, os
from algorithm import cls, regress

import datetime

sys.path.append("..") 
import util_instance, util_dataset
import util_pay, util_account, util_ca_number


bp = Blueprint("instance", __name__, "/")


@bp.route('/run_instance', methods=['post', 'get'])
def run_instance():
    in_id = request.values.get('id')

    result = util_instance.find_instance_byid(in_id)
    email = result[0][1]
    al_id = result[0][2]
    od_id = result[0][5]
    cal_id = result[0][4]
    cal_result = util_ca_number.finder(cal_id, 'id')
    cal_name = cal_result[0][1]
    data = util_dataset.finde_dataset(result[0][3])
    data_path = data[0][4]
    state = result[0][8]
    if state == '0':
        ntime = str(datetime.datetime.now()).split(".")[0]
        ntime = datetime.datetime.strptime(ntime, '%Y-%m-%d %H:%M:%S')
        util_instance.update_info(in_id, ntime, 'begin_time')
        util_instance.update_info(in_id, 1, 'state')
        util_account.add_begin(ntime, in_id, email)
        util_pay.upd_state(od_id)
        t0 = threading.Thread()
        if al_id == '1':
            t0 = threading.Thread(target=regress, args=(data_path, email, result[0][0], cal_name))
        elif al_id == '2':
            t0 = threading.Thread(target=cls, args=(data_path, email, result[0][0], cal_name))
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
    in_id = result[0][0]
    state = result[0][8]

    if state == '2':
        path = f'static\\model\\{email}\\{in_id}\\model.pkl'
        if os.path.exists(path):
            print(path,'存在')
            return jsonify({'code':200, 'path':path})
        else:
            print(path,'不存在')
            return jsonify({'code':300, 'path':''})
    else:
        print('meihaone')
        return jsonify({'code':300, 'path':''})