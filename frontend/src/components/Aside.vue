<template>
    <!--<el-col :span="24">-->
      <!--<el-row>-->
        <el-menu
            default-active="2"
            @open="handleOpen"
            @close="handleClose"
            background-color="#1D1E2E"
            text-color="#fff"
            active-text-color="#ffd04b"
            style="margin: 0; height: 100%; border-color: #26293C;"
        >
            <el-submenu index="1">
              <template slot="title" >
                <i class="el-icon-location"></i>
                <span>绩效仪表盘</span>
              </template>
              <el-menu-item-group style="right: 0;">
                <!--<template slot="title">绩效排行</template>-->
                <el-menu-item index="1-1"><a href="/Dashboard">绩效统计</a> </el-menu-item>
                <el-menu-item index="1-2">选项2</el-menu-item>
              </el-menu-item-group>
              <!--<el-menu-item-group title="分组2">-->
                <!--<el-menu-item index="1-3">选项3</el-menu-item>-->
              <!--</el-menu-item-group>-->
              <!--<el-submenu index="1-4">-->
                <!--<template slot="title">选项4</template>-->
                <!--<el-menu-item index="1-4-1">选项1</el-menu-item>-->
              <!--</el-submenu>-->
            </el-submenu>
            <el-menu-item index="2">
              <i class="el-icon-menu"></i>
              <span slot="title"><a href="/Users">用户管理</a></span>
            </el-menu-item>
            <el-menu-item index="3">
              <i class="el-icon-document"></i>
              <span slot="title"><a href="/Projects">项目管理</a></span>
            </el-menu-item>
            <el-menu-item index="4">
              <i class="el-icon-bell"></i>
              <span slot="title"><a href="/Userscheck">打卡管理</a></span>
            </el-menu-item>
            <el-menu-item index="5">
              <i class="el-icon-date"></i>
              <span slot="title"><a href="/workdiary">日志管理</a></span>
            </el-menu-item>
          </el-menu>
      <!--</el-row>-->
    <!--</el-col>-->
</template>

<script>
export default {
  name: 'Aside',
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>

</style>
