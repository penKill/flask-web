from flask import request, jsonify, session
from ..utils import ResUtil
import logging

logger = logging.getLogger(__name__)


# 定义各种filter的地方改造
def init_filter(app):
    # 登录请求拦截
    @app.before_request
    def check_login():
        uri = request.path
        logging.info('当前访问接口uri={}'.format(uri))
        if not uri.__eq__('/base/user/login'):
            user_id = session.get('user-id')
            if not user_id:
                return jsonify(ResUtil.un_login())
            else:
                pass
        else:
            logging.info('访问登录接口，无需拦截 uri={}'.format(uri))
