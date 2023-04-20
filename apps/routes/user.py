from apps.base import base as base
from .. import db
from sqlalchemy import text


@base.route('/index', methods=['GET'])
def sysconfig_get_value():
    connect = db.engine.connect()
    rs = connect.execute(text('select 1 from dual'))
    print(rs.fetchall())
    return 'hello world'
