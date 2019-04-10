<template>
  <div>
    <el-row :gutter="5" style="margin-bottom: 10px;">
      <el-col :span="6">
        <el-card style="background-color: #26293C; border-color: #26293C;">
          <el-row><span class="dashboard-first">部门人数（在职）<br>DEPARTMENT</span></el-row>
          <el-row><span class="dashboard-number">37</span></el-row>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card style="background-color: #26293C; border-color: #26293C;">
          <el-row><span class="dashboard-first">项目数量（活跃）<br>PROJECTS</span></el-row>
          <el-row><span class="dashboard-number">20</span></el-row>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card style="background-color: #26293C; border-color: #26293C;">
          <el-row><span class="dashboard-first">平均加班（上月）<br>WORKTIME</span></el-row>
          <el-row><span class="dashboard-number">57</span> <span style="color: #ffffff;"> Hours</span></el-row>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card style="background-color: #26293C; border-color: #26293C;">
          <el-row><span class="dashboard-first">其他<br>OTHERS</span></el-row>
          <el-row><span class="dashboard-number">...</span></el-row>
        </el-card>
      </el-col>
    </el-row>
    <el-row style="margin-bottom: 10px;">
      <el-col :span="24">
        <el-card style="background-color: #26293C; border-color: #26293C;">
          <ve-line :data="chartData" :settings="chartSettings" :extend="chartExtend"></ve-line>
        </el-card>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card style="background-color: #26293C; border-color: #26293C;">
          <div slot="header">
            <span class="dashboard-header">绩效排行榜</span>
            <div style="margin-bottom: 3px;"><el-button style="float: right; padding: 3px 0;" type="text">查看更多</el-button></div>
          </div>
          <div>
            <el-row class="dashboard-list">
              <el-col :span="2">1</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
            <el-row class="dashboard-list">
              <el-col :span="2">2</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
            <el-row class="dashboard-list">
              <el-col :span="2">3</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
            <el-row class="dashboard-list">
              <el-col :span="2">4</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
            <el-row class="dashboard-list">
              <el-col :span="2">5</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
          </div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card style="background-color: #26293C; border-color: #26293C;">
          <div slot="header">
            <span class="dashboard-header">加班排行榜</span>
            <div style="margin-bottom: 3px;"><el-button style="float: right; padding: 3px 0;" type="text">查看更多</el-button></div>
          </div>
          <div>
            <el-row class="dashboard-list">
              <el-col :span="2">1</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
            <el-row class="dashboard-list">
              <el-col :span="2">2</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
            <el-row class="dashboard-list">
              <el-col :span="2">3</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
            <el-row class="dashboard-list">
              <el-col :span="2">4</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
            <el-row class="dashboard-list">
              <el-col :span="2">5</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
          </div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card style="background-color: #26293C; border-color: #26293C;">
          <div slot="header">
            <span class="dashboard-header">参与项目排行榜</span>
            <div style="margin-bottom: 3px;"><el-button style="float: right; padding: 3px 0;" type="text">查看更多</el-button></div>
          </div>
          <div>
            <el-row class="dashboard-list">
              <el-col :span="2">1</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
            <el-row class="dashboard-list">
              <el-col :span="2">2</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
            <el-row class="dashboard-list">
              <el-col :span="2">3</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
            <el-row class="dashboard-list">
              <el-col :span="2">4</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
            <el-row class="dashboard-list">
              <el-col :span="2">5</el-col>
              <el-col :span="18">张德锋</el-col>
              <el-col :span="4">98</el-col>
            </el-row>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
/* eslint-disable */

  export default {
  name: 'Dashboard',
  data () {
    this.chartSettings = {
      stack: {'dd': ['加班数', '项目数']},
      area: true
    }
    this.chartExtend = {
      legend: {
        borderColor: '#DB4DC5',
        textStyle: {
          color: '#939495'
        }
      },
      xAxis: {
        show: true,
        axisLine: {
          show: false
        },
        splitLine: {
          show: false
        },
        axisTick: {
          alignWithLabel: true
        }
      },
      yAxis: {
        splitLine: {
          show: false
        }
      },
      axisLabel: {
        show: true,
        color: '#939495'
      },
      series: {
        type: 'line',
        lineStyle: {
          color: '#4EB886'
        },
        markLine: {
          lineStyle: {
            color: 'red'
          }
        },
        areaStyle: {
          color: {
            type: 'linear',
            x: 0,
            y: 0,
            x2: 0,
            y2: 1,
            colorStops: [
              {offset: 0, color: '#2B3B46'},
              {offset: 0.5, color: 'rgba(43, 59, 70, 0.8)'},
              {offset: 1, color: 'rgba(43, 59, 70, 0.1'}
            ]
          }
        }
      }
    }
    return {
      chartData: {
        columns: ['月份', '加班数', '项目数'],
        rows: [
          {'月份': '一月', '加班数': 1393, '项目数': 109 },
          {'月份': '二月', '加班数': 3530, '项目数': 3230},
          {'月份': '三月', '加班数': 2923, '项目数': 2623},
          {'月份': '四月', '加班数': 1723, '项目数': 1423},
          {'月份': '五月', '加班数': 3792, '项目数': 3492},
          {'月份': '六月', '加班数': 4593, '项目数': 4293},
          {'月份': '七月', '加班数': 1393, '项目数': 1093},
          {'月份': '八月', '加班数': 3530, '项目数': 3230},
          {'月份': '九月', '加班数': 2923, '项目数': 2623},
          {'月份': '十月', '加班数': 1723, '项目数': 1423},
          {'月份': '十一月', '加班数': 3792, '项目数': 3492},
          {'月份': '十二月', '加班数': 4593, '项目数': 4293}
        ]
      }
    }
  }
}
</script>

<style scoped>

</style>
