<template>
  <div id="center">
    <div class="up">
      <div class="bg-color-black item">
        <p class="colorBlue"> 年采购次数总量</p>
        <div>
          {{ this.data_list[0] }}次
        </div>
      </div>
      <div class="bg-color-black item">
        <p style="color: rgb(210, 132, 58);text-align: center;">年采购次数</p>
      </div>
      <div class="bg-color-black item">
        <p style="color: rgb(104, 210, 58);text-align: center;"> 数据年份</p>
        <div style="text-align: center;">
          2022
          <!-- {{ this.data_list[4] }} -->
        </div>
      </div>
      <div class="bg-color-black item">
        <p class="colorBlue"> 未收货订单次数</p>
        <div >
          {{ this.data_list[1] }}次
        </div>
      </div>
      <div class="bg-color-black item">
        <p class="colorBlue"> 部分收货订单次数</p>
        <div>
          {{ this.data_list[2] }}次
        </div>
      </div>
      <div class="bg-color-black item">
        <p class="colorBlue"> 完成收获订单次数</p>
        <div>
          {{ this.data_list[3] }}次
        </div>
      </div>
      

    </div>


    <div class="down">
      <div class="ranking bg-color-black">
        <span>
          <icon name="chart-pie" class="text-icon"></icon>
        </span>
        <span>  销售排行榜</span>
        
        <dv-scroll-ranking-board class="dv-scr-rank-board mt-1" :config="ranking" />
      </div>
      <div class="percent">
        <div class="item bg-color-black">
          <span>本月销售利润率</span>
          <CenterChart :id="rate[0].id" :tips="rate[0].tips" :colorObj="rate[0].colorData" />
        </div>
        <div class="item bg-color-black">
          <span>本年销售利润率</span>
          <CenterChart :id="rate[1].id" :tips="rate[1].tips" :colorObj="rate[1].colorData" />
        </div>
        <div class="water">
          <dv-water-level-pond class="dv-wa-le-po" :config="water" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CenterChart from '@/components/echart/center/centerChartRate'

export default {
  data() {
    return {
      profitMargin : 0,
      num : 70,
      number: 90,
      data_list: [],
      ranking: {
      },
      water: {
        data: [20, 80],
        shape: 'roundRect',
        formatter: '欢迎使用',
        // 数字
        waveNum: 1
        // waveNum是波浪的数量
      },
      // 通过率和达标率的组件复用数据
      rate: [
        {
          id: 'centerRate1',
          tips: 0,
          colorData: {
            textStyle: '#3fc0fb',
            series: {
              color: ['#00bcd44a', 'transparent'],
              dataColor: {
                normal: '#03a9f4',
                shadowColor: '#97e2f5'
              }
            }
          }
        },
        {
          id: 'centerRate2',
          tips: 0,
          colorData: {
            textStyle: '#67e0e3',
            series: {
              color: ['#faf3a378', 'transparent'],
              dataColor: {
                normal: '#ff9800',
                shadowColor: '#fcebad'
              }
            }
          }
        }
      ]
    }
  },
  components: {
    CenterChart
  },
  async mounted() {
      const res = await this.$http.get('getPurchaseordersData')
      this.data_list = res.data.valuelist
      this.ranking = res.data.getSalesQuantityData_list
      // console.log(this.ranking)
      this.rate[0].tips = res.data.profitByMouth-0,
      this.rate[1].tips = res.data.profitByYear-0
      
      // console.log(this.profitMargin)
      
  },
}
</script>

<style lang="scss" scoped>
#center {
  display: flex;
  flex-direction: column;

  .up {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;

    .item {
      border-radius: 6px;
      padding-top: 8px;
      margin-top: 8px;
      width: 32%;
      height: 70px;

      .dv-dig-flop {
        width: 150px;
        height: 30px;
      }
    }
  }

  .down {
    padding: 6px 4px;
    padding-bottom: 0;
    width: 100%;
    display: flex;
    height: 255px;
    justify-content: space-between;

    .bg-color-black {
      border-radius: 5px;
    }

    .ranking {
      padding: 10px;
      width: 59%;

      .dv-scr-rank-board {
        height: 225px;
      }
    }

    .percent {
      width: 40%;
      display: flex;
      flex-wrap: wrap;

      .item {
        width: 50%;
        height: 120px;

        span {
          margin-top: 8px;
          font-size: 14px;
          display: flex;
          justify-content: center;
        }
      }

      .water {
        width: 100%;

        .dv-wa-le-po {
          height: 120px;
        }
      }
    }
  }
}
</style>
