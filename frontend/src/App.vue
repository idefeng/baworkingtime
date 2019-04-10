<template>
  <!--<div id="app" style="margin: 0px;">-->
    <el-container id="app" direction="vertical" style="margin: 0;">
      <!--<el-header>Header</el-header>-->
      <el-header style="width: 100%;padding: 0;">
        <Header/>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <Aside/>
        </el-aside>
        <!--<el-row>-->
        <el-main style="background-color: #1D1E2E;">
          <router-view/>
        </el-main>
      </el-container>
      <!--<el-col :span="20">-->

      <!--</el-col>-->
      <!--</el-row>-->
      <el-footer>
        <p style="text-align: center">北京博奥网络教育科技股份有限公司 技术部</p>
      </el-footer>
      <!--<img src="./assets/logo.png">-->
    </el-container>
  <!--</div>-->
</template>

<script>
import Header from './components/Header'
import Aside from './components/Aside'
import Footer from './components/Footer'
import Main from './components/Main'

export default {
  name: 'App',
  components: {Main, Footer, Aside, Header}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
