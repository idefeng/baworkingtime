<template>
    <el-menu
        :default-active="activeIndex"
        @open="handleOpen"
        @close="handleClose"
        @select="handleSelect"
        background-color="#1D1E2E"
        text-color="#fff"
        active-text-color="#ffd04b"
    >
        <el-menu-item index="1">
          <i class="el-icon-location"></i>
          <span slot="title"><a href="/Dashboard" style="color: #fff;">绩效统计</a> </span>
        </el-menu-item>
        <el-menu-item index="2">
          <a href="/Users" style="color: #fff;">
            <i class="el-icon-menu"></i>
            <span slot="title">用户管理</span>
          </a>
        </el-menu-item>
        <el-menu-item index="3">
          <i class="el-icon-document"></i>
          <span slot="title"><a href="/Projects" style="color: #fff;">项目管理</a></span>
        </el-menu-item>
        <el-menu-item index="4">
          <i class="el-icon-bell"></i>
          <span slot="title"><a href="/Userscheck" style="color: #fff;">打卡管理</a></span>
        </el-menu-item>
        <el-menu-item index="5">
          <i class="el-icon-date"></i>
          <span slot="title"><a href="/workdiary" style="color: #fff;">日志管理</a></span>
        </el-menu-item>
    </el-menu>
</template>

<script>
export default {
  name: 'Aside',
  data () {
    return {
      activeIndex: '1'
    }
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    },
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>

</style>
