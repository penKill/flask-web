from apps.base import base as base
from flask import jsonify, request, session
from ..utils import ResUtil


# 获取当前用户授权的菜单
@base.route('/menu-defined', methods=['GET'])
def menu():
    data = []
    for i in range(100):
        data.append('{}'.format(i))
    return jsonify(ResUtil.data(data))
