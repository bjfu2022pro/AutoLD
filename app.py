from flask import Flask
from flask import request
from flask import render_template
import util_user

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Flask!'



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