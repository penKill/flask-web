from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from apps.factory import init_app

app = init_app()
db = SQLAlchemy(app)


@app.route("/")
def testconn():
    connect = db.engine.connect()
    rs = connect.execute(text("select * from t_user"))
    print(rs.fetchone())
    return "success"

@app.route("/a")
def testconna():

    return "a"



if __name__ == '__main__':
    app.run(debug=True)
