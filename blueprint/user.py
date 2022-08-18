import random
import string
import datetime

from flask import (Blueprint, jsonify, 
                    render_template, 
                    request, session,
                    redirect, g)
from flask_mail import Mail, Message

import sys 
sys.path.append("..") 
import util_user
import util_email




bp = Blueprint("user", __name__, "/")
mail = Mail()


@bp.route('/')
@bp.route('/home', methods=['get', 'post']) 
def home():
    """
    首页
    """
    return render_template("home.html")


@bp.route('/login', methods=['get', 'post']) 
def login():
    """
    登录界面
    """
    return render_template("login.html")


@bp.route("/logout")
def logout():
    """
    清除session中所有的数据
    """
    session.clear()
    return redirect('/login')


@bp.route('/login_result', methods=['get', 'post'])
def login_checker():
    """
    登录检查
    """
    email = request.values.get('email')
    password = request.values.get('password')
    code = util_user.login_check(email, password)
    if code == 200:
        session['email'] = email
    return jsonify({"code":code})


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
    """
    个人中心界面
    """
    if hasattr(g,'info'):
        if g.info is None:
            return redirect('/login')
        else: 
            return render_template("usercontrol.html")
    else:
        return redirect('/login')


@bp.route('/password_change')
def password_change():
    """
    更改密码界面
    """
    if hasattr(g, 'info'):
        if g.info is None:
            return redirect('/login')
        else:
            return render_template("password_change.html")
    else:
        return redirect('/login')


@bp.route('/password_forget')
def password_forget():
    """
    忘记密码界面
    """
    return render_template("password_forget.html")


@bp.route('/email_check',methods=['post', 'get'])
def email_chenck():
    """
    改绑邮箱号检查
    """
    email = request.values.get('email')
    new_email = request.values.get('new_email')
    vcode = str(request.values.get('vcode'))
    date_email = util_user.finder(email, "email", "email_captcha")
    result = util_user.email_change(new_email, email)
    deltime = datetime.timedelta(seconds=300)
    if date_email:
        create_time = date_email[0][3]
        time_inter = datetime.datetime.now() - create_time
        if vcode == date_email[0][2] and time_inter < deltime:
             if result == 100:
                return jsonify({"code": 100})
             else:
                return jsonify({"code": 200})
        else:
            return jsonify({"code": 300})
    else:
        return jsonify({"code": 400})


@bp.route('/email_change')
def enail_change():
    """
    修改邮箱号界面
    """
    return render_template('/email_change.html')


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
        return jsonify({"code": 100})
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
        return jsonify({"code": 200})


@bp.route('/email', methods=['post', 'get'])
def send_email_code():
    email = request.values.get("email")
    reged = util_user.finder(email)
    if reged:
        vcode = "".join(random.sample(string.digits, 4))
        mail_body = "【AutoLD】您的验证码是：{}，该验证码用于修改您绑定的邮箱号，请不要泄露给其他人，如果不是您本人在操作，请忽略此邮件".format(vcode)
        message = Message(
            subject="【AutoLD】改绑邮箱号-邮箱验证",
            recipients=[email],
            body=mail_body
        )
        mail.send(message)
        util_email.captcha_insert(email, vcode)
        return jsonify({"code": 200})
    else:
        return jsonify({"code": 100})


@bp.route('/pwd_change', methods=['post', 'get'])
def pwd_change():
    email = request.values.get("email")
    old_password = request.values.get("old_password")
    new_password = request.values.get("new_password")
    new_repwd = request.values.get("new_repwd")
    this_user = util_user.finder(email)
    if old_password == this_user[0][2]:
        if new_password == new_repwd:
            if new_password == old_password:
                return jsonify({"code": 100})   # 新密码与旧密码相同
            else:
                util_user.update_info(email, new_password)
                return jsonify({"code": 200})   # 成功更改
        else:
            return jsonify({"code": 300})       # 两次新密码输入不一致
    else:
        return jsonify({"code": 400})           # 旧密码不正确


@bp.route('/user_update')
def user_update():
    """
        更新用户信息
    """
    username = request.values.get("username")
    gender = request.values.get("gender")
    company = request.values.get("company")
    grjm = request.values.get("grjm")
    describe = request.values.get("describe")
    util_user.update_info(g.info[1], username, "username")
    util_user.update_info(g.info[1], gender, "gender")
    util_user.update_info(g.info[1], company, "company")
    util_user.update_info(g.info[1], grjm, "link")
    util_user.update_info(g.info[1], describe, "self_intro")
    return jsonify({"code": 200})


@bp.route('/my_account')
def my_account():
    return render_template('my_account.html')


@bp.route('/aboutus')
def aboutus():
    """
    关于我们界面
    """
    return render_template("aboutus.html")