from flask import Blueprint, render_template, request, jsonify

from flask import Flask
import sys
sys.path.append("..")
import util_algorithmic_mall
import util_calculate_mall
import util_cache


bp = Blueprint("mall", __name__, "/")


dingdan = [
    {
        'dingdanhao': '10000', 'peizhi': 'j',
        'leixing': 'i', 'shujuji': 'n',
        'jine': '11', 'shijian': '11',
        'fukuanren': '金旭光'
    }
]


@bp.route('/algorithmic_mall', methods=['get', 'post'])
def algorithmic():
    AL_select=util_algorithmic_mall.find_all()
    return render_template("algorithmic_mall.html", AL_select=AL_select)


@bp.route('/calculate_mall', methods=['get', 'post'])
def calculate():
    calculate_select=util_calculate_mall.find_all()
    calculate_select=util_calculate_mall.find_all()
    return render_template("calculate_mall.html",calculate_select=calculate_select)

@bp.route('/cache', methods=['get', 'post'])
def cache():
    # title = request.values.get("title")
    # introduce = request.values.get("introduce")
    # print(title,introduce)
    # util_cache.add(title=title,introduce=introduce)
    # util_algorithmic_mall.find_all()
    id = int(request.values.get("id"))
    print(id)
    details = util_algorithmic_mall.finder(id)
    print(details)
    util_cache.add(details[0][1], details[0][2])
    return jsonify({"code": 200})


@bp.route('/algorithmic_details', methods=['get', 'post'])
def details():
    details = util_cache.find_all()
    print(details)
    util_cache.delete(details[0][0])
    return render_template("algorithmic_details.html", details=details)


@bp.route('/pay')
def confirm():
    return render_template('pay.html',dingdan=dingdan)