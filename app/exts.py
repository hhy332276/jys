'''
扩展插件
'''
from flask_sqlalchemy import SQLAlchemy
model=SQLAlchemy()
def ext(app):
    model.init_app(app)
