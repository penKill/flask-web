from flask import Flask

from apps.index.api import index

# app
app = Flask(__name__)


def init_app():
    # 初始化app的相关设置和配置

    # 注册index路由模块
    app.register_blueprint(index)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:yyUXx3aHC88r@127.0.0.1:3306/lt'

    return app

