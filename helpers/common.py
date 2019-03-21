# -*- coding:utf-8 -*-

"""
@version: python2.7
@author: ‘zhangdf‘
@license: Apache Licence 
@contact: 2921558948@qq.com
@site: 
@software: PyCharm
@file: common.py
@time: 2019/3/15 18:12
"""
from sqlalchemy.ext.declarative import DeclarativeMeta
import json


class JSONHelper():
    '''
    将list转换成JSON
    '''
    @staticmethod
    def jsonBQlist(bqlist):
        result = []
        for item in bqlist:
            jsondata = {}
            for i in range(item.__len__()):
                tdic={item._fields[i]:item[i]}
                jsondata.update(tdic)
            result.append(jsondata)
        return result


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

