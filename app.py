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


if __name__ == '__main__':
    app.run()
