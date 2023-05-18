# 处理全局异常的问题
from ..base import base
from ..base.config import get_logger
from werkzeug.exceptions import HTTPException

logging = get_logger(__name__)


# @base.errorhandler(Exception)
def handler_exception(e):
    logging.error('这里的处理异常错误')


# @base.errorhandler(HTTPException)
def handler_http_exception(e):
    logging.error('这里的处理异常错误HTTPException')


# @base.errorhandler(404)
def handler_404_exception(e):
    logging.error('这里的处理异常错误HTTPException')
