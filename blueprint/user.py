from flask import Blueprint, jsonify, render_template, request
import sys 
sys.path.append("..") 
import util_user
import util_email
from flask_mail import Mail, Message
import random
import string


bp = Blueprint("user", __name__, "/")
mail = Mail()

@bp.route('/')
@bp.route('/login', methods=['get', 'post']) 
def login():
    return render_template("login.html")


@bp.route('/login_result', methods=['get', 'post'])
def login_checker():
    email = request.values.get('phonenumber')
    password = request.values.get('password')
    info = util_user.login_check(email, password)
    print(info)
    return info


@bp.route('/register')
def register():
    return render_template("register.html")


@bp.route('/reg_result', methods=['get', 'post'])
def register_check():
    email = request.values.get('email')
    vcode = request.values.get('vcode')
    password = str(request.values.get('password'))
    repwd = str(request.values.get('repwd'))
    if password != repwd:
        return "两次密码不一致"
    else:
        info = util_user.add_user(email, password)
        return info


@bp.route('/usercontrol')
def user_control():
    return render_template("usercontrol.html")


@bp.route('/password_forget')
def password_forget():
    return render_template("password_forget.html")


@bp.route('/mail', methods=['post', 'get'])
def send_vcode():
    email = request.values.get("email")
    vcode = "".join(random.sample(string.digits, 4))
    mail_body = "您的验证码是：{}".format(vcode)
    message = Message(
        subject="test",
        recipients=[email],
        body=mail_body
    )
    mail.send(message)
    util_email.captcha_insert(email, vcode)
    return jsonify({"code":200})