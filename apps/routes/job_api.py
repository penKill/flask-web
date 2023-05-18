import time
from apps.base import base as base
from flask import jsonify
from ..utils import ResUtil
import logging

logger = logging.getLogger(__name__)


# 今日代办事项
@base.route('/job/todo-list', methods=['GET'])
def todo_list():
    data_list = []
    for i in range(20):
        data_list.append({
            "title": "今日要做的事情{}".format(i),
            "status": i & 3 == 0
        })
    return jsonify(ResUtil.data(data_list))


# 未阅读列表信息
@base.route('/job/undo-list', methods=['GET'])
def undo_list():
    undo_list = []
    for i in range(5):
        undo_list.append({
            "title": "今天要处理的bug的id是{},预计今天处理时间为 {}".format(str(i), time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                 time.localtime())),
            "status": i % 3 == 0
        })
    logger.error("这里是logger的信息")

    return jsonify(ResUtil.data(undo_list))
