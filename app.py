from flask import Flask, render_template, session, g
from blueprint import (user_bp, mall_bp, 
                        in_bp, ac_bp, ad_bp)

import config
from flask_mail import Mail

import util_user

app = Flask(__name__)
app.config.from_object(config)
mail = Mail()
mail.init_app(app)

app.register_blueprint(user_bp)
app.register_blueprint(mall_bp)
app.register_blueprint(in_bp)
app.register_blueprint(ac_bp)
app.register_blueprint(ad_bp)


@app.before_request
def before_request():
    email = session.get('email')
    if email:
        info = util_user.finder(email)
        try:
            g.info = info[0]
        except:
            g.info = None


@app.context_processor
def context_processor():
    if hasattr(g,'info'):
        if g.info is None:
            return {}
        else:
            return {"info": g.info}
    else:
        return {}


if __name__ == '__main__':
    app.run(threaded=True,host="0.0.0.0", port='80')
