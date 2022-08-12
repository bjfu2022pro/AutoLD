from flask import Flask
from flask import request
from flask import render_template
import util_user

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/login_result', methods=['get', 'post'])
def login_checker():
    username = request.values.get('phonenumber')
    password = request.values.get('password')
    info = util_user.login_check(username, password)
    print(info)
    return info


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/reg_result', methods=['get', 'post'])
def register_check():
    username = request.values.get('username')
    vcode = request.values.get('vcode')
    password = str(request.values.get('password'))
    repwd = str(request.values.get('repwd'))
    if password != repwd:
        return "两次密码不一致"
    else:
        info = util_user.add_user(username, password)
        return info


@app.route('/usercontrol')
def user_control():
    return render_template("usercontrol.html")

if __name__ == '__main__':
    app.run()