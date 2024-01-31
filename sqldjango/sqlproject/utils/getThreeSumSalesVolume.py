# 获取三年的销售额
from sqlproject.utils import getSumSalesVolume
from sqlproject.utils import getTime

def getThreeSumSalesVolume():
    # 获取时间
    sum_Sales = []
    starttime = getTime.getYeay()
    i = 3
    while i >0 :
        endtime = starttime+1
        sum_SalesList = getSumSalesVolume.getSumSalesVolume(starttime,endtime)
        sum_Sales.append(sum_SalesList)
        i = i -1 
        starttime = starttime - 1 
    print("sum_Sales========",sum_Sales)
    return sum_Sales
