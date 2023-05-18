from flask import Flask
from .error_handler import init_error_handler
from .filter_handler import init_filter


# 初始化各种插件
def init_plugs(app: Flask) -> None:
    init_error_handler(app)
    init_filter(app)
