from flask import (Blueprint, jsonify, 
                    render_template, 
                    request, session,
                    redirect, g)
import threading
import sys
import algorithm

import datetime

sys.path.append("..") 
import util_instance
import util_dataset


bp = Blueprint("instance", __name__, "/")


@bp.route('/run_instance', methods=['post', 'get'])
def run_instance():
    in_id = request.args.get('id')
    ntime = str(datetime.datetime.now()).split(".")[0]
    ntime = datetime.datetime.strptime(ntime, '%Y-%m-%d %H:%M:%S')
    util_instance.update_info(in_id, ntime, 'begin_time')
    util_instance.update_info(in_id, 2, 'state')
    result = util_instance.find_instance_byid(in_id)
    email = result[0][1]
    al_id = result[0][2]
    data_path = util_dataset.finde_dataset(result[0][3])
    if al_id == 1:
        t0 = threading.Thread(target=algorithm.regression.regress, args=(data_path, email, result[0][0]))
        t0.start()
    elif al_id == 2:
        t0 = threading.Thread(target=algorithm.cn.cls, args=(data_path, email, result[0][0]))
        t0.start()
    return redirect('/my_instance')

