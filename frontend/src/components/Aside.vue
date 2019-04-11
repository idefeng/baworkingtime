<template>
  <div style="background-color: #1D1E2E;height: 100%;">
    <el-row class="nav-aside">
        <el-menu
            default-active="2"
            @open="handleOpen"
            @close="handleClose"
            background-color="#4BB181"
            text-color="#fff"
            active-text-color="#ffd04b"
            style="border-radius: 10px;"
        >
            <el-menu-item index="1">
              <i class="el-icon-location"></i>
              <span slot="title"><a href="/Dashboard">绩效统计</a> </span>
            </el-menu-item>
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
    </el-row>
  </div>
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
