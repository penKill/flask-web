from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# app

db = SQLAlchemy()


def init_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:yyUXx3aHC88r@127.0.0.1:3306/lt'
    # 解决jsonify返回乱码问题
    app.config['JSON_AS_ASCII'] = False

    db.init_app(app)

    from .base import base as base_project
    app.register_blueprint(base_project)
    return app
