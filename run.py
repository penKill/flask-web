from sqlalchemy import text

from apps import init_app

app = init_app()

# 项目可参考工程 https://gitee.com/zhujf21st/authbase 模拟搭建

if __name__ == '__main__':
    app.run(debug=True)
