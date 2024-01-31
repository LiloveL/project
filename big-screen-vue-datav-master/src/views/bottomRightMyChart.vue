<template>
  <div id="pie-chart" style="width 500px; height: 500px;" ref="chart"></div>
</template>
<script>
import * as echarts from 'echarts';
export default {
  data() {
    return {
      a: [
      ]
    }
  },
  async mounted(){
    
    const res = await this.$http.get('getSalesVolumeBySalesperson')
    this.a = res.data.data
    console.log(this.a)
    this.initPieChart();
  },

  methods: {
    initPieChart() {
      const chart = echarts.init(document.getElementById('pie-chart')) // 获取DOM元素作为容器
      const options = {
        title: {
          top:'3%',
          text: '各销售的销售额',
          subtext: '单位/万元',
          left: 'center',
          textStyle: {
            
            fontSize: 20,
            color: '#ffffff'
          },
          subtextStyle: {
            fontSize: 15,
          }
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: '8%',
          top: '5%'
        },
        series: [
          {
            name: '销售额',
            type: 'pie',
            radius: '65%',
            data: this.a,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      }
      chart.setOption(options); // 设置配置项
    }
  },
  
}




</script>
 