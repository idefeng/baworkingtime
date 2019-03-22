from flask import Flask, jsonify, request
from random import *
from models.attendance import db, Users, Users_Workdiary, UsersCheck, Projects_Level_Two, Projects_Top_Level
from flask_cors import CORS
from helpers.common import AlchemyEncoder
import json
import datetime

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def index():
    return 'ddd'


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }

    return jsonify(response)


@app.route('/api/users', methods=['GET', 'POST'])
def all_users():
    if request.method == 'POST':
        post_data = request.get_json()
        # result.append({
        #     'user_cardnum': post_data.get('user_cardnum'),
        #     'username': post_data.get('username'),
        #     'email': post_data.get('email')
        # })
        user = Users(post_data.get('cardnum'), post_data.get('username'), post_data.get('email'))
        db.session.add(user)
        db.session.commit()
        db.session.remove()
    else:
        users = Users.query.all()
        result = json.loads(json.dumps(users, cls=AlchemyEncoder))
        return jsonify({'users': result})

    users = Users.query.all()
    result = json.loads(json.dumps(users, cls=AlchemyEncoder))
    return jsonify({'users': result})


@app.route('/api/users/<userid>', methods=['PUT', 'DELETE'])
def single_user(userid):
    if request.method == 'PUT':
        post_data = request.get_json()
        # userid = post_data.get('id')
        user = Users.query.filter(Users.id == userid).first()
        user.user_cardnum = post_data.get('user_cardnum')
        user.username = post_data.get('username')
        user.email = post_data.get('email')
        db.session.commit()
        db.session.remove()
    if request.method == 'DELETE':
        remove_user(userid)

    users = Users.query.all()
    result = json.loads(json.dumps(users, cls=AlchemyEncoder))
    return jsonify({'users': result})


def remove_user(userid):
    users = Users.query.filter_by(id=userid).all()
    for user in users:
        db.session.delete(user)
    db.session.commit()
    db.session.remove()
    return True


@app.route('/api/projects/<type_id>', methods=['GET', 'POST'])
def all_projects(type_id):
    if request.method == 'POST':    # 添加一级项目
        post_data = request.get_json()
        if type_id == '1':
            top_project = Projects_Top_Level(post_data.get('project_name'), post_data.get('project_desc'))
            db.session.add(top_project)
            db.session.commit()
            db.session.remove()
        elif type_id == '2':    # 添加二级项目
            second_project = Projects_Level_Two(post_data.get('parent_project'),
                                                post_data.get('project2_name'),
                                                post_data.get('project2_desc'))
            db.session.add(second_project)
            db.session.commit()
            db.session.remove()

    result = []
    if type_id == '3':    # 查询所有项目
        all_projects = Projects_Top_Level.query.all()
        for project in all_projects:
            for relate_level_two in project.relate_level_two:
                result.append({"id": project.id,
                               "project_name": project.project_name,
                               "project_desc": project.project_desc,
                               "level2id": relate_level_two.id,
                               "level2projectname": relate_level_two.project_name,
                               "level2projectdesc": relate_level_two.project_desc})
    elif type_id == '1':  # 查询一级项目
        top_projects = Projects_Top_Level.query.all()
        for project in top_projects:
            result.append({"id": project.id,
                           "project_name": project.project_name,
                           "project_desc": project.project_desc})
    elif type_id == '2':  # 查询二级项目
        second_projects = Projects_Level_Two.query.all()
        for project in second_projects:
            result.append({"id": project.id,
                           "parent_id": project.parent_project,
                           "project_name": project.project_name,
                           "project_desc": project.project_desc})

    # result = json.loads(json.dumps(all_projects, cls=AlchemyEncoder))
    # print(result)
    return jsonify({'projects': result})


def remove_projects(type_id, project_id):
    if type_id == '1':
        projects = Projects_Top_Level.query.filter(Projects_Top_Level.id == project_id).all()
    elif type_id == '2':
        projects = Projects_Level_Two.query.filter(Projects_Level_Two.id == project_id).all()

    for project in projects:
        db.session.delete(project)
        db.session.commit()
        db.session.remove()


@app.route('/api/projects/<type_id>/<project_id>', methods=['PUT', 'DELETE'])
def single_projects(type_id, project_id):
    if request.method == 'PUT':    # 添加一级项目
        post_data = request.get_json()
        # print(post_data)
        if type_id == '1':
            pass
        elif type_id == '2':    # 添加二级项目
            second_project = Projects_Level_Two.query.filter(Projects_Level_Two.id == project_id).first()
            second_project.parent_project = post_data.get('parent_project'),
            second_project.project_name = post_data.get('project2_name'),
            second_project.project_desc = post_data.get('project2_desc')
            db.session.commit()
            db.session.remove()
    if request.method == 'DELETE':
        # post_data = request.get_json()
        # print(post_data)
        remove_projects(type_id, project_id)

    return jsonify({'status': 'success'})


@app.route('/api/userscheck', methods=['GET', 'POST'])
def users_check():
    if request.method == 'POST':
        response_data = request.get_json()
        userCheck = UsersCheck(response_data.get('userid'),
                               response_data.get('checkin'),
                               response_data.get('checkout'),
                               response_data.get('check_detail'))
        db.session.add(userCheck)
        db.session.commit()
        db.session.remove()

    users_check = UsersCheck.query.all()
    result = []
    for userCheck in users_check:
        result.append({
            'id': userCheck.id,
            'userid': userCheck.userid,
            'username': userCheck.relate_Users.username,
            'check_date': userCheck.checkin.strftime("%Y-%m-%d"),
            'checkin': userCheck.checkin.strftime("%H:%M:%S"),
            'checkout': userCheck.checkout.strftime("%H:%M:%S"),
            'check_detail': userCheck.check_detail
        })

    return jsonify({'results': result})


@app.route('/api/userscheck/<check_id>', methods=['PUT', 'DELETE'])
def single_check(check_id):
    if request.method == 'PUT':
        put_data = request.get_json()
        users_check = UsersCheck.query.filter(UsersCheck.id == check_id).first()
        users_check.userid = users_check.relate_Users.id
        users_check.checkin = put_data.get('check_date')+' '+put_data.get('checkin')
        users_check.checkin = put_data.get('check_date') + ' ' + put_data.get('checkin')
        users_check.checkout = put_data.get('check_date') + ' ' + put_data.get('checkout')
        users_check.check_detail = put_data.get('check_detail')

        db.session.add(users_check)
        db.session.commit()
    if request.method == 'DELETE':
        user_check = UsersCheck.query.filter(UsersCheck.id == check_id).first()
        db.session.delete(user_check)
        db.session.commit()

    return jsonify({'status': 'success'})


@app.route('/api/workdiary', methods=['GET', 'POST'])
def all_diary():
    if request.method == 'POST':
        post_data = request.get_json()
        work_dairy = Users_Workdiary(post_data.get('user_id'),
                                     post_data.get('work_date'),
                                     post_data.get('work_hours'),
                                     post_data.get('project_id'),
                                     post_data.get('work_content'))
        db.session.add(work_dairy)
        db.session.commit()

    all_diary = Users_Workdiary.query.all()
    result = []
    for diary in all_diary:
        result.append({
            'id': diary.id,
            'user_id': diary.username,
            'username': diary.relate_users_diary.username,
            'work_date': diary.work_date.strftime("%Y-%m-%d"),
            'work_hours': diary.work_hours,
            'project_id': diary.project_name,
            'project_name': diary.relate_projects_diary.project_name,
            'work_content': diary.work_diary
        })

    return jsonify({'results': result})


# @app.route('/', defaults={'path': 'POST'})
# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=1)
