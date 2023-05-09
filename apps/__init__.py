
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# app

db = SQLAlchemy()


def init_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:yyUXx3aHC88r@127.0.0.1:3306/lt'
    app.config["SQLALCHEMY_ECHO"] = True
    # 解决jsonify返回乱码问题
    app.config['JSON_AS_ASCII'] = False
    # 配置session的密匙
    app.config['SECRET_KEY'] = 'yyUXx3aHC88r'

    db.init_app(app)

    from .base import base as base_project
    app.register_blueprint(base_project)
    return app
