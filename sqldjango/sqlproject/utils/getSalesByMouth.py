from .getTime import *
from .getSalesVolumetest import *
def getSalesByMouth():
    year = getYeay()
    month = getMonth()
    starttime = str(year) + "-" + str(month) + "-01 00:00:00.000"
    if month == 12:
        year = year + 1
        month = (month+1)%12
    else:
        month = month+1
    endtime = str(year) + "-" + str(month) + "-01 00:00:00.000"
    print("starttimedasdasd=",starttime,endtime)
    getSalesVolumetest_list = getValueFromOrdercontractdetails(starttime,endtime)
    
    sumSales = 0
    sumProfit = 0
    print("mouth=",len(getSalesVolumetest_list))
    print(getSalesVolumetest_list)
    for i in getSalesVolumetest_list['lineData']:
        sumSales = sumSales + i
        
    for j in getSalesVolumetest_list['barData']:
        sumProfit = sumProfit + j
    if sumSales == 0:
        profitMargin=0
    else:
        profitMargin = sumProfit/sumSales * 100
        profitMargin = round(profitMargin,1)
    
    return profitMargin