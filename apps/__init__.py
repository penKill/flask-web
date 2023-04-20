from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app

db = SQLAlchemy()


def init_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/djangoblog'

    db.init_app(app)

    from .base import base as base_project
    app.register_blueprint(base_project)
    return app
