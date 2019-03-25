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
          {{ data.row.username }}
        </template>
      </el-table-column>
      <el-table-column
        label="Email">
        <template  slot-scope="data">
          {{ data.row.email }}
        </template>
      </el-table-column>
      <el-table-column
        label="操作">
        <template  slot-scope="data">
          <el-button type="warning" @click="editUser(data.row)">编辑</el-button>
          <el-button type="danger" @click="popDeleteUserDialog(data.row)">删除</el-button>
        </template>
      </el-table-column>
          <!--<template slot="actions" slot-scope="row">-->
            <!--<b-button class="btn-warning" v-b-modal.user-update-modal @click="editUser(row.item)">编辑</b-button>-->
            <!--<b-button class="btn-danger" @click="row.toggleDetails">-->
              <!--{{ row.detailsShowing ? '取消删除' : '删除'}}</b-button>-->
          <!--</template>-->
          <!--<template slot="row-details" slot-scope="row">-->
            <!--<b-card>-->
              <!--<b-row class="mb-6">-->
                <!--<b-col class="text-sm-right"><b>员工ID：</b></b-col>-->
                <!--<b-col>{{ row.item.id}}</b-col>-->
                <!--<b-col class="text-sm-right"><b>用户名称：</b></b-col>-->
                <!--<b-col class="text-sm-left">{{ row.item.username}}</b-col>-->
                <!--<b-col class="text-sm-right"><b>电子邮件：</b></b-col>-->
                <!--<b-col class="text-sm-left">{{ row.item.email}}</b-col>-->
              <!--</b-row>-->
              <!--<hr>-->
              <!--<b-button class="btn-danger" @click="onDeleteUser(row.item)">确定删除该条日志信息?</b-button>-->
            <!--</b-card>-->
          <!--</template>-->
        <!--</el-table>-->
        <!--&lt;!&ndash;</b-row>&ndash;&gt;-->
         <!--<div class="row" style="text-align: center;">-->
          <!--<div class="col-md-4" style="text-align: left;">-->
            <!--<button type="button" class="btn btn-success" v-b-modal.user-modal>添加员工</button>-->
            <!--<b-button variant="primary" v-b-modal.batchImportCheckInfo-Modal @click="''">批量导入</b-button>-->
          <!--</div>-->

        <!--<div class="col-md-4">-->
        <!--<b-pagination-->
          <!--:total-rows="totalRows"-->
          <!--:per-page="perPage"-->
          <!--v-model="currentPage"-->
          <!--aria-controls="projectsTable"-->
          <!--&gt;</b-pagination>-->
      <!--</div>-->
      <!--<div class="col-md-4">打卡记录总数:&nbsp;<b>{{ totalRows }}</b>,&nbsp;当前第{{ currentPage }}页&nbsp;</div>-->
      <!--</div>-->
    <!--</div>-->
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
        <el-form-item label="电子邮件:">
          <el-input v-model="editUserForm.email"></el-input>
        </el-form-item>
        <el-form-item style="text-align: right;">
          <b-button type="submit" @click="onSubmitUpdate">更新信息</b-button>
          <b-button type="reset" @click="onResetUpdate">重置</b-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <!--添加用户-->
    <el-dialog id="user-add-dialog" title="添加员工" :visible.sync="userAddDialogShow" width="30%">
      <el-form :model="addUserForm" label-width="20%">
        <el-form-item label="员工卡号:">
          <el-input v-model="addUserForm.cardnum" placeholder="请输入员工卡号"></el-input>
        </el-form-item>
        <el-form-item label="员工姓名:">
          <el-input v-model="addUserForm.username" placeholder="请输入员工姓名">
          </el-input>
        </el-form-item>
        <br>
        <el-form-item label="电子邮件:">
          <el-input v-model="addUserForm.email" placeholder="请输入员工电子邮件">
          </el-input>
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
        email: ''
      },
      editUserForm: {
        id: '',
        user_cardnum: '',
        username: '',
        email: ''
      },
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
      this.editUserForm.id = ''
      this.editUserForm.user_cardnum = ''
      this.editUserForm.username = ''
      this.editUserForm.email = ''
    },
    onSubmit (evt) {
      evt.preventDefault()
      this.userAddDialogShow = false
      const payload = {
        cardnum: this.addUserForm.cardnum,
        username: this.addUserForm.username,
        email: this.addUserForm.email
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
        email: this.editUserForm.email
      }
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
    }
  },
  created () {
    this.getUsers()
  }
}
</script>

<style scoped>

</style>
