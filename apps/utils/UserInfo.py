from flask import request, session
from ..models.User import User


# 获取当前用户信息
def current_user():
    return User.query.filter(User.id == session.get('user-id')).one()
