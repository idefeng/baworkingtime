<template>
    <b-container>
      <b-row>
      <el-table
        id="workDiaryTable"
        :data="items"
        :stripe="true"
      >
        <el-table-column prop="id" label="序号"></el-table-column>
        <el-table-column prop="username" label="用户名"></el-table-column>
        <el-table-column prop="work_date" label="日期"></el-table-column>
        <el-table-column prop="work_hours" label="工作时长"></el-table-column>
        <el-table-column prop="project_name" label="涉及项目"></el-table-column>
        <el-table-column prop="work_content" label="工作内容"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="success" size="mini" @click="editDiaryInfo(scope.row)">编辑</el-button>
            <el-button type="danger" size="mini" @click="deleteDiaryInfo(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      </b-row>
      <div class="row" style="text-align: center;">
        <div class="col-md-4" style="text-align: left;">
          <el-button variant="success" @click="getBasicInfo" >单条添加</el-button>
          <el-button variant="primary" sr-only>批量导入</el-button>
        </div>
      </div>
      <!-- 添加日志记录信息 -->
      <b-modal id="addDiayInfo-Modal" ref="addDiaryInfoRef" title="添加日志信息" class="text-left" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset">
        <b-form-group label="员工姓名：" label-for="username-select">
            <b-form-select id="username-select" v-model="username_selected" :options="username_options" required >
              <option :value="null" slot="first">请选择员工姓名</option>
            </b-form-select>
        </b-form-group>
        <b-form-group label="工作项目：" label-for="username-select">
            <b-form-select id="project-select" v-model="project_selected" :options="project_options" required >
              <option :value="null" slot="first">请选择项目名称</option>
            </b-form-select>
        </b-form-group>
        <b-form-group description="注：日期格式YYYY-MM-DD 如：2019-01-01">
            <b-input-group prepend="工作日期:" >
              <b-input v-model="workDiaryForm.work_date"></b-input>
            </b-input-group>
        </b-form-group>
        <b-form-group description="注：以小时为单位">
            <b-input-group prepend="工作时长:" >
              <b-input v-model="workDiaryForm.work_hours"></b-input>
            </b-input-group>
        </b-form-group>
        <b-form-group description="注：填写主要事项">
            <b-input-group prepend="工作内容:">
              <b-input v-model="workDiaryForm.work_content"></b-input>
            </b-input-group>
        </b-form-group>
        <b-button type="submit" variant="primary">添加记录</b-button>
        <b-button type="reset" variant="danger">重置</b-button>
      </b-form>
      </b-modal>
      <!-- 编辑日志记录 -->
      <el-dialog id="editDiaryInfo-Modal" ref="editUserCheckInfoRef" title="编辑日志信息" center width="30%" :visible.sync="diaryUpdateDialogShow">
        <el-form :model="editDiaryInfoForm" @submit="onSubmitEdit" @reset="onResetEdit" label-width="20%">
          <el-form-item label="用户名">
            <el-input v-model="editDiaryInfoForm.username"></el-input>
          </el-form-item>
          <el-form-item label="工作日期">
              <el-input v-model="editDiaryInfoForm.work_date"></el-input>
          </el-form-item>
          <el-form-item label="工作时长" >
              <el-input v-model="editDiaryInfoForm.work_hours"></el-input>
          </el-form-item>
          <el-form-item label="涉及项目" >
            <el-select id="project1-select" v-model="editDiaryInfoForm.project_name" required >
              <el-option
                v-for="item in project_options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
        </el-form-item>
          <el-form-item label="工作内容">
              <el-input type="textarea" :rows="4" v-model="editDiaryInfoForm.work_content"></el-input>
          </el-form-item>
          <span slot="footer" class="dialog-footer">
            <el-button @click=" diaryUpdateDialogShow = false ">取消</el-button>
            <el-button type="primary" @click="onSubmitEdit">确定</el-button>
          </span>
        </el-form>
      </el-dialog>
      <!-- 批量导入工作日志 -->
    </b-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'WorkDiary',
  data () {
    return {
      items: [],
      diaryUpdateDialogShow: false,
      username_options: [],
      project_options: [],
      username_selected: null,
      project_selected: null,
      workDiaryForm: {
        'user_id': '',
        'username': '',
        'work_date': '',
        'work_hours': 0,
        'project_id': '',
        'project_name': '',
        'work_content': ''
      },
      editDiaryInfoForm: {}
    }
  },
  methods: {
    initData () {
      this.workDiaryForm.user_id = ''
      this.workDiaryForm.username = ''
      this.workDiaryForm.work_date = ''
      this.workDiaryForm.project_name = ''
      this.workDiaryForm.project_id = ''
      this.workDiaryForm.work_hours = ''
      this.workDiaryForm.work_content = ''
      this.editDiaryInfoForm = {}
      this.project_options = {}
    },
    getWorkDiary () {
      const path = 'http://localhost:5000/api/workdiary'
      axios.get(path)
        .then((res) => {
          this.items = res.data.results
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getUsers () {
      const path = 'http://localhost:5000/api/users'
      axios.get(path)
        .then((res) => {
          // this.users = JSON.parse(res.data.users)
          // console.log(res.data.users)
          // this.options = res.data.users
          for (let i = 0; i < res.data.users.length; i++) {
            this.username_options.push({
              'value': res.data.users[i].id,
              'text': res.data.users[i].username
            })
          }
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getProjects () {
      const path = 'http://localhost:5000/api/projects/2'
      axios.get(path)
        .then((res) => {
          this.project_options = ''
          // console.log(res.data.projects)
          for (let i = 0; i < res.data.projects.length; i++) {
            this.project_options.push({
              'value': res.data.projects[i].id,
              'label': res.data.projects[i].project_name
            })
          }
        })
        .catch((error) => {
          console.error(error)
        })
    },
    addDiary (payload) {
      const path = 'http://localhost:5000/api/workdiary'
      axios.post(path, payload)
        .then(() => {
          this.getWorkDiary()
        })
        .catch((error) => {
          console.error(error)
          this.getWorkDiary()
        })
    },
    getBasicInfo () {
      this.getUsers()
      this.getProjects()
    },
    onSubmit (evt) {
      evt.preventDefault()
      const payload = {
        'user_id': this.username_selected,
        'work_date': this.workDiaryForm.work_date,
        'work_hours': this.workDiaryForm.work_hours,
        'project_id': this.project_selected,
        'work_content': this.workDiaryForm.work_content
      }
      // console.log(payload)
      this.addDiary(payload)
      this.$refs.addDiaryInfoRef.hide()
      this.initDate()
    },
    onReset (evt) {
      // console.log('onreset')
      evt.preventDefault()
      this.$refs.addDiaryInfoRef.hide()
      this.initDate()
    },
    // 删除单条日志
    removeDiaryInfo (diaryId) {
      const path = `http://localhost:5000/api/workdiary/${diaryId}`
      axios.delete(path)
        .then(() => {
          this.getWorkDiary()
        })
        .catch((error) => {
          console.error(error)
          this.getWorkDiary()
        })
    },
    deleteDiaryInfo (item) {
      this.removeDiaryInfo(item.id)
    },
    // 编辑单条日志
    editDiaryInfo (item) {
      this.getProjects()
      console.log(this.project_options)
      this.diaryUpdateDialogShow = true
      this.editDiaryInfoForm = item
      // console.log(item)
    },
    updateDiary (diaryId, payload) {
      const path = `http://localhost:5000/api/workdiary/${diaryId}`
      axios.put(path, payload)
        .then(() => {
          this.getWorkDiary()
        })
        .catch((error) => {
          console.error(error)
          this.getWorkDiary()
        })
    },
    onSubmitEdit (evt) {
      evt.preventDefault()
      this.$refs.editUserCheckInfoRef.hide()
      const payload = {
        'id': this.editDiaryInfoForm.id,
        'user_id': this.editDiaryInfoForm.user_id,
        'work_date': this.editDiaryInfoForm.work_date,
        'work_hours': this.editDiaryInfoForm.work_hours,
        'project_id': this.editDiaryInfoForm.project_id,
        'work_content': this.editDiaryInfoForm.work_content
      }
      // console.log(payload)
      this.updateDiary(this.editDiaryInfoForm.id, payload)
      this.initDate()
    },
    onResetEdit (evt) {
      evt.preventDefault()
      this.$refs.editUserCheckInfoRef.hide()
      this.initDate()
    }
  },
  created () {
    this.getWorkDiary()
  }
}
</script>

<style scoped>

</style>
