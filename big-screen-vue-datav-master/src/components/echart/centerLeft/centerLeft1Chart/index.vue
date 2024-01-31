<template>
  <div>
    <Chart :cdata="cdata" />
  </div>
</template>

<script>
import Chart from './chart.vue';
export default {
  data () {
    return {
      cdata: {
        // xData: ["FT-仓库1", "data2", "data3", "data4", "data5", "data6","data7"],
        seriesData: []
      }
    }
  },
  components: {
    Chart,
  },
  // 获取数据
  async mounted(){
    const res = await this.$http.get('getExchangeOrderDetailsData')
    this.cdata.seriesData = res.data.value_list

  },
  methods: {
  }
}
</script>

<style lang="scss" scoped>
</style>