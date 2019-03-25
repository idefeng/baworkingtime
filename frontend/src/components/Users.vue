<template>
    <el-table
      id="UsersTable"
      :data="items"
    >
      <el-table-column
        label="序号“"
        type="index"
      >
      </el-table-column>
      <el-table-column
        label="员工卡号">
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
          <el-button @click="editUser(data.item)">编辑</el-button>
          <el-button type="danger" @click="onDeleteUser(data.item)">删除</el-button>
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
    <!--&lt;!&ndash;添加用户&ndash;&gt;-->
    <!--<b-modal ref="addUser" id="user-modal" title="添加员工" hide-footer>-->
      <!--<b-form @submit="onSubmit" @reset="onReset" class="w-100">-->
        <!--<b-input-group id="form-cardnum-group"  prepend="员工卡号:" label-for="form-cardnum-input">-->
          <!--<b-form-input id="form-cardnum-input" type="text"-->
                        <!--v-model="addUserForm.cardnum"-->
                        <!--required-->
                        <!--placeholder="请输入员工卡号" trim >-->
          <!--</b-form-input>-->
        <!--</b-input-group>-->
        <!--<br>-->
        <!--<b-input-group id="form-username-group" prepend="员工姓名:" label-for="form-username-input">-->
          <!--<b-form-input id="form-username-input" type="text"-->
                        <!--v-model="addUserForm.username"-->
                        <!--required-->
                        <!--placeholder="请输入员工姓名">-->
          <!--</b-form-input>-->
        <!--</b-input-group>-->
        <!--<br>-->
        <!--<b-input-group id="form-email-group" prepend="电子邮件:" label-for="form-email-input">-->
          <!--<b-form-input id="form-email-input" type="text"-->
                        <!--v-model="addUserForm.email"-->
                        <!--required-->
                        <!--placeholder="请输入员工电子邮件">-->
          <!--</b-form-input>-->
        <!--</b-input-group>-->
        <!--<br>-->
        <!--<b-button type="submit" variant="primary">添加</b-button>-->
        <!--<b-button type="reset" variant="danger">重置</b-button>-->
      <!--</b-form>-->
    <!--</b-modal>-->
    <!--&lt;!&ndash;更新用户信息&ndash;&gt;-->
    <!--<b-modal ref="editUser" id="user-update-modal" title="更新员工信息" hide-footer>-->
      <!--<b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">-->
        <!--<b-input-group id="form-cardnum-edit-group" prepend="员工卡号:" label-for="form-cardnum-edit-input">-->
          <!--<b-form-input id="form-cardnum-edit-input" type="text"-->
                        <!--v-model="editUserForm.user_cardnum"-->
                        <!--required-->
                        <!--placeholder="请输入员工卡号">-->
          <!--</b-form-input>-->
        <!--</b-input-group>-->
        <!--<br>-->
        <!--<b-input-group id="form-username-edit-group" prepend="员工姓名:" label-for="form-username-edit-input">-->
          <!--<b-form-input id="form-username-edit-input" type="text"-->
                        <!--v-model="editUserForm.username"-->
                        <!--required-->
                        <!--placeholder="请输入员工姓名">-->
          <!--</b-form-input>-->
        <!--</b-input-group>-->
        <!--<br>-->
        <!--<b-input-group id="form-email-edit-group" prepend="电子邮件:" label-for="form-email-edit-input">-->
          <!--<b-form-input id="form-email-edit-input" type="text"-->
                        <!--v-model="editUserForm.email"-->
                        <!--required-->
                        <!--placeholder="请输入员工电子邮件">-->
          <!--</b-form-input>-->
        <!--</b-input-group>-->
        <!--<br>-->
        <!--<b-button type="submit" variant="primary">更新信息</b-button>-->
        <!--<b-button type="reset" variant="danger">重置</b-button>-->
      <!--</b-form>-->
    <!--</b-modal>-->
  </el-table>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Users',
  data () {
    return {
      items: [],
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
      }
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
      this.$refs.addUser.hide()
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
      this.$refs.addUser.hide()
      this.initForm()
    },
    //  更新信息按钮事件
    onSubmitUpdate (evt) {
      evt.preventDefault()
      this.$refs.editUser.hide()
      const payload = {
        user_cardnum: this.editUserForm.user_cardnum,
        username: this.editUserForm.username,
        email: this.editUserForm.email
      }
      this.updateUser(payload, this.editUserForm.id)
    },
    onResetUpdate (evt) {
      evt.preventDefault()
      this.$refs.editUser.hide()
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
    onDeleteUser (user) {
      this.removeUser(user.id)
    }
  },
  created () {
    this.getUsers()
  }
}
</script>

<style scoped>

</style>
