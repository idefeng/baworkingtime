<template>
    <div>
<!--      <h1>公司项目管理</h1>-->
      <el-row>
      <el-table
        id="projectsTable"
        striped
        hover
        :data="items"
      >
        <el-table-column type="index"></el-table-column>
        <el-table-column
          fixted
        prop="TOP_Project_name"
        label="一级项目名称"
        sortable
        >
          <template  slot-scope="data">
            {{ data.row.TOP_Project_name }}
          </template>
        </el-table-column>
        <el-table-column prop="Second_Project_name" label="二级项目名称">
            <template  slot-scope="data">
              {{ data.row.Second_Project_name }}
            </template>
          </el-table-column>
        <el-table-column prop="Second_Project_Description" label="二级项目描述">
            <template  slot-scope="data">
              {{ data.row.Second_Project_description }}
            </template>
          </el-table-column>
        <el-table-column label="操作">
          <template  slot-scope="data">
            <el-button type="warning"  @click="editProject(data.row)">编辑</el-button>
            <el-button type="danger" @click="deleteProjectDialogShow = true">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      </el-row>
      <div class="row" style="text-align: center;">
        <div class="col-md-4" style="text-align: left;">
          <el-button type="success" @click="popAddProject">添加项目</el-button>
          <b-button type="primary" v-b-modal.topProjectInfo-modal @click="getTopProjects(2)">管理一级项目</b-button>
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
      <!-- 添加项目信息 -->
      <el-dialog
        id="addProjectInfo"
        title="添加新项目信息"
        :visible.sync="addProjectInfoShow"
        center
        width="30%"
        >
        <el-form v-model="projectForm" label-width="20%">
          <el-form-item label="一级项目">
            <el-select v-model="selected" label="请选择一个项目" :options="project_options" >
              <el-option
                v-for="option in project_options"
                :key="option.value"
                :label="option.label"
                :value="option.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="二级项目名称">
          <el-input v-model="projectForm.project2_name" placeholder="请输入二级项目名称:" />
          </el-form-item>
          <br>
        <el-form-item label="二级项目描述">
          <el-input type="textarea" rows="2" v-model="projectForm.project2_desc" placeholder="请输入二级项目描述" />
        </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onOKAdd">添加</el-button>
            <el-button type="danger" @click="onCancelAdd">取消</el-button>
          </el-form-item>
      </el-form>
      </el-dialog>
      <!-- 更新项目信息 -->
      <el-dialog
        id="editProjectInfo"
        title="编辑项目信息"
        :visible.sync="editProjectInfoShow"
        center
        width="30%"
        >
        <el-form :model="editProjectForm" label-width="30%">
          <el-form-item label="所属一级项目">
            <el-select v-model="selected" placeholder="请选择">
              <el-option
                v-for="option in project_options"
                :key="option.value"
                :label="option.label"
                :value="option.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="二级项目名称">
          <el-input v-model="editProjectForm.Second_Project_name"/>
        </el-form-item>
        <el-form-item label="二级项目描述">
          <el-input type="textarea" :rows="2" v-model="editProjectForm.Second_Project_description"/>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmitUpdateProject">更新</el-button>
          <el-button type="danger" @click="onResetUpdateProject">重置</el-button>
        </el-form-item>
      </el-form>
      </el-dialog>
      <!-- 删除项目信息确认对话框 -->
      <el-dialog
      title="确认删除项目信息?"
      :visible.sync="deleteProjectDialogShow"
      width="30%"
      :model="editProjectForm"
      center>
      <span style="text-align: center">确认要删除此项目信息?</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="deleteProject(2, editProjectForm)" type="danger">删除</el-button>
        <el-button @click="''" type="info">取消删除</el-button>
      </span>
    </el-dialog>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Projects',
  data () {
    return {
      topProjectInfoFields: {
        TOP_Project_id: {
          label: '序号',
          sortable: true
        },
        TOP_Project_name: {
          label: '一级项目名称',
          sortable: true
        },
        TOP_Project_desc: {
          label: '一级项目描述'
        },
        Actions: {
          label: '操作'
        }
      },
      addProjectInfoShow: false,
      editProjectInfoShow: false,
      deleteProjectDialogShow: false,
      items: [],
      topProjectInfoItems: [],
      totalRows: 0,
      perPage: 10,
      currentPage: 1,
      selected: null,
      selectedRow: [],
      project_options: [],
      topProjectForm: {
        project_name: '',
        project_desc: ''
      },
      projectForm: {
        project1_id: '',
        project2_name: '',
        project2_desc: ''
      },
      editProjectForm: {}
    }
  },
  methods: {
    // 获取二级项目信息
    getProjects () {
      const path = 'http://localhost:5000/api/projects/3'
      this.items = []
      axios.get(path)
        .then((res) => {
          console.log(res.data.projects)
          for (let i = 0; i < res.data.projects.length; i++) {
            this.items.push({'id': res.data.projects[i].id,
              'TOP_Project_name': res.data.projects[i].project_name,
              'TOP_Project_desc': res.data.projects[i].project_desc,
              'Second_Project_id': res.data.projects[i].level2id,
              'Second_Project_name': res.data.projects[i].level2projectname,
              'Second_Project_description': res.data.projects[i].level2projectdesc})
          }
          this.totalRows = this.items.length
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getTopProjects (typeID) {
      const path = 'http://localhost:5000/api/projects/1'
      this.project_options = []
      this.topProjectInfoItems = []
      axios.get(path)
        .then((res) => {
          // console.log(res.data.projects)
          if (typeID === 1) {
            for (let i = 0; i < res.data.projects.length; i++) {
              this.project_options.push({'value': res.data.projects[i].id,
                'label': res.data.projects[i].project_name})
            }
            // console.log(this.project_options)
          } else if (typeID === 2) {
            for (let i = 0; i < res.data.projects.length; i++) {
              this.topProjectInfoItems.push({'TOP_Project_id': res.data.projects[i].id,
                'TOP_Project_name': res.data.projects[i].project_name,
                'TOP_Project_desc': res.data.projects[i].project_desc})
            }
            // console.log(this.topProjectInfoItems)
          }
        })
        .catch((error) => {
          console.error(error)
        })
    },
    popAddProject () {
      this.addProjectInfoShow = true
      this.getTopProjects(1)
    },
    addProject (typeID, payload) {
      const path = `http://localhost:5000/api/projects/${typeID}`
      axios.post(path, payload)
        .then(() => {
          this.getProjects()
          // this.getTopProjects()
        })
        .catch((error) => {
          console.error(error)
          this.getProjects()
        })
    },
    initForm () {
      // this.items = []
      this.projectForm.project1_id = ''
      this.projectForm.project2_name = ''
      this.projectForm.project2_desc = ''
      this.topProjectForm.project_name = ''
      this.topProjectForm.project_desc = ''
      this.editProjectForm = {}
      this.selected = null
    },
    onOKAdd (evt) {
      evt.preventDefault()
      const payload = {
        parent_project: this.selected,
        project2_name: this.projectForm.project2_name,
        project2_desc: this.projectForm.project2_desc
      }
      this.addProject('2', payload)
      this.addProjectInfoShow = false
      this.initForm()
    },
    onCancelAdd (evt) {
      evt.preventDefault()
      this.addProjectInfoShow = false
      this.initForm()
    },
    // 编辑项目信息
    editProject (project) {
      this.getTopProjects(1)
      this.editProjectInfoShow = true
      console.log(project)
      this.editProjectForm = project
      this.selected = this.editProjectForm.id
      // console.log(this.editProjectForm)
    },
    updateProject (typeID, projectID, payload) {
      const path = `http://localhost:5000/api/projects/${typeID}/${projectID}`
      axios.put(path, payload)
        .then(() => {
          this.getProjects()
        })
        .catch((error) => {
          console.error(error)
          this.getProjects()
        })
    },
    onSubmitUpdateProject (evt) {
      evt.preventDefault()
      this.editProjectInfoShow = false
      const payload = {
        parent_project: this.selected,
        project2_name: this.editProjectForm.Second_Project_name,
        project2_desc: this.editProjectForm.Second_Project_description
      }
      this.updateProject('2', this.editProjectForm.Second_Project_id, payload)
    },
    onResetUpdateProject (evt) {
      evt.preventDefault()
      this.editProjectInfoShow = false
      this.initForm()
      this.getProjects()
    },
    removeProject (typeID, projectID) {
      const path = `http://localhost:5000/api/projects/${typeID}/${projectID}`
      axios.delete(path)
        .then(() => {
          if (typeID === '1') {
            this.getProjects()
          } else if (typeID === '2') {
            this.getTopProjects(2)
          }
        })
        .catch((error) => {
          console.error(error)
          if (typeID === '1') {
            this.getProjects()
          } else if (typeID === '2') {
            this.getTopProjects(2)
          }
        })
    },
    // 删除二级项目
    deleteProject (typeID, project) {
      console.log(typeID)
      if (typeID === 1) {
        this.removeProject('1', project.TOP_Project_id)
        this.getTopProjects(2)
      } else if (typeID === 2) {
        this.removeProject('2', project.Second_Project_id)
      }
    }
  },
  created () {
    this.getProjects()
  }
}
</script>

<style scoped>

</style>
