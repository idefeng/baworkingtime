<template>
    <el-header style="padding: 0;">
      <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b">
        <el-menu-item index="1">技术部大盘</el-menu-item>
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
        <el-menu-item index="3" disabled>消息中心</el-menu-item>
        <el-menu-item index="4"><a href="#">个人中心</a></el-menu-item>
      </el-menu>
    </el-header>
    <!--<div>-->
      <!--<b-navbar toggleable="lg" type="dark" variant="success">-->
        <!--<b-navbar-brand href="/">首页</b-navbar-brand>-->
    <!---->
        <!--<b-navbar-toggle target="nav_collapse" />-->
    <!---->
        <!--<b-collapse is-nav id="nav_collapse">-->
          <!--<b-navbar-nav>-->
            <!--<b-nav-item href="/Users"><b>用户管理</b></b-nav-item>-->
            <!--<b-nav-item href="/Projects"><b>项目管理</b></b-nav-item>-->
            <!--<b-nav-item href="/Userscheck"><b>打卡管理</b></b-nav-item>-->
            <!--<b-nav-item href="/workdiary"><b>日志管理</b></b-nav-item>-->
            <!--&lt;!&ndash;<b-nav-item href="#" disabled><b>Disabled</b></b-nav-item>&ndash;&gt;-->
          <!--</b-navbar-nav>-->
    <!---->
          <!--&lt;!&ndash; Right aligned nav items &ndash;&gt;-->
          <!--<b-navbar-nav class="ml-auto">-->
            <!--<b-nav-form>-->
              <!--<b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search" />-->
              <!--<b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>-->
            <!--</b-nav-form>-->
    <!---->
            <!--<b-nav-item-dropdown text="语言" right>-->
              <!--<b-dropdown-item href="#">简体中文</b-dropdown-item>-->
              <!--<b-dropdown-item href="#">EN</b-dropdown-item>-->
              <!--<b-dropdown-item href="#">ES</b-dropdown-item>-->
              <!--<b-dropdown-item href="#">RU</b-dropdown-item>-->
              <!--<b-dropdown-item href="#">FA</b-dropdown-item>-->
            <!--</b-nav-item-dropdown>-->
    <!---->
            <!--<b-nav-item-dropdown right>-->
              <!--&lt;!&ndash; Using button-content slot &ndash;&gt;-->
              <!--<template slot="button-content"><em>用户中心</em></template>-->
              <!--<b-dropdown-item href="#">个人中心</b-dropdown-item>-->
              <!--<b-dropdown-item href="#">退出</b-dropdown-item>-->
            <!--</b-nav-item-dropdown>-->
          <!--</b-navbar-nav>-->
        <!--</b-collapse>-->
      <!--</b-navbar>-->
    <!--</div>-->
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
