from flask import request, jsonify, session
from ..utils import ResUtil


def init_filter(app):
    # 登录请求拦截
    @app.before_request
    def check_login():
        uri = request.path
        if not uri.__eq__('/base/user/login'):
            user_id = session.get('user-id')
            if not user_id:
                return jsonify(ResUtil.un_login())
            else:
                pass
        else:
            pass
