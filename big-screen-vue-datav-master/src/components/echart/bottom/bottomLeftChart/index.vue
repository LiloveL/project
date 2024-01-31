<template>
  <div>
    <Chart :cdata="cdata" />
  </div>
</template>

<script>
import Chart from './chart.vue'
export default {
  data () {
    return {
      cdata: {
      }
    };
  },
  components: {
    Chart,
  },
  async mounted() {
      
      const res = await this.$http.get('getSalesVolumeData')
      this.cdata = res.data.ValueFromOrdercontractdetails_list
      console.log(this.cdata)
      this.setData();
      
      
  },
  // mounted () {
  //   this.setData();
  // },
  methods: {
    // 根据自己的业务情况修改
    setData () {
      for (let i = 0; i < this.cdata.barData.length -1; i++) {
        let rate = this.cdata.barData[i] / this.cdata.lineData[i];
        this.cdata.rateData.push(rate.toFixed(2));
      }
    },
  }
};
</script>

<style lang="scss" scoped>
</style>