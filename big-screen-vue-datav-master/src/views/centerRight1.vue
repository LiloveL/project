<template>
  <div id="centerRight1">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span>
          <icon name="chart-line" class="text-icon"></icon>
        </span>
        <div class="d-flex">
          <span>任务完成排行榜</span>
        </div>
      </div>
      <div class="d-flex jc-center body-box">
        <dv-scroll-board class="dv-scr-board" :config="config" />-=
      </div>
    </div>
  </div>
</template>

<script>


export default {
  data() {
    return {
      config: {
      }
    }
  },
  async mounted() {
    const res = await this.$http.get('getSalesVolumeBySalesperson')
    this.config = res.data.getSalesVolumeBySalespersonData_list
  },
}
</script>

<style lang="scss" scoped>
$box-height: 410px;
$box-width: 300px;

#centerRight1 {
  padding: 16px;
  padding-top: 20px;
  height: $box-height;
  width: $box-width;
  border-radius: 5px;

  .bg-color-black {
    height: $box-height - 30px;
    border-radius: 10px;
  }

  .text {
    color: #c3cbde;
  }

  .body-box {
    border-radius: 10px;
    overflow: hidden;

    .dv-scr-board {
      width: 270px;
      height: 340px;
    }
  }
}</style>
