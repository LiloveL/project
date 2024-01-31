# 此方法为采购数据，用于页面第一层中间位置的数据编写

import time
from sqlproject.models import Purchaseorders
from sqlproject.utils import getTime


# 获取年份
def getYeay():
    year = time.strftime("%Y", time.localtime())
    # print(year)
    return year


# 获取月份
def getMonth():
    month = time.strftime("%m", time.localtime())
    # print(month)
    return month


# 获取当年的数据
def getYeayData():
    # 起止时间
    yearStart = getTime.getStartTime()
    yearFinal = getTime.getEndTime()
    # yearStart = "2021-01-01 00:00:00.000"
    # yearFinal = "2022-01-01 00:00:00.000"
    # 获取年采购总数据
    data_AllList = Purchaseorders.objects.filter(
        orderdate__range=[yearStart, yearFinal], isdeleted=0
    )
    yearDataNumber = len(data_AllList)

    # 获取订单未发货的数据
    data_ReceiveStatusList = Purchaseorders.objects.filter(
        orderdate__range=[yearStart, yearFinal], isdeleted=0, receivestatus=0
    )
    yearDataReceuve0 = len(data_ReceiveStatusList)

    # 获取订单正在进行的数据
    data_ReceiveStatusList = Purchaseorders.objects.filter(
        orderdate__range=[yearStart, yearFinal], isdeleted=0, receivestatus=1
    )
    yearDataReceuve1 = len(data_ReceiveStatusList)

    # 获取订单接受的数据
    data_ReceiveStatusList = Purchaseorders.objects.filter(
        orderdate__range=[yearStart, yearFinal], isdeleted=0, receivestatus=2
    )
    yearDataReceuve2 = len(data_ReceiveStatusList)

    # print("yearDataNumber=", yearDataNumber, "yearDataReceuve0=",
    #       yearDataReceuve0, "yearDataReceuve1=", yearDataReceuve1,
    #       "yearDataReceuve2=", yearDataReceuve2)
    # for data in data_list:
    #     i = i+1
    year = getYeay()
    data_list = [
        yearDataNumber,
        yearDataReceuve0,
        yearDataReceuve1,
        yearDataReceuve2,
        year,
    ]
    return data_list
