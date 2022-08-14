from flask import Flask, render_template
from blueprint import user_bp, mall_bp

import config
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(config)
mail = Mail()
mail.init_app(app)

app.register_blueprint(user_bp)
app.register_blueprint(mall_bp)

dingdan = [
    {
        'dingdanhao': '10000', 'peizhi': 'j',
        'leixing': 'i', 'shujuji': 'n',
        'jine': '11', 'shijian': '11',
        'fukuanren': '金旭光'
    }
]


@app.route('/pay_confirm')
def confirm():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run()
