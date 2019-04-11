<template>
  <div id="app" style="margin: 0px;">
    <!--<el-container id="app" direction="vertical" style="margin: 0;">-->
      <!--<el-header>Header</el-header>-->
      <!--<el-header style="width: 100%;padding: 0;">-->
        <Header/>
      <!--</el-header>-->
      <!--<el-container>-->
        <!--<el-aside width="200px">-->
          <!--<Aside/>-->
        <!--</el-aside>-->
        <!--&lt;!&ndash;<el-row>&ndash;&gt;-->
        <!--<el-main style="background-color: #1D1E2E;">-->
          <!--<router-view/>-->
        <!--</el-main>-->
      <div class="content">
        <el-row style="margin-right: 15px;">
          <el-col :span="4">
            <Aside />
          </el-col>
          <el-col :span="20" style="margin-top: 15px;">
            <router-view/>
          </el-col>
        </el-row>
        <el-row style="background-color: #1D1E2E;height: 50px;">
        <el-col :span="24">
          <p style="text-align: center;">北京博奥网络教育科技股份有限公司 技术部</p>
        </el-col>
      </el-row>
      </div>
      <!--</el-container>-->
      <!--<el-col :span="20">-->

      <!--</el-col>-->
      <!--</el-row>-->
      <!--<img src="./assets/logo.png">-->
    <!--</el-container>-->
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
