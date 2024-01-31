from django.shortcuts import render
from .models import Checkrepodetails

# 引入方法
from django.http import HttpResponse
from django.http import JsonResponse
from .utils import getValue
from .utils import getExchangeorderdetails
from .utils import getPurchaseorders
from .utils import getSalesVolumetest
from .utils import getSalesQuantityData
from .utils import getTime
from .utils import getSalesByMouth
from .utils import getSalesByYear
from .utils import getSalesVolumeBySalespersonData
from .utils import getThreeSumSalesVolume


# Create your views here.
def project(request):
    name = Checkrepodetails.objects.filter(productcode="CG025")
    for i in name:
        print(i.productname)

    return HttpResponse("添加成功")


# 下面是进行数据库与前端连接实验
def test1(request):
    if request.method == "GET":
        product = getValue.getValue1()
        return JsonResponse({"value": product[0].productname})
    # for i in product:
    #     print(i.refprice)
    # return HttpResponse("添加成功")


# 按照时间取仓库转移货物的数据
def getExchangeOrderDetailsData(request):
    if request.method == "GET":
        value_list = getExchangeorderdetails.getExchangeOrderDetailsData()
        return JsonResponse({"value_list": value_list})

    else:
        return HttpResponse("运行失败")


# 获取每年和每月的订单
def getPurchaseordersData(request):
    if request.method == "GET":
        data_list = getPurchaseorders.getYeayData()

        getSalesQuantityData_list = getSalesQuantityData.getSalesQuantityData()
        # 根据月份去获得利润率
        profitByMouth = getSalesByMouth.getSalesByMouth()
        # 根据年份去获得利润率
        profitByYear = getSalesByYear.getSalesByYear()
        # print(getSalesVolumetest_list)
        return JsonResponse(
            {
                "valuelist": data_list,
                "getSalesQuantityData_list": getSalesQuantityData_list,
                "profitByMouth": profitByMouth,
                "profitByYear": profitByYear,
            }
        )
    else:
        return HttpResponse("运行失败")


# 获得年销售额、年利润和利润率
def getSalesVolumeData(request):
    if request.method == "GET":
        # 先获取今年日期，再获取数据
        starttime = getTime.getStartTime()
        endtime = getTime.getEndTime()
        print("starttime,endtime", starttime, endtime)
        ValueFromOrdercontractdetails_list = (
            getSalesVolumetest.getValueFromOrdercontractdetails(starttime, endtime)
        )
        # print(ValueFromOrdercontractdetails_list)
        return JsonResponse(
            {"ValueFromOrdercontractdetails_list": ValueFromOrdercontractdetails_list}
        )
    else:
        return HttpResponse("运行失败")


# 获取每个销售人员的销售单数
def getSalesQuantity(request):
    if request.method == "GET":
        getSalesQuantityData_list = getSalesQuantityData.getSalesQuantityData()
        
        return JsonResponse(
            {
                "getSalesQuantityData_list": getSalesQuantityData_list,
            }
        )
    else:
        return HttpResponse("运行失败")


# 获取每个销售人员的销售额和销售利润
def getSalesVolumeBySalesperson(request):
    if request.method == "GET":
        starttime = getTime.getStartTime()
        endtime = getTime.getEndTime()
        getSalesVolumeBySalespersonData_list = (
            getSalesVolumeBySalespersonData.getSalesVolumeBySalespersonData(
                starttime, endtime
            )
        )
        data_list = {
        "header": ["姓名", "销售额", "利润额"],
        "data": getSalesVolumeBySalespersonData_list["Data_list"],
        "rowNum": 6,
        "headerHeight": 35,
        "headerBGC": "#0f1325",
        "oddRowBGC": "#0f1325",
        "evenRowBGC": "#171c33",
        "index": "true",
        "columnWidth": [50],
        "align": ["center"],
    }
        return JsonResponse(
            {
                "getSalesVolumeBySalespersonData_list": data_list,
                "data":getSalesVolumeBySalespersonData_list["data_bylist"]
            }
        )
    else:
        return HttpResponse("运行失败")


# 该方法是获取近三年的销售额
def getSumSalesVolumeData(request):
    if request.method == "GET":
        getThreeSumSalesVolume_list = getThreeSumSalesVolume.getThreeSumSalesVolume()
        config = {"data": getThreeSumSalesVolume_list}
        return JsonResponse({"config": config})
    else:
        return HttpResponse("运行失败")
