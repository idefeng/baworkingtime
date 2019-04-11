<template>
  <div style="height: 100%;">
    <el-row>
      <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#1D1E2E"
        text-color="#fff"
        active-text-color="#ffd04b"
        style="border-color: #26293C;">
        <el-menu-item index="1"><span STYLE="font-weight: bolder;font-size: 20px;">ETLCHINA R&D DEPARTMENT</span> </el-menu-item>
        <el-menu-item index="2" style="float:right;"><span class="el-icon-setting"></span></el-menu-item>
        <el-menu-item index="3" style="float:right;">
          <a href="#">
            <span class="el-icon-message">
              <el-badge is-dot style="margin-top: 0px;"></el-badge>
            </span>
          </a>
        </el-menu-item>
        <el-menu-item index="4" style="float:right;"><a href="#">
          <b-img src="xxx.jpg" rounded="circle" alt="xxx"></b-img>
        </a></el-menu-item>
      </el-menu>
    </el-row>
    </div>
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
