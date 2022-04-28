from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_login import LoginManager
from config import config

mail = Mail()
db = SQLAlchemy()
mongo = PyMongo()
login_manager = LoginManager()

# login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # print(app.config)

    mail.init_app(app)
    db.init_app(app)
    mongo.init_app(app)
    login_manager.init_app(app)

    # if app.config['SSL_REDIRECT']:
    #     from flask_sslify import SSLify
    #     sslify = SSLify(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # from .api import api as api_blueprint
    # app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
