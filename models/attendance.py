# -*- coding:utf-8 -*-

"""
@version: python2.7
@author: ‘zhangdf‘
@license: Apache Licence 
@contact: 2921558948@qq.com
@site: 
@software: PyCharm
@file: attendance.py
@time: 2019/3/15 15:54
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/attendance?charset=utf8"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    user_cardnum = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True)
    relate_usersCheck = db.relationship('UsersCheck', backref='relate_Users')
    relate_usersDiary = db.relationship('Users_Workdiary', backref='relate_users_diary')

    def __init__(self, user_cardnum, username, email):
        self.user_cardnum = user_cardnum
        self.username = username
        self.email = email

    def __repr__(self):
        return '{\'User\': %r}' % self.username


class UsersCheck(db.Model):
    __tablename__ = 'UsersCheck'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    checkin = db.Column(db.DateTime, nullable=False)
    checkout = db.Column(db.DateTime, nullable=False)
    check_detail = db.Column(db.String(500))

    def __init__(self, userid, checkin, checkout, check_detail):
        self.userid = userid
        self.checkin = checkin
        self.checkout = checkout
        if check_detail == '':
            self.check_detail = '没有说明'
        else:
            self.check_detail = check_detail

    def __repr__(self):
        return self.userid


class Projects_Top_Level(db.Model):
    __tablename__ = 'Projects_Top_Level'
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    project_desc = db.Column(db.String(500))
    relate_level_two = db.relationship('Projects_Level_Two', backref='relate_Top_Level')

    def __init__(self, project_name, project_desc=''):
        self.project_name = project_name
        if project_desc == '':
            self.project_desc = ' 没有填写项目说明'
        else:
            self.project_desc = project_desc

    def __repr__(self):
        return self.project_name


class Projects_Level_Two(db.Model):
    __tablename__ = 'Projects_Level_Two'
    id = db.Column(db.Integer, primary_key=True)
    parent_project = db.Column(db.Integer, db.ForeignKey('Projects_Top_Level.id'), nullable=False)
    project_name = db.Column(db.String(100), nullable=False)
    project_desc = db.Column(db.String(500))
    relate_projects_diary = db.relationship('Users_Workdiary', backref='relate_projects_diary')
    # relate_top_level = db.relationship('Projects_Top_Level', backref='relate_level_two', lazy='dynamic')

    def __init__(self, parent_project, project_name, project_desc=''):
        self.parent_project = parent_project
        self.project_name = project_name
        if project_desc == '':
            self.project_desc = ' 没有填写项目说明'
        else:
            self.project_desc = project_desc

    def __repr__(self):
        return self.project_name


class Users_Workdiary(db.Model):
    __tablename__ = 'Users_Workdiary'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    work_date = db.Column(db.Date, nullable=True)
    work_hours = db.Column(db.Integer, nullable=False)
    project_name = db.Column(db.Integer, db.ForeignKey('Projects_Level_Two.id'), nullable=False)
    work_diary = db.Column(db.String(2000))

    def __init__(self, username, work_date, work_hours, project_name, work_diary = ''):
        self.username = username
        self.work_date = work_date
        self.work_hours = work_hours
        self.project_name = project_name
        if work_diary == '':
            self.work_diary = '没有填写工作日志'
        else:
            self.work_diary = work_diary

    def __repr__(self):
        self.id