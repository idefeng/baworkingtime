<template>
    <b-container>
      <h1>工作日志管理</h1>
      <b-row>
        <b-col md="6" class="my-3">
          <b-form-group label-cols-sm="3" class="mb-1">
            <b-input-group prepend="查找">
              <b-form-input v-model="filter" placeholder="输入关键字搜索" />
              <b-input-group-append>
                <b-button :disabled="!filter" @click="filter = ''">清除条件</b-button>
              </b-input-group-append>
            </b-input-group>
          </b-form-group>
        </b-col>
      </b-row>
      <b-row>
      <b-table
        id="workDiaryTable"
        show-empty
        empty-text="无数据可加载..."
        striped
        hover
        :filter="filter"
        @filtered="filterChanged"
        :fields="fields"
        :items="items"
        :per-page="perPage"
        :current-page="currentPage"
      >
        <template slot="index" slot-scope="data">
          {{ data.index + 1 }}
        </template>
        <template slot="actions" slot-scope="row">
          <b-button class="btn-warning" v-b-modal.editDiaryInfo-Modal @click="editDiaryInfo(row.item)">编辑</b-button>
          <b-button class="btn-danger" @click="row.toggleDetails">
            {{ row.detailsShowing ? '取消删除' : '删除'}}</b-button>
        </template>
        <template slot="row-details" slot-scope="row">
          <b-card>
            <b-row class="mb-6">
              <b-col class="text-sm-right"><b>日志ID：</b></b-col>
              <b-col>{{ row.item.id}}</b-col>
              <b-col class="text-sm-right"><b>用户名称：</b></b-col>
              <b-col class="text-sm-left">{{ row.item.username}}</b-col>
              <b-col class="text-sm-right"><b>工作日期：</b></b-col>
              <b-col class="text-sm-left">{{ row.item.work_date}}</b-col>
            </b-row>
            <hr>
            <b-row class="mb-6">
              <b-col class="text-sm-right"><b>工作时长：</b></b-col>
              <b-col>{{ row.item.work_hours}}</b-col>
              <b-col class="text-sm-right"><b>工作项目：</b></b-col>
              <b-col class="text-sm-left">{{ row.item.project_name}}</b-col>
              <b-col class="text-sm-right"><b>工作内容：</b></b-col>
              <b-col class="text-sm-left">{{ row.item.work_content}}</b-col>
            </b-row>
            <hr>
            <b-button class="btn-danger" @click="deleteDiaryInfo(row.item)">确定删除该条日志信息?</b-button>
          </b-card>
        </template>
      </b-table>
      </b-row>
      <div class="row" style="text-align: center;">
        <div class="col-md-4" style="text-align: left;">
          <b-button variant="success" v-b-modal.addDiayInfo-Modal @click="getBasicInfo" >单条添加</b-button>
          <b-button variant="primary" sr-only>批量导入</b-button>
        </div>
        <div class="col-md-4">
          <b-pagination
            :total-rows="totalRows"
            :per-page="perPage"
            v-model="currentPage"
            aria-controls="projectsTable"
            ></b-pagination>
        </div>
        <div class="col-md-4">部门工作日志记录总数:&nbsp;<b>{{ totalRows }}</b>,&nbsp;当前第{{ currentPage }}页&nbsp;</div>
      </div>
      <!-- 添加日志记录信息 -->
      <b-modal id="addDiayInfo-Modal" ref="addDiaryInfoRef" title="添加打卡信息" class="text-left" hide-footer>
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
      <!-- 编辑打卡记录 -->
      <b-modal id="editDiaryInfo-Modal" ref="editUserCheckInfoRef" title="编辑打卡信息" class="text-left" hide-footer>
        <b-form @submit="onSubmitEdit" @reset="onResetEdit">
          <label>用户名: {{ editDiaryInfoForm.username}}</label>
          <b-form-group >
            <b-input-group prepend="上班具体日期">
              <b-input v-model="editDiaryInfoForm.check_date"></b-input>
            </b-input-group>
          </b-form-group>
          <b-form-group >
            <b-input-group prepend="上班打卡时间">
              <b-input v-model="editDiaryInfoForm.checkin"></b-input>
            </b-input-group>
          </b-form-group>
          <b-form-group>
            <b-input-group prepend="下班打卡时间">
              <b-input v-model="editDiaryInfoForm.checkout"></b-input>
            </b-input-group>
          </b-form-group>
          <b-form-group>
            <b-input-group prepend="打卡理由说明">
              <b-input v-model="editDiaryInfoForm.check_detail"></b-input>
            </b-input-group>
          </b-form-group>
          <b-button variant="success" type="submit">确认</b-button>
          <b-button variant="danger" type="reset">重置</b-button>
        </b-form>
      </b-modal>
    </b-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'WorkDiary',
  data () {
    return {
      totalRows: 0,
      perPage: 10,
      currentPage: 1,
      filter: null,
      fields: {
        'id': {
          label: '序号'
        },
        'username': {
          label: '姓名'
        },
        'work_date': {
          label: '工作日期'
        },
        'work_hours': {
          label: '工作时长',
          sortable: true
        },
        'project_name': {
          label: '工作项目'
        },
        'work_content': {
          label: '工作内容'
        },
        'actions': {
          label: '操作'
        }
      },
      items: [],
      username_options: [],
      project_options: [],
      username_selected: null,
      project_selected: null,
      workDiaryForm: {
        'user_id': '',
        'user_name': '',
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
    initDate () {
      this.workDiaryForm.user_id = ''
      this.workDiaryForm.user_name = ''
      this.workDiaryForm.work_date = ''
      this.workDiaryForm.project_name = ''
      this.workDiaryForm.project_id = ''
      this.workDiaryForm.work_hours = ''
      this.workDiaryForm.work_content = ''
    },
    filterChanged (filteredItems) {
      this.totalRows = filteredItems.length
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
          // console.log(res.data.projects)
          for (let i = 0; i < res.data.projects.length; i++) {
            this.project_options.push({
              'value': res.data.projects[i].id,
              'text': res.data.projects[i].project_name
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
      // console.log('onsubmit')
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
    onSubmitEdit (evt) {
      evt.preventDefault()
    },
    onResetEdit (evt) {
      evt.preventDefault()
    }
  },
  created () {
    this.getWorkDiary()
  }
}
</script>

<style scoped>

</style>
