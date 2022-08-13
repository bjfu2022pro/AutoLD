import random
import string
import datetime

from flask import Blueprint, jsonify, render_template, request
from flask_mail import Mail, Message

import sys 
sys.path.append("..") 
import util_user
import util_email




bp = Blueprint("user", __name__, "/")
mail = Mail()


@bp.route('/')
@bp.route('/login', methods=['get', 'post']) 
def login():
    """
    登录界面
    """
    return render_template("login.html")


@bp.route('/login_result', methods=['get', 'post'])
def login_checker():
    """
    登录检查
    """
    email = request.values.get('phonenumber')
    password = request.values.get('password')
    info = util_user.login_check(email, password)
    print(info)
    return info


@bp.route('/register')
def register():
    """
    注册界面
    """
    return render_template("register.html")


@bp.route('/reg_result', methods=['get', 'post'])
def register_check():
    """
    注册检查
    """
    email = request.values.get('email')
    vcode = request.values.get('vcode')
    password = str(request.values.get('password'))
    repwd = str(request.values.get('repwd'))
    date_email = util_user.finder(email, "email", "email_captcha")
    deltime = datetime.timedelta(seconds=300)
    if date_email:
        create_time = date_email[0][3]
        time_inter = datetime.datetime.now()-create_time
        if vcode == date_email[0][2] and time_inter < deltime:
            if password != repwd:
                return jsonify({"code":100})
            else:
                util_user.add_user(email, password)
                return jsonify({"code":200})
        else :
            return jsonify({"code":300})


@bp.route('/usercontrol')
def user_control():
    return render_template("usercontrol.html")


@bp.route('/password_forget')
def password_forget():
    return render_template("password_forget.html")


@bp.route('/mail', methods=['post', 'get'])
def send_vcode():
    email = request.values.get("email")
    reged = util_user.finder(email)
    if reged:
        return jsonify({"code":100})
    else:
        vcode = "".join(random.sample(string.digits, 4))
        mail_body = "【AutoLD】欢迎您注册AutoLD账户，您的验证码是：{}，请不要泄露给其他人，如果不是您本人在操作，请忽略此邮件".format(vcode)
        message = Message(
            subject="【AutoLD】邮箱验证",
            recipients=[email],
            body=mail_body
        )
        mail.send(message)
        util_email.captcha_insert(email, vcode)
        return jsonify({"code":200})