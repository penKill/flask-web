from flask import request, jsonify, session
from ..utils import ResUtil
import logging

logger = logging.getLogger(__name__)

REQUIRE_URL = [
    '/base/user/login', '/base/user/search'
    '/base/user/login', '/base/test/test-info'
]


# 定义各种filter的地方改造
def init_filter(app):
    # 登录请求拦截
    @app.before_request
    def check_login():
        uri = request.path
        logging.info('当前访问接口uri={}'.format(uri))
        check = True
        for url in REQUIRE_URL:
            if uri.endswith(url):
                check = False
                break
        if check:
            user_id = session.get('user-id')
            if not user_id:
                return jsonify(ResUtil.un_login())

        else:
            logging.info('访问的接口信息，无需拦截 uri={}'.format(uri))
