from flask import Flask, render_template, session, g
from blueprint import user_bp, mall_bp

import config
from flask_mail import Mail

import util_user

app = Flask(__name__)
app.config.from_object(config)
mail = Mail()
mail.init_app(app)

app.register_blueprint(user_bp)
app.register_blueprint(mall_bp)


@app.before_request
def before_request():
    email = session.get('email')
    if email:
        info = util_user.finder(email)
        try:
            g.info = info[0]
        except:
            g.info = None
        print(g.info)


@app.context_processor
def context_processor():
    if hasattr(g,'info'):
        if g.info is None:
            return {}
        else:
            return {"info": g.info[1]}
    else:
        return {}


if __name__ == '__main__':
    app.run()
