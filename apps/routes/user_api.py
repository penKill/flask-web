import datetime
import time

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
    user_info = User.query.filter(*filters).one()
    if not user_info:
        return jsonify(ResUtil.log_error())
    else:
        session['user-id'] = user_info.id
        return jsonify(ResUtil.success())


# 获取用户当当前个人信息
@base.route('/user/info', methods=['GET'])
def user_info():
    user_id = session.get('user-id')
    if user_id:
        user_info = User.query.filter(User.id == user_id).one()
        return jsonify(ResUtil.data(user_info.to_simple()))
    else:
        return jsonify(ResUtil.un_log())


# 登录退出处理
@base.route('/user/login-out', methods=['GET'])
def login_out():
    user_id = session.get('user-id')
    if user_id:
        session.pop('user-id')
        return jsonify(ResUtil.success())
    else:
        return jsonify(ResUtil.un_log())


@base.route('/user/last-info', methods=['GET'])
def last_info():
    last_login_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    login_info = {
        'last_time': last_login_time,
        'last_place': '广东省深圳市南山区'
    }
    return jsonify(ResUtil.data(login_info))


# 搜索用户列表
@base.route('/user/search', methods=['GET'])
def user_search_list():
    username = request.args.get('username')
    gander = request.args.get('gander')
    page = int(request.args.get('page') if request.args.get('page') else '1')
    size = int(request.args.get('size') if request.args.get('size') else '10')
    filters = []
    if username:
        filters.append(User.username.like('%{}%'.format(username)))
    if gander:
        filters.append(User.gander == gander)
    paginate = User.query.filter(*filters).paginate(page=page, per_page=size)

    return jsonify(ResUtil.paginate_data(paginate))
