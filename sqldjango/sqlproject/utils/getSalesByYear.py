from .getTime import *
from .getSalesVolumetest import *
def getSalesByYear():
    year = getYeay()
    starttime = str(year) + "-01-01 00:00:00.000"
    endtime = str(year+1) + "-01-01 00:00:00.000"
    print("year=",year)
    getSalesVolumetest_list = getValueFromOrdercontractdetails(starttime,endtime)
    sumSales = 0
    sumProfit = 0
    for i in getSalesVolumetest_list['lineData']:
        sumSales = sumSales + i
        
    for j in getSalesVolumetest_list['barData']:
        sumProfit = sumProfit + j
    print("sumSales=",sumSales)
    if sumSales == 0:
        profitMargin=0
    else:
        profitMargin = sumProfit/sumSales * 100
        profitMargin = round(profitMargin,1)
        print("profitMargin=",profitMargin)
    
    return profitMargin