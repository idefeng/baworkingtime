# -*- coding:utf-8 -*-

"""
@version: python2.7
@author: ‘zhangdf‘
@license: Apache Licence 
@contact: 2921558948@qq.com
@site: 
@software: PyCharm
@file: database.py
@time: 2019/3/15 12:58
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:123456@localhost/attendance", convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    pass