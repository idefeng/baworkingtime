<template>
  <div id="app" style="margin-top: 0px;margin-right: 10px;">
    <el-container>
      <!--<el-header>Header</el-header>-->
      <Header/>
      <el-row>
      <Aside/>
      <el-col :span="20">
        <router-view/>
      </el-col>
      </el-row>
      <br>
      <el-footer>
        <p style="text-align: center">北京博奥网络教育科技股份有限公司 技术部</p>
      </el-footer>
      <!--<img src="./assets/logo.png">-->
    </el-container>
  </div>
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
