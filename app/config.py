'''
配置文件
'''
import os
import logging
from logging.handlers import RotatingFileHandler
#获取根目录
BASEDIR=os.path.abspath(os.path.dirname(__file__))
#通用配置
class Config:
    #密匙
    SECRET_KEY=os.environ.get('SECRET_KEY') or '123456'

    #数据库配置
    # 逻辑性sql语句自动提交事务(默认为False)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 默认为True,追踪对象的修改,并且在控制台显示
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #数据库查询时间，超过该时间，将日志打印
    DATABASE_QUERY_TIMEOUT=0.1
    # 邮件配置
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = '17328768265@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'zhihuayu95blake'


    #短信配置
    USERNAME='zbhgr'
    PASSWORD_MD5 = 'ef6fcaf836a774b2446bb794a52b8254'  # 32位MD5密码加密，不区分大小写
    APIKEY = '139f7e5ae0e0808d5999ace3d53af5c9'  # apikey秘钥（请登录 http://m.5c.com.cn 短信平台-->账号管理-->我的信息 中复制apikey）


    #文件上传配置
    # 配置上传文件目录
    UPLOADED_PHOTOS_DEST = os.path.join(BASEDIR, 'static/upload')
    # 配置上传文件的大小
    MAX_CONTENT_LENGTH = 1024 * 1024 * 10


    # 额外的初始化
    @staticmethod
    def init_app(app):
        # 日志配置
        formatter = logging.Formatter(
            "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
        handler = RotatingFileHandler('slow_query.log', maxBytes=10000, backupCount=10)
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)

# 开发环境
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://qiqi:Qiqi2018_@rm-j6c7o95747bp853w0so.mysql.rds.aliyuncs.com/aaa'
    SQLALCHEMY_BINDS = {
        'jys': 'mysql://qiqi:Qiqi2018_@rm-j6c7o95747bp853w0so.mysql.rds.aliyuncs.com/jys',
        'qhjy': 'mysql://qiqi:Qiqi2018_@rm-j6c7o95747bp853w0so.mysql.rds.aliyuncs.com/qhjy',
        'wallet': 'mysql://qiqi:Qiqi2018_@rm-j6c7o95747bp853w0so.mysql.rds.aliyuncs.com/wallet',
    }


# 测试环境
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'jys.sqlite')
    REDIS_URL='127.0.0.1'


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@192.168.1.100/aaa'
    SQLALCHEMY_BINDS = {
        'jys': 'mysql://root:root@192.168.1.100/jys',
        'qhjy': 'mysql://root:root@192.168.1.100/qhjy',
        'wallet': 'mysql://root:root@192.168.1.100/wallet',
    }


# 定义一个字典。
config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig,
    'default': TestConfig
}


