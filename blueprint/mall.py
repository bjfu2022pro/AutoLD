from flask import Blueprint, render_template, request
import util_user, util_pay
from flask import Flask
import sys
from flask import g

sys.path.append("..")
import util_algorithmic_mall
import util_calculate_mall
import util_pay

bp = Blueprint("mall", __name__, "/")

dingdan = [
    {
        'dingdanhao': 1000, 'peizhi': '空',
        'leixing': '空', 'shujuji': '空',
        'jine': '空', 'shijian': '空',
        'fukuanren': '大公园'
    }
]


@bp.route('/algorithmic_mall', methods=['get', 'post'])
def algorithmic():
    AL_select = util_algorithmic_mall.find_all()
    return render_template("algorithmic_mall.html", AL_select=AL_select)


@bp.route('/calculate_mall', methods=['get', 'post'])
def calculate():
    calculate_select = util_calculate_mall.find_all()
    calculate_select = util_calculate_mall.find_all()
    return render_template("calculate_mall.html", calculate_select=calculate_select)


@bp.route('/pay')
def confirm():
    return render_template('pay.html', dingdan=dingdan)


@bp.route('/my_bill')
def my_bill():
    email = g.info[1]
    print(email)
    my_bill =util_pay.show_orders(email)
    return render_template('my_bill.html',my_bill=my_bill)
