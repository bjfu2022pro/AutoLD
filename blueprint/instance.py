from flask import (Blueprint, jsonify, 
                    render_template, 
                    request, session,
                    redirect, g)
import threading
import sys
from algorithm import cls, regress

import datetime

sys.path.append("..") 
import util_instance
import util_dataset


bp = Blueprint("instance", __name__, "/")


@bp.route('/run_instance', methods=['post', 'get'])
def run_instance():
    in_id = request.args.get('id')

    result = util_instance.find_instance_byid(in_id)
    email = result[0][1]
    al_id = result[0][2]
    data = util_dataset.finde_dataset(result[0][3])
    data_path = data[0][4]

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
    return redirect('/my_instance')

