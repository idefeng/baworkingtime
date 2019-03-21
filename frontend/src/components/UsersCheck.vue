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
        :fields="fields"
        :items="items"
        :per-page="perPage"
        :current-page="currentPage"
      >
        <template slot="index" slot-scope="data">
          {{ data.index + 1 }}
        </template>
        <template slot="actions" slot-scope="row">
          <b-button class="btn-warning" v-b-modal.editProjectInfo @click="editProject(row.item)">编辑</b-button>
          <!--<b-button class="btn-danger" @click="row.toggleDetails">-->
            <!--{{ row.detailsShowing ? '取消删除' : '删除'}}</b-button>-->
        </template>
        <!--<template slot="row-details" slot-scope="row">-->
          <!--<b-card>-->
            <!--<b-row class="mb-6">-->
              <!--<b-col class="text-sm-right"><b>一级项目ID：</b></b-col>-->
              <!--<b-col>{{ row.item.id}}</b-col>-->
              <!--<b-col class="text-sm-right"><b>一级项目名称：</b></b-col>-->
              <!--<b-col class="text-sm-left">{{ row.item.TOP_Project_name}}</b-col>-->
              <!--<b-col class="text-sm-right"><b>一级项目描述：</b></b-col>-->
              <!--<b-col class="text-sm-left">{{ row.item.TOP_Project_desc}}</b-col>-->
            <!--</b-row>-->
            <!--<hr>-->
            <!--<b-row class="mb-6">-->
              <!--<b-col class="text-sm-right"><b>二级项目ID：</b></b-col>-->
              <!--<b-col>{{ row.item.Second_Project_id}}</b-col>-->
              <!--<b-col class="text-sm-right"><b>二级项目名称：</b></b-col>-->
              <!--<b-col class="text-sm-left">{{ row.item.Second_Project_name}}</b-col>-->
              <!--<b-col class="text-sm-right"><b>二级项目描述：</b></b-col>-->
              <!--<b-col class="text-sm-left">{{ row.item.Second_Project_description}}</b-col>-->
            <!--</b-row>-->
            <!--<hr>-->
            <!--<b-button class="btn-danger" @click="deleteProject(2, row.item)">确定删除上述信息?</b-button>-->
          <!--</b-card>-->
        <!--</template>-->
      </b-table>
      </b-row>
      <div class="row" style="text-align: center;">
        <div class="col-md-4" style="text-align: left;">
          <b-button type="button" variant="success" v-b-modal.addUserCheckInfo-Modal @click="''">单条添加</b-button>
          <b-button type="button" variant="primary" v-b-modal.topProjectInfo-modal @click="getTopProjects(2)">管理一级项目</b-button>
        </div>
        <div class="col-md-4">
          <b-pagination
            :total-rows="totalRows"
            :per-page="perPage"
            v-model="currentPage"
            aria-controls="projectsTable"
            ></b-pagination>
        </div>
        <div class="col-md-4">二级项目总数:&nbsp;<b>{{ totalRows }}</b>,&nbsp;当前第{{ currentPage }}页&nbsp;</div>
      </div>
      <b-modal id="addUserCheckInfo-Modal" title="添加打卡信息" class="text-left" hide-footer>
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
              <b-input></b-input>
            </b-input-group>
        </b-form-group>
          <!--</b-col>-->
          <!--<b-col>-->
        <b-form-group description="打卡时间格式YYYY-MM-DD hh:mm:ss 例如2019-03-21 19:00:00">
            <b-input-group prepend="下班打卡时间:">
              <b-input></b-input>
            </b-input-group>
        </b-form-group>
          <!--</b-col>-->
        <b-form-group label="有特殊打卡说明吗?">
          <b-form-textarea placeholder="打卡说明" rows="3" id="check_desc"></b-form-textarea>
        </b-form-group>
        <b-button type="submit" variant="primary">添加记录</b-button>
        <b-button type="reset" variant="danger">重置</b-button>
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
      items: []
    }
  },
  methods: {
    getUsersCheck () {
      const path = 'http://localhost:5000/api/userscheck'
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
            this.options.push({
              'value': res.data.results[i].userid,
              'text': res.data.results[i].username
            })
            // console.log(this.items)
            this.totalRows = this.items.length
          }
        })
        .catch((error) => {
          console.error(error)
        })
    },
    onSubmit (evt) {
      evt.preventDefault()
    },
    onReset (evt) {
      evt.preventDefault()
    }
  },
  created () {
    this.getUsersCheck()
  }
}
</script>

<style scoped>

</style>
