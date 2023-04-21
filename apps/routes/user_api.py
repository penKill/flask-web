from apps.base import base as base
from .. import db
from sqlalchemy import text
from ..models.User import User
from flask import jsonify
from ..utils import response


@base.route('/index', methods=['GET'])
def index():
    connect = db.engine.connect()
    rs = connect.execute(text('select 1 from dual'))
    print(rs.fetchall())
    return 'hello world'


@base.route('/user', methods=['GET'])
def user():
    data_list = User.query.all()
    # return jsonify({'msg': '操作成功', 'code': 200, 'data': [data.to_json() for data in data_list]})
    return jsonify(response.json_list(data_list))


# 登录接口
@base.route('/user/login')
def login():
    return 'hello world'
