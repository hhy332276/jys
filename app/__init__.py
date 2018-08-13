'''
初始化flask应用（全局配置，插件集成）
'''
from app.views import config_blueprint
from .config import config
from .exts import ext
from flask import Flask
def create_app(config_name):
    # 创建flask实例对象
    app = Flask(__name__)
    # 初始化
    app.config.from_object(config.get(config_name, 'default'))
    # 执行额外的初始化操作
    config[config_name].init_app(app)
    # 注册蓝本
    config_blueprint(app)
    # 扩展文件打包
    # 返回生成的app
    return app

