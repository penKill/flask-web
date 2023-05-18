# 处理全局异常的问题
from werkzeug.exceptions import HTTPException
from flask import jsonify
from ..utils import ResUtil


# 定义全局异常处理的地方
def init_error_handler(app):
    # 全局异常兜底
    @app.errorhandler(Exception)
    def page_not_found(e: Exception):
        return jsonify(ResUtil.server_error(500, e.__str__()))

    # http请求的异常信息
    @app.errorhandler(HTTPException)
    def page_not_found(e: HTTPException):
        return jsonify(ResUtil.server_error(e.code, e.name))

    # 处理500请求异常
    @app.errorhandler(500)
    def internal_server_error(e):
        print('hererererere')

    @app.errorhandler(422)
    @app.errorhandler(400)
    def handle_error(err):
        print('hererererere')

        # headers = err.data.get("headers", None)
        # messages = err.data.get("messages", ["Invalid request."]).get('json')
        # print(err.data.get("messages"))
        # print(messages.items())
        # msg = ''
        #
        # for i in messages.items():
        #     msg = str(i[0]) + str(i[1][0])
        #     break
        #
        # if headers:
        #     return jsonify({"success": False, "msg": msg})
        # else:
        #     return jsonify({"success": False, "msg": msg})
