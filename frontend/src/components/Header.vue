<template>
    <!--<el-row>-->
      <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b">
        <el-menu-item index="1"><img src="../../static/images/logo.png" /> </el-menu-item>
        <el-submenu index="2">
          <template slot="title">我的工作台</template>
          <el-menu-item index="2-1"><a href="/Users">用户管理</a></el-menu-item>
          <el-menu-item index="2-2"><a href="/Projects">项目管理</a></el-menu-item>
          <el-menu-item index="2-3"><a href="/Userscheck">打卡管理</a></el-menu-item>
          <el-menu-item index="2-4"><a href="/workdiary">日志管理</a></el-menu-item>
          <!--<el-submenu index="2-4">-->
            <!--<template slot="title">选项4</template>-->
            <!--<el-menu-item index="2-4-1">选项1</el-menu-item>-->
            <!--<el-menu-item index="2-4-2">选项2</el-menu-item>-->
            <!--<el-menu-item index="2-4-3">选项3</el-menu-item>-->
          <!--</el-submenu>-->
        </el-submenu>
        <el-menu-item index="3" style="text-align:right;">消息中心</el-menu-item>
        <el-menu-item index="4" style="float:right;"><a href="#">个人中心</a></el-menu-item>
        <el-menu-item index="4" style="float:right;"><a href="#">设置</a></el-menu-item>
      </el-menu>
    <!--</el-row>-->
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
