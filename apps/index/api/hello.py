from . import index

@index.route('/')
def index_fun():
    return 'this is index of index xxxx'


@index.route('/hello')
def index_hello():
    return 'this is index/hello'


# @index.route('/user')
# def query_user():
#     with db.engine.connect() as con:
#         rs = con.execute("select * from t_user")
#         print(rs.fetchall())
#     return 'user'
