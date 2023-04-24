from apps.base import base as base
from .. import db
from sqlalchemy import text
from ..models.User import User
from flask import jsonify, request, session
from ..utils import ResUtil


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
    return jsonify(ResUtil.json_list(data_list))


# 登录接口
@base.route('/user/login', methods=['POST'])
def login():
    filters = []

    username = request.json['username']
    password = request.json['password']
    if username:
        filters.append(User.username == username)
    if password:
        filters.append(User.password == password)
    data_list = User.query.filter(*filters).all()
    if not data_list:
        return jsonify(ResUtil.log_error())
    else:
        out = jsonify(ResUtil.json_list(data_list))
        out.set_cookie('User-Info', 'this is good cookie')
        session['userInfo'] = 'userinfo-session'
        return out


# 获取用户能拿到的菜单
@base.route('/user/menu', methods=['GET'])
def menu():
    user_info = session['userInfo']
    print(user_info)
    data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return jsonify(ResUtil.data(data))
