import time

from apps.base import base as base
from .. import db
from sqlalchemy import text
from ..models.User import User
from flask import jsonify, request, session
from ..utils import ResUtil
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


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
    try:
        user_info = User.query.filter(*filters).one()
        if not user_info and user_info.password is not password:
            return jsonify(ResUtil.log_error())
        else:

            session['user-id'] = user_info.id
    except Exception as e:
        logger.error('登录发生错误，error={}'.format(e))
        return jsonify(ResUtil.log_error())

    return jsonify(ResUtil.success())


# 获取用户当当前个人信息
@base.route('/user/info', methods=['GET'])
def user_info():
    user_id = session.get('user-id')
    if user_id:
        user_info = User.query.filter(User.id == user_id).one()
        return jsonify(ResUtil.data(user_info.to_simple()))
    else:
        return jsonify(ResUtil.un_login())


# 登录退出处理
@base.route('/user/login-out', methods=['GET'])
def login_out():
    user_id = session.get('user-id')
    if user_id:
        session.pop('user-id')
        return jsonify(ResUtil.success())
    else:
        return jsonify(ResUtil.un_login())


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
    gender = request.args.get('gender')
    page = int(request.args.get('page') if request.args.get('page') else '1')
    size = int(request.args.get('size') if request.args.get('size') else '10')
    filters = []
    if username:
        filters.append(User.username.like('%{}%'.format(username)))
    if gender:
        filters.append(User.gender == gender)
    paginate = User.query.filter(*filters).paginate(page=page, per_page=size)

    return jsonify(ResUtil.paginate_data(paginate))


# 编辑用户信息
@base.route('/user/edit', methods=['POST'])
def user_edit():
    res = User.query.get(request.json['id'])
    res.update_time = datetime.now()
    if 'username' in request.json: res.username = request.json['username']
    if 'nickname' in request.json: res.nickname = request.json['nickname']
    if 'mail' in request.json: res.mail = request.json['mail']
    db.session.add(res)
    return jsonify(ResUtil.success())
