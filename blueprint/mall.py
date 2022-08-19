from flask import Blueprint, render_template, request, redirect, session


import sys
from flask import g, jsonify

sys.path.append("..")
import util_algorithmic_mall
import util_calculate_mall
import util_instance
import util_pay
import util_details_cache
import util_cache
import util_data

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
    # AL_select = util_algorithmic_mall.find_all()
    AL_select = util_details_cache.find_all()
    print("AL_select", AL_select)
    if len(AL_select) == 1:
        util_details_cache.delete(AL_select[0][1])
    elif len(AL_select) == 2:
        util_details_cache.delete(AL_select[0][1])
        util_details_cache.delete(AL_select[1][1])
    # else:
    #     util_details_cache.delete(AL_select[0][1])
    #     util_details_cache.delete(AL_select[1][1])
    #     util_details_cache.delete(AL_select[2][1])
    return render_template("algorithmic_mall.html", AL_select=AL_select)


@bp.route('/calculate_mall', methods=['get', 'post'])
def calculate():
    calculate_select = util_calculate_mall.find_all()
    return render_template("calculate_mall.html", calculate_select=calculate_select)


@bp.route('/pay')
def confirm():
    return render_template('pay.html', dingdan=dingdan)





@bp.route('/my_bill')
def my_bill():
    email = g.info[1]
    my_bill = util_pay.show_orders(email)
    return render_template('my_bill.html', my_bill=my_bill)


@bp.route('/expt', methods=['get', 'post'])
def expt():
    email = g.info[1]
    lujing = util_pay.daochu(email)
    return jsonify({"od": 400, "lujing": lujing})


@bp.route('/cache2', methods=['get', 'post'])
def cache2():
    sort = int(request.values.get("sort"))
    print(sort)
    sorting = util_details_cache.finder(sort)
    print("sorting", sorting)
    if len(sorting) == 1:
        util_details_cache.add(sorting[0][0], sorting[0][1], sorting[0][2],sorting[0][3],sorting[0][5])
    elif len(sorting) == 2:
        util_details_cache.add(sorting[0][0], sorting[0][1], sorting[0][2],sorting[0][3],sorting[0][5])
        util_details_cache.add(sorting[1][0], sorting[1][1], sorting[1][2],sorting[1][3],sorting[0][5])
    else:
        util_details_cache.add(sorting[0][0], sorting[0][1], sorting[0][2],sorting[0][3],sorting[0][5])
        util_details_cache.add(sorting[1][0], sorting[1][1], sorting[1][2],sorting[1][3],sorting[0][5])
        util_details_cache.add(sorting[2][0], sorting[2][1], sorting[2][2],sorting[2][3],sorting[0][5])
    return jsonify({"code": 200})



@bp.route('/algorithmic_details', methods=['get', 'post'])
def details():
    details = util_cache.find_all()
    if details:
        session['algorithmic']=details[0][0]
        algorithmic=session.get('algorithmic')
        print("algorithmic",algorithmic)
    else :
        pass
    print("details", details)
    datas = util_data.finder(details[0][2])
    print("datas", datas)
    util_cache.delete(details[0][0])
    return render_template("algorithmic_details.html", details=details, datas=datas)



@bp.route('/cache', methods=['get', 'post'])
def cache():
    id = int(request.values.get("id"))
    print(id)
    details = util_algorithmic_mall.finder(id)
    print(details)
    util_cache.add(details[0][1], details[0][2], details[0][5])
    return jsonify({"code": 200})


@bp.route('/my_instance', methods=['post', 'get'])
def my_instance():
    if hasattr(g, 'info'):
        if g.info is None:
            return redirect('/login')
        else:
            my_instance = util_instance.find_instance(g.info[1])
            return render_template("my_instance.html", my_instance=my_instance)
    else:
        return redirect('/login')


@bp.route('/canl', methods=['post', 'get'])
def canl():
    danhao=request.values.get('danhao')
    util_pay.orders_canl(danhao)
    return jsonify({"cod":400})


@bp.route('/upload', methods=['get', 'post'])
def upload():
    f = request.files['file']
    f.save(f.filename)
    print("filename", f.filename)
    session['datas'] = f.filename
    return redirect('/calculate_mall')

@bp.route('/calculate_cache', methods=['get', 'post'])
def calculate_cache():
    data=request.values.get("data")
    print("data",data)
    session['datas']=data
    return jsonify({"code":200})
