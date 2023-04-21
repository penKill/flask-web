def json_data(data):
    return {'msg': '操作成功', 'code': 200, 'data': data.to_json()}


# 返回数据为数组
def json_list(list_data):
    return {'msg': '操作成功', 'code': 200, 'data': [data.to_json() for data in list_data]}
