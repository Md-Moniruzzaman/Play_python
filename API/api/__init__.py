from flask import Flask
from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("api/Key.json")
default_app = initialize_app(cred)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'dev'

    from .userApi import userApi

    app.register_blueprint(userApi, url_prefix  = '/user')
    return app