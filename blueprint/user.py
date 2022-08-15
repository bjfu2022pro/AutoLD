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
    email = request.values.get('loginUsername')
    password = request.values.get('loginPassword')
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
    email = request.values.get('email')                                 #获取前端传递的数据
    vcode = request.values.get('vcode')
    password = str(request.values.get('password'))
    repwd = str(request.values.get('repwd'))
    date_email = util_user.finder(email, "email", "email_captcha")      #获取服务器里当前邮箱的验证码信息
    deltime = datetime.timedelta(seconds=300)                           #过期时间5分钟
    if date_email:                                                      #判断邮箱已经发过验证码
        create_time = date_email[0][3]
        time_inter = datetime.datetime.now()-create_time                #验证码时间
        if vcode == date_email[0][2] and time_inter < deltime:          #确认验证码是否正确
            if password != repwd:                                       #两次输入密码是否正确
                return jsonify({"code":100})                            #返回code100密码不正确
            else:
                util_user.add_user(email, password)
                return jsonify({"code":200})
        else :
            return jsonify({"code":300})
    else:
        return jsonify({"code":400})


@bp.route('/usercontrol')
def user_control():
    return render_template("usercontrol.html")


@bp.route('/password_forget')
def password_forget():
    """
    忘记密码界面
    """
    return render_template("password_forget.html")


@bp.route('/pwd_fgt_ck', methods=['get', 'post'])
def pwd_fgt_ck():
    """
    忘记密码检查
    """
    email = request.values.get('email')
    vcode = str(request.values.get('vcode'))
    new_password = str(request.values.get('new_password'))
    new_repwd = str(request.values.get('new_repwd'))
    date_email = util_user.finder(email, "email", "email_captcha")
    deltime = datetime.timedelta(seconds=300)
    if date_email:
        create_time = date_email[0][3]
        time_inter = datetime.datetime.now() - create_time
        if vcode == date_email[0][2] and time_inter < deltime:
            if new_password != new_repwd:
                return jsonify({"code": 100})
            else:
                util_user.update_info(email, new_password)
                return jsonify({"code": 200})
        else:
            return jsonify({"code": 300})
    else:
        return jsonify({"code": 400})


@bp.route('/reset_mail', methods=['post', 'get'])
def send_reset_vcode():
    """
    重置密码验证码邮件
    """
    email = request.values.get("email")
    reged = util_user.finder(email)
    if reged:
        vcode = "".join(random.sample(string.digits, 4))
        mail_body = "【AutoLD】您的验证码是：{}，该验证码用于重置您的密码，请不要泄露给其他人，如果不是您本人在操作，请忽略此邮件".format(vcode)
        message = Message(
            subject="【AutoLD】重置密码-邮箱验证",
            recipients=[email],
            body=mail_body
        )
        mail.send(message)
        util_email.captcha_insert(email, vcode)
        return jsonify({"code": 200})
    else:
        return jsonify({"code": 100})


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