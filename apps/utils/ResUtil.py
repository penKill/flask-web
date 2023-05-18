# 返回的数据是object对象
from flask_sqlalchemy.pagination import QueryPagination


def json_data(data):
    return {'msg': '操作成功', 'code': 200, 'data': data.to_json()}


# 返回的数据为简单对象
def data(data):
    return {'msg': '操作成功', 'code': 200, 'data': data}


# 返回数据为数组
def json_list(list_data):
    return {'msg': '操作成功', 'code': 200, 'data': [item.to_json() for item in list_data]}


# 成功获取到的数据
def success():
    return {'msg': '操作成功', 'code': 200, 'data': []}


# 登录失败
def log_error():
    return {'msg': '操作成功', 'code': 500, 'data': '请检查用户名密码是否匹配'}


# 尚未登录
def un_login():
    return {'msg': '尚未登录，请登录', 'code': 505, 'data': []}


# 返回数据为
def paginate_data(paginate: QueryPagination):
    return {'msg': '操作成功', 'code': 200, 'data': {
        "pages": paginate.pages,
        "total": paginate.total,
        "hasNext": paginate.has_next,
        "hasPrev": paginate.has_prev,
        "prevNum": paginate.prev_num,
        "items": [item.to_json() for item in paginate.items]
    }}
