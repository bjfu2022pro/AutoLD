from flask import Blueprint, render_template, request, redirect, session

import util_dataset
import datetime
import sys
from flask import g, jsonify


import util_user
sys.path.append("..")
import util_algorithmic_mall
import util_calculate_mall
import util_instance
import util_pay
import util_data
import util_ca_number
bp = Blueprint("mall", __name__, "/")


@bp.route('/algorithmic_mall', methods=['get', 'post'])
def algorithmic():
    AL_select = util_algorithmic_mall.finder2(session.get('sort'))
    return render_template("algorithmic_mall.html", AL_select=AL_select)


@bp.route('/calculate_mall', methods=['get', 'post'])
def calculate():
    calculate_select = util_calculate_mall.find_all()
    return render_template("calculate_mall.html", calculate_select=calculate_select)


@bp.route('/pay')
def confirm():
    util_pay.get_orders1()
    danhao = util_pay.get_orders2()
    util_pay.get_orders3()
    createTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    session['time'] = str(createTime)
    session['danhao'] = int(danhao)
    return render_template('pay.html', time=session['time'], danhao=session['danhao'], datas=session['datas'],
                           algorithmic=session['algorithmic'], calculate=session['calculate'])


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
    session['sort']=sort
    return jsonify({"code": 200})


@bp.route('/algorithmic_details', methods=['get', 'post'])
def details():
    datas=util_data.finder(session.get('sort2'))
    return render_template("algorithmic_details.html", title=session.get('algorithmic'), introduce=session.get('al_introduce'), datas=datas)


@bp.route('/cache', methods=['get', 'post'])
def cache():
    id = int(request.values.get("id"))
    details = util_algorithmic_mall.finder(id)
    session['algorithmic'] = details[0][1]
    session['al_introduce']=details[0][2]
    session['sort2']=int(details[0][5])
    return jsonify({"code": 200})


@bp.route('/my_instance', methods=['post', 'get'])
def my_instance():
    if hasattr(g, 'info'):
        if g.info is None:
            return redirect('/login')
        else:
            my_instance = util_instance.find_instance(g.info[1])
            my_ins = list(my_instance)
            new_list = set()
            for instance in my_ins:
                ins = list(instance)
                my_al = util_algorithmic_mall.finder(ins[2])
                ins[2] = my_al[0][1]
                my_ds = util_dataset.finde_dataset(ins[3])
                ins[3] = my_ds[0][1]
                my_ca = util_calculate_mall.finder(ins[4])
                ins[4] = my_ca[0][1]
                li_tuple = tuple(ins)
                new_list.add(li_tuple)
            new_tuple = sorted(tuple(new_list))
            return render_template("my_instance.html", new_tuple=new_tuple)
    else:
        return redirect('/login')


@bp.route('/canl', methods=['post', 'get'])
def canl():
    danhao = request.values.get('danhao')
    gpu=util_pay.get_dingdan(danhao)
    ca_num = util_ca_number.finder(gpu)
    num = int(ca_num[0][4]) + 1
    util_ca_number.update_num(num, ca_num[0][1])
    util_pay.orders_canl(danhao)
    id=int(danhao)
    util_instance.state_change(id)
    return jsonify({"cod": 400})


@bp.route('/upload', methods=['get', 'post'])
def upload():
    f = request.files['file']
    f.save(f.filename)
    session['datas'] = f.filename
    return redirect('/calculate_mall')


@bp.route('/calculate_cache', methods=['get', 'post'])
def calculate_cache():
    data = request.values.get("data")
    session['datas'] = data
    # ca = session.get('calculate')
    # print("ca",ca)
    # if ca==None :
    return jsonify({"code": 200})
    # else:
    #     return jsonify({"code": 400})


@bp.route('/quxiao', methods=['get', 'post'])
def quxiao():
    session["algorithmic"] = ""
    session['datas'] = ""
    session['calculate'] = ""
    return jsonify({"cod": 800})


@bp.route('/DJ_cache', methods=['get', 'post'])
def DJ_cache():
    ca = request.values.get('ca')
    session['calculate'] = ca
    return jsonify({"code":200})


@bp.route('/zhifu', methods=['get', 'post'])
def zhifu():
    email = g.info[1]
    yue = float(g.info[4])
    if (yue > 5.0):
        yue = yue - 5.0
        ca = session.get('calculate')
        ca_num=util_ca_number.finder(ca)
        print(ca_num)
        num=int(ca_num[0][4])-1
        util_ca_number.update_num(num, ca_num[0][1])
        util_user.update_info(email, yue, 'balance')
        util_pay.save_orders(session['danhao'],email,session['algorithmic'],session['datas'],session['calculate'],session['time'],'prossessing')
        util_instance.add_instance(email,session['algorithmic'],session['datas'],session['calculate'],session['danhao'],session['time'])
        return jsonify({'cod': 200})
    else:
        return jsonify({"cod": 400})
