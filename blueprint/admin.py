from flask import (Blueprint, jsonify, 
                    render_template, 
                    request)

import sys 
sys.path.append("..") 
import util_pay
import util_algorithmic_mall
import util_user


bp = Blueprint("admin", __name__, "/")


@bp.route('/admin_login')
def admin_login():
    return render_template("admin_login.html")


@bp.route('/adlog_result', methods=['get', 'post'])
def login_checker():
    """
    登录检查
    """
    ad_name = request.values.get('ad_name')
    password = request.values.get('password')
    result = util_user.finder(ad_name, "name", "admin")
    if result:
        if password == result[0][2]:
            return jsonify({"code": 200})
        else:
            return jsonify({"code": 100})
    else:
        return jsonify({"code": 300})


@bp.route('/admin_bill')
def admin_bill():
    bill=util_pay.show_all_orders()
    return render_template('admin_bill.html',my_bill=bill)


@bp.route('/examine',methods=['post', 'get'])
def examine():
    danhao = request.values.get('danhao')
    util_pay.orders_examine(danhao)
    return jsonify({"od": 400})


@bp.route('/admin_gpu')
def admin_gpu():
    pass


@bp.route('/admin_algor', methods=['post', 'get'])
def admin_algor():
    our_algorithm = util_algorithmic_mall.find_all2()
    return render_template("admin_algor.html", our_algorithm=our_algorithm)


@bp.route('/algorithm_up', methods=['post', 'get'])
def algorithm_up():
    al_id = int(request.values.get('id'))
    result = util_algorithmic_mall.finder(al_id)
    if result[0][3] == 1:
        return jsonify({"code": 400})
    elif result[0][3] == 0:
        util_algorithmic_mall.change_up(al_id)
        return jsonify({"code": 200})


@bp.route('/algorithm_down', methods=['post', 'get'])
def algorithm_down():
    al_id = request.values.get('id')
    result = util_algorithmic_mall.finder(al_id)
    if result[0][3] == 0:
        return jsonify({"code": 400})
    elif result[0][3] == 1:
        util_algorithmic_mall.change_down(al_id)
        return jsonify({"code": 200})

