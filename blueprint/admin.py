from flask import (Blueprint, jsonify, 
                    render_template, 
                    request, session,
                    redirect, g)
import util_user
import sys 
sys.path.append("..") 
import util_pay


bp = Blueprint("admin", __name__, "/")


@bp.route('/admin_login')
def admin_login():
    pass


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


@bp.route('/admin_algor')
def admin_algor():
    pass