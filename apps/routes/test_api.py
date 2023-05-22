from apps.base import base as base
from .. import db
from sqlalchemy import text


from flask import jsonify, request
from ..utils import ResUtil
import logging

logger = logging.getLogger(__name__)


@base.route('test/test-info', methods=['GET'])
def test_info():
    username = request.args.get('username')
    sql = "select * from t_user where username like '%{}%'".format(username)
    connect = db.engine.connect()
    datas = connect.execute(text(sql)).fetchall()
    return jsonify(ResUtil.success())
