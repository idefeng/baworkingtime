# -*- coding:utf-8 -*-

"""
@version: python2.7
@author: ‘zhangdf‘
@license: Apache Licence 
@contact: 2921558948@qq.com
@site: 
@software: PyCharm
@file: projects.py
@time: 2019/3/18 10:40
"""

from flask import Flask, jsonify, request
from helpers.common import AlchemyEncoder
from models.attendance import db, Users, Users_Workdiary, UsersCheck, Projects_Level_Two, Projects_Top_Level
import json


class Projects:
    def all_projects(self):
        all_projects = Projects_Top_Level.query.all()
        result = json.loads(json.dumps(all_projects, cls=AlchemyEncoder))
        return jsonify({'projects': result})