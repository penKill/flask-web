from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask.json import JSONEncoder
from datetime import datetime, date
from .extensions import init_plugs

# app

db = SQLAlchemy()
app = Flask(__name__)


# 初始化数据库
def init_databases():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/lt'
    app.config["SQLALCHEMY_ECHO"] = True
    # 保证事务自动提交
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


# 初始化web配置
def init_web():
    # 解决jsonify返回乱码问题
    app.config['JSON_AS_ASCII'] = False
    # 配置session的密匙
    app.config['SECRET_KEY'] = 'yyUXx3aHC88r'
    app.config['PROPAGATE_EXCEPTIONS'] = True
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


def logo():
    print('''
 _____                              _           _         ______ _           _    
|  __ \                    /\      | |         (_)       |  ____| |         | |   
| |__) |__  __ _ _ __     /  \   __| |_ __ ___  _ _ __   | |__  | | __ _ ___| | __
|  ___/ _ \/ _` | '__|   / /\ \ / _` | '_ ` _ \| | '_ \  |  __| | |/ _` / __| |/ /
| |  |  __/ (_| | |     / ____ \ (_| | | | | | | | | | | | |    | | (_| \__ \   < 
|_|   \___|\__,_|_|    /_/    \_\__,_|_| |_| |_|_|_| |_| |_|    |_|\__,_|___/_|\_\\

    ''')


def init_app():
    init_databases()
    init_web()
    db.init_app(app)

    from .base import base as base_project
    app.register_blueprint(base_project)
    # 打印log
    logo()

    init_plugs(app)
    return app
