from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from random import *
from models.attendance import db, Users, Users_Workdiary, UsersCheck, Projects_Level_Two, Projects_Top_Level
from flask_cors import CORS
from helpers.common import AlchemyEncoder
from openpyxl import load_workbook
import json
import time
import datetime
import os

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
    if request.method == 'POST':    # 增加用户
        post_data = request.get_json()
        user = Users(post_data.get('cardnum'),
                     post_data.get('username'),
                     post_data.get('email'),
                     post_data.get('entry_time'),
                     post_data.get('job_title'))

        db.session.add(user)
        db.session.commit()
        db.session.remove()

    users = Users.query.all()   # 查询所有用户
    result = []
    for user in users:
        if user.entry_time is None:
            result.append({
                'id': user.id,
                'user_cardnum': user.user_cardnum,
                'username': user.username,
                'email': user.email,
                'entry_time': '',
                'job_title': user.job_title
            })
        else:
            result.append({
                'id': user.id,
                'user_cardnum': user.user_cardnum,
                'username': user.username,
                'email': user.email,
                'entry_time': user.entry_time.strftime("%Y-%m-%d"),
                'job_title': user.job_title
            })
    # result = json.loads(json.dumps(users, cls=AlchemyEncoder))
    # print(result)
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
        user.entry_time = datetime.datetime.strptime(post_data.get('entry_time'), "%Y-%m-%d")
        user.job_title = post_data.get('job_title')
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


UPLOAD_DIR = 'upload/batchCheckInfo'
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR
base_dir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = ('xls', 'xlsx')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/api/userscheck/batch', methods=['POST'], strict_slashes=False)
def batch_check_info_upload():
    file_dir = os.path.join(base_dir, app.config['UPLOAD_FOLDER'])
    # print(file_dir)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['check_file']
    # print(f.filename)

    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        ext = fname.rsplit('.', 1)[1]
        unix_time = int(time.time())
        new_filename = str(unix_time) + '.' + ext

        f.save(os.path.join(file_dir, new_filename))
        excel_file = load_workbook(file_dir + '/' + new_filename)
        sheet = excel_file.get_sheet_by_name('北京')  # 打开名叫”“”“”“”“”“”“”“北京的sheet
        # print(sheet["C4"].value)
        # print(sheet.rows)
        # print(sheet)
        check_info = []
        check_rows = tuple(sheet.rows)  # 按行生成tuple
        check_cols = tuple(sheet.columns)   # 按列生成tuple
        # print(check_rows)
        # print(check_cols)
        tmp_value = ''
        for card_number in check_cols[2]:    # 员工卡号，先拿到员工卡号做为分键值
            if card_number.value != tmp_value:  # 确保员工卡号做为键不重复
                check_info.append({card_number.value: {}})  # 生成列表元素是以员工卡号为key的一个字典
                tmp_value = card_number.value

        # for work_day in check_cols[3]:
        #     if work_day.value.strftime('%Y%m%d') != tmp_value:

        for row in check_rows:
            for i in range(len(check_info)):
                if row[2].value in check_info[i]:  # 根据员工卡号去匹配
                    # check_info[i][row[2].value]['name'] = row[1].value
                    # check_info[i][row[2].value]['check'] = row[3].value
                    # print(row[3].value)
                    work_day = row[3].value.strftime('%Y-%m-%d')   # 上班日期,年-月-日格式
                    if work_day not in check_info[i][row[2].value]:     # 如果该员工卡号下面的字典里,没有该日期,则将该打卡时间加入列表
                        check_info[i][row[2].value][work_day] = [row[3].value.strftime('%Y-%m-%d %H:%M:%S')]
                    else:   # 如果有该日期,则append追加到列表
                        check_info[i][row[2].value][work_day].append(row[3].value.strftime('%Y-%m-%d %H:%M:%S'))
        # print(check_info)
        # 下面的语句从用户表中列出userid,user_cardnum列
        user_info = Users.query.with_entities(Users.id, Users.user_cardnum).distinct().all()
        # print(user_info)
        for userInfo in user_info:
            for checkInfo in check_info:
                if userInfo[1] in checkInfo:   # userInfo[1]为员工卡号,如果在checkInfo中存在
                    for key in checkInfo[userInfo[1]]:
                        checkInfo[userInfo[1]][key].sort()  # 将最后的日志按从早到晚进行排序
                        # 插入数据库
                        user_check_info = UsersCheck(userInfo[0],
                                                     checkInfo[userInfo[1]][key][0],
                                                     checkInfo[userInfo[1]][key][len(checkInfo[userInfo[1]][key])-1],
                                                     '没有打卡说明')
                        db.session.add(user_check_info)
                        db.session.commit()

    return jsonify({'result': 'success'})


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


@app.route('/api/workdiary/<diary_id>', methods=['PUT', 'DELETE'])
def single_diary(diary_id):
    if request.method == 'PUT':
        put_data = request.get_json()
        diary_info = Users_Workdiary.query.filter(Users_Workdiary.id == diary_id).first()
        diary_info.username = put_data.get('user_id')
        diary_info.work_date = put_data.get('work_date')
        diary_info.work_hours = put_data.get('work_hours')
        diary_info.project_name = put_data.get('project_id')
        diary_info.work_diary = put_data.get('work_content')

        db.session.add(diary_info)
        db.session.commit()

    if request.method == 'DELETE':
        diary_info = Users_Workdiary.query.filter(Users_Workdiary.id == diary_id).first()
        db.session.delete(diary_info)
        db.session.commit()

    return jsonify({'result': 'success'})
# @app.route('/', defaults={'path': 'POST'})
# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=1)
