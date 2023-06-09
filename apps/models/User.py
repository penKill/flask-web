import json

from .. import db
from datetime import datetime


# 用户表相关信息
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    nickname = db.Column(db.String)
    company_id = db.Column(db.String)
    gender = db.Column(db.Integer)
    age = db.Column(db.Integer)
    mail = db.Column(db.String)
    phone = db.Column(db.String)
    create_time = db.Column(db.DATETIME, default=datetime.now)
    update_time = db.Column(db.DATETIME, default=datetime.now)
    user_desc = db.Column(db.String)

    def __str__(self):
        return json.dump(self)

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<Role %r>' % self.id

    # 对象转给前端的时候调用的方法
    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'nickname': self.nickname,
            'companyId': self.company_id,
            'gender': self.gender,
            'age': self.age,
            'userDesc': self.user_desc,
            'mail': self.mail
        }

    # 对象转给前端的时候调用的方法
    def to_simple(self):
        return {
            'username': self.username,
            'nickname': self.nickname,
            'gender': self.gender,
            'age': self.age,
            'userDesc': self.user_desc,
            'mail': self.mail
        }