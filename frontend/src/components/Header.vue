<template>
<!--  <div style="height: 100%;">-->
<!--    <el-row>-->
      <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#1D1E2E"
        text-color="#fff"
        active-text-color="#ffd04b"
        style="border-color: #26293C;">
        <el-menu-item index="1"><span STYLE="font-weight: bolder;font-size: 20px;"><a href="/Dashboard">ETLCHINA R&D DEPARTMENT</a></span> </el-menu-item>
        <el-submenu index="2">
          <template slot="title"><i class="el-icon-location"></i>工作台</template>
          <el-menu-item index="2-1"><a href="/Users"><i class="el-icon-menu"></i>部门用户管理</a></el-menu-item>
          <el-menu-item index="2-2"><a href="/Projects"><i class="el-icon-document"></i>部门项目管理</a> </el-menu-item>
          <el-menu-item index="2-3"><a href="/Userscheck"><i class="el-icon-bell"></i>部门考勤管理</a> </el-menu-item>
          <el-menu-item index="2-4"><a href="/WorkDiary"><i class="el-icon-date"></i>部门日志管理</a> </el-menu-item>
          <hr>
          <el-menu-item index="2-5"><a href="/Dashboard"><i class="el-icon-menu"></i>返回首页</a> </el-menu-item>
        </el-submenu>
        <el-menu-item index="3" style="float:right;"><span class="el-icon-setting"></span></el-menu-item>
        <el-menu-item index="4" style="float:right;">
          <a href="#">
            <span class="el-icon-message">
              <el-badge is-dot style="margin-top: 0px;"></el-badge>
            </span>
          </a>
        </el-menu-item>
        <el-menu-item index="4" style="float:right;"><a href="#">
          <b-img src="xxx.jpg" rounded="circle" alt="xxx"></b-img>
        </a></el-menu-item>
      </el-menu>
<!--    </el-row>-->
<!--    </div>-->
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
      activeIndex: '1'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>

</style>
