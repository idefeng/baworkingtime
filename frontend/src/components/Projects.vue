<template>
    <div class="container">
      <h1>公司项目管理</h1>
      <b-row>
        <b-col md="6" class="my-3">
          <b-form-group label-cols-sm="3" class="mb-1">
            <b-input-group prepend="筛查">
              <b-form-input v-model="filter" placeholder="输入关键字搜索" />
              <b-input-group-append>
                <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
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
        <template slot="Actions" slot-scope="row">
          <b-button class="btn-warning" v-b-modal.editProjectInfo @click="editProject(row.item)">编辑</b-button>
          <b-button class="btn-danger" @click="row.toggleDetails">
            {{ row.detailsShowing ? '取消删除' : '删除'}}</b-button>
        </template>
        <template slot="row-details" slot-scope="row">
          <b-card>
            <b-row class="mb-6">
              <b-col class="text-sm-right"><b>一级项目ID：</b></b-col>
              <b-col>{{ row.item.id}}</b-col>
              <b-col class="text-sm-right"><b>一级项目名称：</b></b-col>
              <b-col class="text-sm-left">{{ row.item.TOP_Project_name}}</b-col>
              <b-col class="text-sm-right"><b>一级项目描述：</b></b-col>
              <b-col class="text-sm-left">{{ row.item.TOP_Project_desc}}</b-col>
            </b-row>
            <hr>
            <b-row class="mb-6">
              <b-col class="text-sm-right"><b>二级项目ID：</b></b-col>
              <b-col>{{ row.item.Second_Project_id}}</b-col>
              <b-col class="text-sm-right"><b>二级项目名称：</b></b-col>
              <b-col class="text-sm-left">{{ row.item.Second_Project_name}}</b-col>
              <b-col class="text-sm-right"><b>二级项目描述：</b></b-col>
              <b-col class="text-sm-left">{{ row.item.Second_Project_description}}</b-col>
            </b-row>
            <hr>
            <b-button class="btn-danger" @click="deleteProject(2, row.item)">确定删除上述信息?</b-button>
          </b-card>
        </template>
      </b-table>
      </b-row>
      <div class="row" style="text-align: center;">
        <div class="col-md-4" style="text-align: left;">
          <b-button type="button" variant="success" v-b-modal.addProjectInfo @click="getTopProjects(1)">添加项目</b-button>
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
      <!-- 添加项目信息 -->
      <b-modal
        id="addProjectInfo"
        ref="projectInfoRef"
        title="添加新项目信息"
        ok-title="添加"
        @ok="onOKAdd"
        cancel-title="重置"
        @cancel="onCancelAdd"
        >
        <b-form class="w-100">
          <b-input-group
            id="toplevelproject"
            prepend="请选择一个一级项目"
            label-for="top_level_project">
            <b-form-select v-model="selected" :options="project_options" >
              <template slot="first">
                <option :value="null" disabled>请选择一个项目</option>
              </template>
            </b-form-select>
            <b-input-group-append>
              <b-button variant="success" v-b-modal.addTopProject-modal>添加新项目</b-button>
            </b-input-group-append>
          </b-input-group>
          <br>
          <b-input-group
          id="secondlevelprojectname"
          prepend="请输入二级项目名称"
          label-for="second_level_project_name">
          <b-form-input type="text"
                        id="second_level_project_name"
                        v-model="projectForm.project2_name"
                        required
                        aria-placeholder="请输入二级项目名称:" />
        </b-input-group>
          <br>
        <b-input-group
          id="secondlevelprojectdesc"
          prepend="请输入二级项目描述"
          label-for="second_level_project_desc">
          <b-form-input type="text"
                        id="second_level_project_desc"
                        v-model="projectForm.project2_desc"
                        required
                        aria-placeholder="请输入二级项目描述" />
        </b-input-group>
        <!--<b-button type="submit" variant="primary">Update</b-button>-->
        <!--<b-button type="reset" variant="danger">Cancel</b-button>-->
      </b-form>
      </b-modal>
      <!-- 添加一级项目 -->
      <b-modal
            id="addTopProject-modal"
            title="添加一级项目信息"
            ref="addTopProjectRef"
            hide-footer
            >
            <b-form ref="addtoproject"
                  id="add_top_project_modal"
                  @submit="onSubmitAddProject"
                  @reset="onResetAddProject"
                  >
              <b-input-group
                id="addtopproject"
                prepend="请输入一级项目名称"
                label-for="top_level_project_name" >
                <b-form-input type="text"
                              id="top_level_project_name"
                              v-model="topProjectForm.project_name"
                              required
                              aria-placeholder="请输入一级项目名称：" />
              </b-input-group>
              <br>
              <b-input-group
                id="addtopprojectdesc"
                prepend="请输入一级项目描述"
                label-for="top_level_project_desc" >
                <b-form-input type="text"
                              id="top_level_project_desc"
                              v-model="topProjectForm.project_desc"
                              required
                              aria-placeholder="请输入一级项目描述：" />
              </b-input-group>
              <br>
              <b-button type="submit" variant="primary" >添加项目</b-button>
              <b-button type="reset" variant="danger" >重置</b-button>
            </b-form>
      </b-modal>
      <!-- 更新项目信息 -->
      <b-modal
        id="editProjectInfo"
        ref="editProjectInfoRef"
        title="编辑项目信息"
        hide-footer
        >
        <b-form
          class="w-100"
          @submit="onSubmitUpdateProject"
          @reset="onResetUpdateProject">
          <b-input-group
            id="topLevelProject_for_Edit"
            prepend="选择一个一级项目"
            label-for="top_level_project">
            <b-form-select v-model="selected" :options="project_options" >
            </b-form-select>
            <b-input-group-append>
              <b-button variant="success" v-b-modal.addTopProject-modal>添加项目</b-button>
            </b-input-group-append>
          </b-input-group>
          <br>
          <b-input-group
          id="secondLevelProject_for_Edit"
          prepend="编辑二级项目名称"
          label-for="second_level_project_for_edit">
          <b-form-input type="text"
                        id="second_level_project_for_edit"
                        v-model="editProjectForm.Second_Project_name"
                        required
                        aria-placeholder="编辑二级项目名称:" />
        </b-input-group>
          <br>
        <b-input-group
          id="secondLevelProjectDesc_for_Edit"
          prepend="编辑二级项目描述"
          label-for="second_level_project_desc_for_edit">
          <b-form-input type="text"
                        id="second_level_project_desc_for_edit"
                        v-model="editProjectForm.Second_Project_description"
                        required
                        aria-placeholder="编辑二级项目描述" />
        </b-input-group>
          <br>
        <b-button type="submit" variant="primary">更新</b-button>
        <b-button type="reset" variant="danger">重置</b-button>
      </b-form>
      </b-modal>
      <!-- 一级项目信息展示 -->
      <b-modal
        id="topProjectInfo-modal"
        ref="topProjectInfoRef"
        title="一级项目信息"
        size="lg"
        hide-footer>
        <b-table
          id="topProjectInfoTable"
          show-empty
          empty-text="无数据可加载..."
          striped
          hover
          :fields="topProjectInfoFields"
          :items="topProjectInfoItems">
          <template slot="Actions" slot-scope="row">
            <b-button class="btn-danger" @click="deleteProject(1, row.item)">删除</b-button>
          </template>
        </b-table>
      </b-modal>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Projects',
  data () {
    return {
      fields: {
        index: {
          label: '序号'
          // variant: 'success'
        },
        TOP_Project_name: {
          label: '一级项目名称',
          sortable: true
          // variant: 'success'
        },
        Second_Project_name: {
          label: '二级项目名称'
        },
        Second_Project_description: {
          label: '项目描述'
        },
        Actions: {
          label: '操作'
        }
      },
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
      filter: null,
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
  computed: {
    sortOptions () {
      return this.fields
        .filter(f => f.sortable)
        .map(f => {
          return {text: f.label, value: f.key}
        })
    }
  },
  methods: {
    getProjects () {
      const path = 'http://localhost:5000/api/projects/3'
      this.items = []
      axios.get(path)
        .then((res) => {
          // console.log(res.data.projects)
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
                'text': res.data.projects[i].project_name})
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
    onSubmitAddProject (evt) {
      evt.preventDefault()
      const payload = {
        project_name: this.topProjectForm.project_name,
        project_desc: this.topProjectForm.project_desc
      }
      this.addProject('1', payload)
      this.getTopProjects()
      this.$refs.addTopProjectRef.hide()
      this.initForm()
    },
    onResetAddProject (evt) {
      evt.preventDefault()
      this.$refs.addTopProjectRef.hide()
      this.initForm()
    },
    onOKAdd (evt) {
      evt.preventDefault()
      const payload = {
        parent_project: this.selected,
        project2_name: this.projectForm.project2_name,
        project2_desc: this.projectForm.project2_desc
      }
      this.addProject('2', payload)
      this.$refs.projectInfoRef.hide()
      this.initForm()
    },
    onCancelAdd (evt) {
      evt.preventDefault()
      this.$refs.projectInfoRef.hide()
      this.initForm()
    },
    editProject (project) {
      this.getTopProjects()
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
      this.$refs.editProjectInfoRef.hide()
      const payload = {
        parent_project: this.selected,
        project2_name: this.editProjectForm.Second_Project_name,
        project2_desc: this.editProjectForm.Second_Project_description
      }
      this.updateProject('2', this.editProjectForm.Second_Project_id, payload)
    },
    onResetUpdateProject (evt) {
      evt.preventDefault()
      this.$refs.editProjectInfoRef.hide()
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
    deleteProject (typeID, project) {
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
