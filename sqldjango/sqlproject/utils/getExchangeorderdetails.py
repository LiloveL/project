# 获得公司内部交换数据，根据时间查找货物从哪个仓库出来的
from sqlproject.models import Warehouses
from sqlproject.models import Exchangeorderdetails
import time
from sqlproject.utils import getTime

# 获取仓库的名称和id
def getWarehousesData():
    Warehouses_list = Warehouses.objects.all()
    return Warehouses_list


def getExchangeOrderDetailsData():
    # 得到仓库数据
    Warehouses_list = getWarehousesData()

    # 获取今年时间
    # timeStart = time.strftime('%Y', time.localtime())
    # timeStart = timeStart + "-01-01 00:00:00.000"
    timeStart = "2021-01-01 00:00:00.000"
    timeFinal = "2022-01-01 00:00:00.000"
    # 两个下划线
    value_list = []
    for Warehousesdata in Warehouses_list:
        data_list = Exchangeorderdetails.objects.filter(
            creationtime__range=[timeStart, timeFinal],
            towarehouseid=Warehousesdata.id)
        i = len(data_list)
        
        value = {"name":Warehousesdata.warehousename,"id":Warehousesdata.id,"value":i}
        value_list.append(value)
        # print(value_list)
        # print(Warehousesdata.warehousename,"id=",Warehousesdata.id,"i = ",i)
    # for i in value_list:
    #     print(i["name"])
    return value_list
