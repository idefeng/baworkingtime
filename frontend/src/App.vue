<template>
  <el-container id="app" style="margin: 0px; background-color: #1D1E2E;">
      <el-header style="padding: 0;">
          <Header/>
      </el-header>
      <el-container>
          <el-aside  width="200px">
            <Aside />
          </el-aside>
          <el-main>
            <router-view/>
          </el-main>
      </el-container>
      <el-container>
        <el-footer>
          <p style="text-align: center;">北京博奥网络教育科技股份有限公司 研发与运营中心</p>
        </el-footer>
      </el-container>
  </el-container>
</template>

<script>
import Header from './components/Header'
import Aside from './components/Aside'
import Footer from './components/Footer'

export default {
  name: 'App',
  components: {Footer, Aside, Header}
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
