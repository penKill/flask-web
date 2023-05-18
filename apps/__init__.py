from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask.json import JSONEncoder
from datetime import datetime, date

# app

db = SQLAlchemy()
app = Flask(__name__)


# 初始化数据库
def init_databases():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:yyUXx3aHC88r@127.0.0.1:3306/lt'
    app.config["SQLALCHEMY_ECHO"] = True
    # 保证事务自动提交
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


# 初始化web配置
def init_web():
    # 解决jsonify返回乱码问题
    app.config['JSON_AS_ASCII'] = False
    # 配置session的密匙
    app.config['SECRET_KEY'] = 'yyUXx3aHC88r'
    CORS(app, supports_credentials=True)
    app.json_encoder = CustomJSONEncoder


# 替换默认的json格式序列化
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return JSONEncoder.default(self, obj)


def init_app():
    init_databases()
    init_web()
    db.init_app(app)

    from .base import base as base_project
    app.register_blueprint(base_project)
    return app
