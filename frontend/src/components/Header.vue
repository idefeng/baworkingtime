<template>
    <div>
  <b-navbar toggleable="lg" type="dark" variant="success">
    <b-navbar-brand href="/">首页</b-navbar-brand>

    <b-navbar-toggle target="nav_collapse" />

    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav>
        <b-nav-item href="/Users"><b>用户管理</b></b-nav-item>
        <b-nav-item href="/Projects"><b>项目管理</b></b-nav-item>
        <b-nav-item href="/Userscheck"><b>打卡管理</b></b-nav-item>
        <b-nav-item href="/workdiary"><b>日志管理</b></b-nav-item>
        <!--<b-nav-item href="#" disabled><b>Disabled</b></b-nav-item>-->
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search" />
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>

        <b-nav-item-dropdown text="语言" right>
          <b-dropdown-item href="#">简体中文</b-dropdown-item>
          <b-dropdown-item href="#">EN</b-dropdown-item>
          <b-dropdown-item href="#">ES</b-dropdown-item>
          <b-dropdown-item href="#">RU</b-dropdown-item>
          <b-dropdown-item href="#">FA</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown right>
          <!-- Using button-content slot -->
          <template slot="button-content"><em>用户中心</em></template>
          <b-dropdown-item href="#">个人中心</b-dropdown-item>
          <b-dropdown-item href="#">退出</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style scoped>

</style>
