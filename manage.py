'''
启动程序的一个入口文件
'''

import os
from flask_script import Manager

import datetime
from flask_cors import *
# from flask_apidoc import ApiDoc
# 获取配置
from app import create_app
config_name = os.environ.get('FLASK_CONFIG', 'default')
# 创建Flask实例
app = create_app(config_name)
# doc = ApiDoc(app=app)
CORS(app, supports_credentials=True)
# 设置session的过期时间
app.permanent_session_lifetime = datetime.timedelta(hours=24 * 31)
manage = Manager(app)


# 创建命令行启动控制对象
# manager = Manager(app)
# 启动项目
if __name__ == '__main__':
    manage.run()
