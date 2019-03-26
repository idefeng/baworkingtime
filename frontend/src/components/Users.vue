<template>
  <div>
    <el-row style="height: 50px; padding-top: 20px;">
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
          <el-breadcrumb-item><a href="/">活动管理</a></el-breadcrumb-item>
          <el-breadcrumb-item>活动列表</el-breadcrumb-item>
          <el-breadcrumb-item>活动详情</el-breadcrumb-item>
        </el-breadcrumb>
    </el-row>
  <el-table
      id="UsersTable"
      :data="items.slice((currentPage-1)*pageSize, currentPage*pageSize)"
      style="margin: 5px 5px;"
      stripe
      border
      :default-sort="{prop: 'user_cardnum', order: 'ascending'}"
    >
      <el-table-column
        type="index"
      >
      </el-table-column>
      <el-table-column
        prop="user_cardnum"
        label="员工卡号"
        sortable
      >
        <template  slot-scope="data">
          {{ data.row.user_cardnum }}
        </template>
      </el-table-column>
      <el-table-column
        label="员工姓名">
        <template  slot-scope="data">
          {{ data.row.username }}<el-tag type="success">{{ getDays(data.row.entry_time) }}年</el-tag>
        </template>
      </el-table-column>
      <el-table-column
        label="岗位名称">
        <template  slot-scope="data">
          {{ data.row.job_title }}
        </template>
      </el-table-column>
      <el-table-column
        label="Email">
        <template  slot-scope="data">
          {{ data.row.email }}
        </template>
      </el-table-column>
    <el-table-column
        label="入职时间">
        <template  slot-scope="data">
          {{ data.row.entry_time }}
        </template>
      </el-table-column>
      <el-table-column
        label="操作">
        <template  slot-scope="data">
          <el-button type="warning" @click="editUser(data.row)">编辑</el-button>
          <el-button type="danger" @click="popDeleteUserDialog(data.row)">删除</el-button>
        </template>
      </el-table-column>
  </el-table>
    <el-row>
      <el-col :span="4">
        <el-button type="primary" @click="userAddDialogShow = true">添加员工</el-button>
        <el-button type="success" @click="''">批量导入</el-button>
      </el-col>
      <el-col :span="20">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[10, 20, 50, 100]"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="totalRows">
        </el-pagination>
      </el-col>
    </el-row>
  <!--更新用户信息-->
    <el-dialog id="user-update-dialog" title="更新员工信息" :visible.sync="userUpdateDialogShow" center width="30%">
      <el-form :model="editUserForm" label-width="20%">
        <el-form-item label="员工卡号:">
          <el-input v-model="editUserForm.user_cardnum"></el-input>
        </el-form-item>
        <el-form-item label="员工姓名:">
          <el-input v-model="editUserForm.username"></el-input>
        </el-form-item>
        <el-form-item label="岗位名称:">
          <el-input v-model="editUserForm.job_title"></el-input>
        </el-form-item>
        <el-form-item label="电子邮件:">
          <el-input v-model="editUserForm.email"></el-input>
        </el-form-item>
        <el-form-item label="入职时间:">
          <el-date-picker v-model="editUserForm.entry_time" type="datetime" value-format="yyyy-MM-dd HH:mm:ss"></el-date-picker>
        </el-form-item>
        <el-form-item style="text-align: right;">
          <el-button type="primary" @click="onSubmitUpdate">更新信息</el-button>
          <el-button type="danger" @click="onResetUpdate">重置</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <!--添加用户-->
    <el-dialog id="user-add-dialog" title="添加员工" :visible.sync="userAddDialogShow" width="30%" center>
      <el-form :model="addUserForm" label-width="20%">
        <el-form-item label="员工卡号:">
          <el-input v-model="addUserForm.cardnum" placeholder="请输入员工卡号"></el-input>
        </el-form-item>
        <el-form-item label="员工姓名:">
          <el-input v-model="addUserForm.username" placeholder="请输入员工姓名">
          </el-input>
        </el-form-item>
        <el-form-item label="岗位名称:">
          <el-input v-model="addUserForm.job_title" placeholder="请输入员工姓名">
          </el-input>
        </el-form-item>
        <el-form-item label="电子邮件:">
          <el-input v-model="addUserForm.email" placeholder="请输入员工电子邮件">
          </el-input>
        </el-form-item>
        <el-form-item label="入职时间:">
          <el-date-picker type="datetime"
                          v-model="addUserForm.entry_time"
                          value-format="yyyy-MM-dd HH:mm:ss"
                          placeholder="请输入员工入职日期"
                          >
          </el-date-picker>
        </el-form-item>
        <el-form-item style="text-align: right;">
          <el-button type="primary" @click="onSubmit">添加</el-button>
          <el-button type="danger" @click="onReset">重置</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <!-- 删除用户信息的确认对话框 -->
    <el-dialog
      title="确认删除用户信息?"
      :visible.sync="deleteUserDialogVisible"
      width="30%"
      :model="editUserForm"
      center>
      <span style="text-align: center">确认要删除此用户信息?</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="onDeleteUser(editUserForm.id)" type="danger">删除</el-button>
        <el-button @click="noDeleteUser" type="info">取消删除</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Users',
  data () {
    return {
      items: [],
      userUpdateDialogShow: false,
      userAddDialogShow: false,
      deleteUserDialogVisible: false,
      addUserForm: {
        cardnum: '',
        username: '',
        email: '',
        entry_time: '',
        job_title: ''
      },
      editUserForm: {
        id: '',
        user_cardnum: '',
        username: '',
        email: '',
        entry_time: '',
        job_title: ''
      },
      show: true,
      user_type: '',
      user_tag: '',
      totalRows: 0,
      pageSize: 10,
      currentPage: 1
    }
  },
  methods: {
    getUsers () {
      const path = 'http://localhost:5000/api/users'
      axios.get(path)
        .then((res) => {
          // this.users = JSON.parse(res.data.users)
          // console.log(res.data.users)
          this.items = res.data.users
          this.totalRows = this.items.length
        })
        .catch((error) => {
          console.error(error)
        })
    },
    //  添加员工
    addUser (payload) {
      const path = 'http://localhost:5000/api/users'
      axios.post(path, payload)
        .then(() => {
          this.getUsers()
        })
        .catch((error) => {
          console.log(error)
          this.getUsers()
        })
    },
    updateUser (payload, ID) {
      const path = `http://localhost:5000/api/users/${ID}`
      axios.put(path, payload)
        .then(() => {
          this.getUsers()
        })
        .catch((error) => {
          console.error(error)
          this.getUsers()
        })
    },
    editUser (user) {
      this.userUpdateDialogShow = true
      this.editUserForm = user
      // console.log(this.editUserForm)
    },
    initForm () {
      this.addUserForm.cardnum = ''
      this.addUserForm.username = ''
      this.addUserForm.email = ''
      this.addUserForm.entry_time = ''
      this.addUserForm.job_title = ''
      this.editUserForm.id = ''
      this.editUserForm.user_cardnum = ''
      this.editUserForm.username = ''
      this.editUserForm.email = ''
      this.editUserForm.entry_time = ''
      this.editUserForm.job_title = ''
    },
    onSubmit (evt) {
      evt.preventDefault()
      this.userAddDialogShow = false
      const payload = {
        cardnum: this.addUserForm.cardnum,
        username: this.addUserForm.username,
        email: this.addUserForm.email,
        entry_time: this.addUserForm.entry_time,
        job_title: this.addUserForm.job_title
      }
      this.addUser(payload)
      this.initForm()
    },
    onReset (evt) {
      evt.preventDefault()
      this.userAddDialogShow = false
      this.initForm()
    },
    //  更新信息按钮事件
    onSubmitUpdate (evt) {
      evt.preventDefault()
      this.userUpdateDialogShow = false
      const payload = {
        user_cardnum: this.editUserForm.user_cardnum,
        username: this.editUserForm.username,
        email: this.editUserForm.email,
        entry_time: this.editUserForm.entry_time,
        job_title: this.editUserForm.job_title
      }
      // console.log(payload)
      this.updateUser(payload, this.editUserForm.id)
    },
    onResetUpdate (evt) {
      evt.preventDefault()
      this.userUpdateDialogShow = false
      this.initForm()
      this.getUsers()
    },
    removeUser (userID) {
      const path = `http://localhost:5000/api/users/${userID}`
      axios.delete(path)
        .then(() => {
          this.getUsers()
        })
        .catch((error) => {
          console.error(error)
          this.getUsers()
        })
    },
    popDeleteUserDialog (user) {
      this.deleteUserDialogVisible = true
      this.editUserForm = user
    },
    onDeleteUser (userID) {
      // console.log(userID)
      this.deleteUserDialogVisible = false
      this.removeUser(userID)
    },
    noDeleteUser () {
      this.deleteUserDialogVisible = false
    },
    handleSizeChange (val) {
      // console.log(val)
      this.pageSize = val
    },
    handleCurrentChange (val) {
      // console.log(val)
      this.currentPage = val
    },
    // 计算天数
    getDays (sdate) {
      const sDate = new Date(sdate).getFullYear() + '-' + new Date(sdate).getMonth() + '-' + new Date(sdate).getDay()
      // console.log(sDate)
      const now = new Date()
      const days = now.getTime() - new Date(sDate).getTime()
      // console.log(days)
      const day = parseInt(days / (1000 * 60 * 60 * 24 * 365))
      return day
    }
  },
  created () {
    this.getUsers()
  }
}
</script>

<style scoped>

</style>
