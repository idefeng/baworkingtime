<template>
    <b-container>
      <h1>打卡记录管理</h1>
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
        id="projectsTable"
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
          <b-button class="btn-warning" v-b-modal.editUserCheckInfo-Modal @click="editUserCheckInfo(row.item)">编辑</b-button>
          <b-button class="btn-danger" @click="row.toggleDetails">
            {{ row.detailsShowing ? '取消删除' : '删除'}}</b-button>
        </template>
        <template slot="row-details" slot-scope="row">
          <b-card>
            <b-row class="mb-6">
              <b-col class="text-sm-right"><b>一级项目ID：</b></b-col>
              <b-col>{{ row.item.id}}</b-col>
              <b-col class="text-sm-right"><b>用户名：</b></b-col>
              <b-col class="text-sm-left">{{ row.item.username}}</b-col>
              <b-col class="text-sm-right"><b>上班日期：</b></b-col>
              <b-col class="text-sm-left">{{ row.item.check_date}}</b-col>
            </b-row>
            <hr>
            <b-row class="mb-6">
              <b-col class="text-sm-right"><b>上班打卡：</b></b-col>
              <b-col>{{ row.item.checkin}}</b-col>
              <b-col class="text-sm-right"><b>下班打卡：</b></b-col>
              <b-col class="text-sm-left">{{ row.item.checkout}}</b-col>
              <b-col class="text-sm-right"><b>打卡说明：</b></b-col>
              <b-col class="text-sm-left">{{ row.item.check_detail}}</b-col>
            </b-row>
            <hr>
            <b-button class="btn-danger" @click="deleteCheckInfo(row.item)">确定删除打卡信息?</b-button>
          </b-card>
        </template>
      </b-table>
      </b-row>
      <div class="row" style="text-align: center;">
        <div class="col-md-4" style="text-align: left;">
          <b-button variant="success" v-b-modal.addUserCheckInfo-Modal >单条添加</b-button>
          <b-button variant="primary" v-b-modal.topProjectInfo-modal @click="''">批量导入</b-button>
        </div>
        <div class="col-md-4">
          <b-pagination
            :total-rows="totalRows"
            :per-page="perPage"
            v-model="currentPage"
            aria-controls="projectsTable"
            ></b-pagination>
        </div>
        <div class="col-md-4">打卡记录总数:&nbsp;<b>{{ totalRows }}</b>,&nbsp;当前第{{ currentPage }}页&nbsp;</div>
      </div>
      <!-- 添加打卡记录信息 -->
      <b-modal id="addUserCheckInfo-Modal" ref="addUserCheckInfoRef" title="添加打卡信息" class="text-left" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset">
        <b-form-group label="姓名：" label-for="username-select">
          <!--<b-col>-->
            <b-form-select id="username-select" v-model="selected" :options="options" required >
              <option :value="null" slot="first">请选择员工姓名</option>
            </b-form-select>
        </b-form-group>
          <!--</b-col>-->
          <!--<b-col>-->
        <b-form-group description="打卡时间格式YYYY-MM-DD hh:mm:ss 例如2019-03-21 10:00:00">
            <b-input-group prepend="上班打卡时间:" >
              <b-input v-model="checkInfoForm.checkin"></b-input>
            </b-input-group>
        </b-form-group>
          <!--</b-col>-->
          <!--<b-col>-->
        <b-form-group description="打卡时间格式YYYY-MM-DD hh:mm:ss 例如2019-03-21 19:00:00">
            <b-input-group prepend="下班打卡时间:">
              <b-input v-model="checkInfoForm.checkout"></b-input>
            </b-input-group>
        </b-form-group>
          <!--</b-col>-->
        <b-form-group label="有特殊打卡说明吗?">
          <b-form-textarea placeholder="打卡说明" rows="3" id="check_desc" v-model="checkInfoForm.check_detail"></b-form-textarea>
        </b-form-group>
        <b-button type="submit" variant="primary">添加记录</b-button>
        <b-button type="reset" variant="danger">重置</b-button>
      </b-form>
      </b-modal>
      <!-- 编辑打卡记录 -->
      <b-modal id="editUserCheckInfo-Modal" ref="editUserCheckInfoRef" title="编辑打卡信息" class="text-left" hide-footer>
        <b-form @submit="onSubmitEdit" @reset="onResetEdit">
          <label>用户名: {{ editCheckInfoForm.username}}</label>
          <b-form-group >
            <b-input-group prepend="上班具体日期">
              <b-input v-model="editCheckInfoForm.check_date"></b-input>
            </b-input-group>
          </b-form-group>
          <b-form-group >
            <b-input-group prepend="上班打卡时间">
              <b-input v-model="editCheckInfoForm.checkin"></b-input>
            </b-input-group>
          </b-form-group>
          <b-form-group>
            <b-input-group prepend="下班打卡时间">
              <b-input v-model="editCheckInfoForm.checkout"></b-input>
            </b-input-group>
          </b-form-group>
          <b-form-group>
            <b-input-group prepend="打卡理由说明">
              <b-input v-model="editCheckInfoForm.check_detail"></b-input>
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
  name: 'UsersCheck',
  data () {
    return {
      options: [],
      selected: null,
      show: false,
      filter: null,
      totalRows: 0,
      perPage: 10,
      currentPage: 1,
      fields: {
        id: {
          label: '序号'
        },
        username: {
          label: '用户名'
        },
        check_date: {
          label: '日期'
        },
        checkin: {
          label: '上班打卡时间'
        },
        checkout: {
          label: '下班打卡时间'
        },
        check_detail: {
          label: '打卡理由说明'
        },
        actions: {
          label: '操作'
        }
      },
      items: [],
      checkInfoForm: {
        'userid': '',
        'checkin': '',
        'checkout': '',
        'check_detail': ''
      },
      editCheckInfoForm: {
        'id': '',
        'username': '',
        'check_date': '',
        'checkin': '',
        'checkout': '',
        'check_detail': ''
      }
    }
  },
  methods: {
    initData () {
      this.selected = null
      this.checkInfoForm.userid = ''
      this.checkInfoForm.checkin = ''
      this.checkInfoForm.checkout = ''
      this.checkInfoForm.check_detail = ''
      this.editCheckInfoForm.id = ''
      this.editCheckInfoForm.username = ''
      this.editCheckInfoForm.check_date = ''
      this.editCheckInfoForm.checkin = ''
      this.editCheckInfoForm.checkout = ''
      this.editCheckInfoForm.check_detail = ''
      // this.items = []
      // this.options = []
    },
    filterChanged (filteredItems) {
      this.totalRows = filteredItems.length
    },
    getUsersCheck () {
      const path = 'http://localhost:5000/api/userscheck'
      this.items = []
      axios.get(path)
        .then((res) => {
          for (let i = 0; i < res.data.results.length; i++) {
            this.items.push({
              'id': res.data.results[i].id,
              'username': res.data.results[i].username,
              'check_date': res.data.results[i].check_date,
              'checkin': res.data.results[i].checkin,
              'checkout': res.data.results[i].checkout,
              'check_detail': res.data.results[i].check_detail
            })
            // console.log(this.items)
            this.totalRows = this.items.length
          }
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
            this.options.push({
              'value': res.data.users[i].id,
              'text': res.data.users[i].username
            })
          }
        })
        .catch((error) => {
          console.error(error)
        })
    },
    addCheckInfo (payload) {
      const path = 'http://localhost:5000/api/userscheck'
      axios.post(path, payload)
        .then(() => {
          this.getUsersCheck()
        })
        .catch((error) => {
          console.error(error)
          this.getUsersCheck()
        })
    },
    onSubmit (evt) {
      evt.preventDefault()
      const payload = {
        'userid': this.selected,
        'checkin': this.checkInfoForm.checkin,
        'checkout': this.checkInfoForm.checkout,
        'check_detail': this.checkInfoForm.check_detail
      }
      console.log(payload)
      this.addCheckInfo(payload)
      this.$refs.addUserCheckInfoRef.hide()
      this.initData()
    },
    onReset (evt) {
      evt.preventDefault()
      this.$refs.addUserCheckInfoRef.hide()
      this.initData()
    },
    editUserCheckInfo (item) {
      this.editCheckInfoForm = item
      // console.log(this.editCheckInfoForm)
    },
    updateUserCheckInfo (checkId, payload) {
      const path = `http://localhost:5000/api/userscheck/${checkId}`
      axios.put(path, payload)
        .then(() => {
          this.getUsersCheck()
        })
        .catch((error) => {
          console.error(error)
          this.getUsersCheck()
        })
    },
    onSubmitEdit (evt) {
      evt.preventDefault()
      this.$refs.editUserCheckInfoRef.hide()
      const payload = {
        'id': this.editCheckInfoForm.id,
        'check_date': this.editCheckInfoForm.check_date,
        'checkin': this.editCheckInfoForm.checkin,
        'checkout': this.editCheckInfoForm.checkout,
        'check_detail': this.editCheckInfoForm.check_detail
      }
      this.updateUserCheckInfo(this.editCheckInfoForm.id, payload)
    },
    onResetEdit (evt) {
      evt.preventDefault()
      this.$refs.editUserCheckInfoRef.hide()
      this.initData()
    },
    removeCheckInfo (checkId) {
      const path = `http://localhost:5000/api/userscheck/${checkId}`
      axios.delete(path)
        .then(() => {
          this.getUsersCheck()
        })
        .catch((error) => {
          console.error(error)
          this.getUsersCheck()
        })
    },
    deleteCheckInfo (item) {
      this.removeCheckInfo(item.id)
    }
  },
  created () {
    this.getUsersCheck()
    this.getUsers()
  }
}
</script>

<style scoped>

</style>
