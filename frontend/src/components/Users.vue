<template>
    <div class="container">
      <div class="row">
        <div class="col-md-10">
          <h1>技术部员工管理</h1>
          <hr>
          <button type="button" class="btn btn-success btn-sm" v-b-modal.user-modal>添加员工</button>
          <br><br>
          <table class="table table-hover">
            <thead>
              <tr>
                <!--<th scope="col">ID</th>-->
                <th scope="col">员工卡号</th>
                <th scope="col">员工姓名</th>
                <th scope="col">电子邮件</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(user, index) in users" :key="index">
                <!--<td >{{ user.id }}</td>-->
                <td>{{ user.user_cardnum }}</td>
                <td>{{ user.username }}</td>
                <td>{{ user.email }}</td>
                <td>
                  <button type="button" class="btn btn-warning btn-sm" v-b-modal.user-update-modal @click="editUser(user)">更新</button>
                  <button type="button" class="btn btn-danger btn-sm" @click="onDeleteUser(user)">删除</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <!--添加用户-->
      <b-modal ref="addUser" id="user-modal" title="添加员工" hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-input-group id="form-cardnum-group"  prepend="员工卡号:" label-for="form-cardnum-input">
            <b-form-input id="form-cardnum-input" type="text"
                          v-model="addUserForm.cardnum"
                          required
                          placeholder="请输入员工卡号" trim >
            </b-form-input>
          </b-input-group>
          <br>
          <b-input-group id="form-username-group" prepend="员工姓名:" label-for="form-username-input">
            <b-form-input id="form-username-input" type="text"
                          v-model="addUserForm.username"
                          required
                          placeholder="请输入员工姓名">
            </b-form-input>
          </b-input-group>
          <br>
          <b-input-group id="form-email-group" prepend="电子邮件:" label-for="form-email-input">
            <b-form-input id="form-email-input" type="text"
                          v-model="addUserForm.email"
                          required
                          placeholder="请输入员工电子邮件">
            </b-form-input>
          </b-input-group>
          <br>
          <b-button type="submit" variant="primary">添加</b-button>
          <b-button type="reset" variant="danger">重置</b-button>
        </b-form>
      </b-modal>
      <!--更新用户信息-->
      <b-modal ref="editUser" id="user-update-modal" title="更新员工信息" hide-footer>
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
          <b-input-group id="form-cardnum-edit-group" prepend="员工卡号:" label-for="form-cardnum-edit-input">
            <b-form-input id="form-cardnum-edit-input" type="text"
                          v-model="editUserForm.user_cardnum"
                          required
                          placeholder="请输入员工卡号">
            </b-form-input>
          </b-input-group>
          <br>
          <b-input-group id="form-username-edit-group" prepend="员工姓名:" label-for="form-username-edit-input">
            <b-form-input id="form-username-edit-input" type="text"
                          v-model="editUserForm.username"
                          required
                          placeholder="请输入员工姓名">
            </b-form-input>
          </b-input-group>
          <br>
          <b-input-group id="form-email-edit-group" prepend="电子邮件:" label-for="form-email-edit-input">
            <b-form-input id="form-email-edit-input" type="text"
                          v-model="editUserForm.email"
                          required
                          placeholder="请输入员工电子邮件">
            </b-form-input>
          </b-input-group>
          <br>
          <b-button type="submit" variant="primary">更新信息</b-button>
          <b-button type="reset" variant="danger">重置</b-button>
        </b-form>
      </b-modal>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Users',
  data () {
    return {
      users: [],
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
          this.users = res.data.users
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
