# 获得年销售额、年利润和利润率
from sqlproject.models import Ordercontractdetails
from sqlproject.models import Ordercontracts
from sqlproject.models import Saleorders
from sqlproject.models import Brands
from django.db import connection



# 获得品牌名称
def getBrandName():
    # print(0)
    Brand_Name = Brands.objects.filter(isdeleted=0).values('brandname')
    brand_list = []
    for b in Brand_Name:
        brand_list.append(b['brandname'])
    brand_list.append("套装")
    return brand_list

# 根据公司名称获得ordercontractid
def getOrderContractId(brandname):
    # print(1)
    timeStart = "2021-01-01 00:00:00.000"
    timeFinal = "2022-01-01 00:00:00.000"
    # ,isdeleted=0
    OrderContractId_List = Ordercontractdetails.objects.filter(creationtime__range = [timeStart,timeFinal],brandname=brandname).values('ordercontractid')
    ordercontractid_list = []
    for o in OrderContractId_List:
        ordercontractid_list.append(o['ordercontractid'])
    return ordercontractid_list

# 利用ordercontractid查询ordercode
def getOrderCode(ordercontractid):
    # print(2)
    ordercode = Ordercontracts.objects.filter(
        id=ordercontractid).values('ordercode')
    return ordercode


# 利用ordercode查询销售额，利润
def getSalesVolume(ordercode):
    # print(3)
    # ,isdeleted=0
    SalesVolume_list = Saleorders.objects.filter(ordercode=ordercode,isdeleted=0)
    return SalesVolume_list


# 便利所有订单，获取数据
def getValueFromOrdercontractdetails():
    
    # 获得公司名称
    brand_list = getBrandName()
    print(brand_list)
    
    brandname = "Seba"
    # 根据公司名称获得订单id
    # for brandname in brand_list:
    list1 = getOrderContractId(brandname)
    OrderID_List = list(set(list1))
    # print()
    saleorderpricebydiscountnum = 0
    profitestimatenum = 0
    for id in OrderID_List:
        ordercode = getOrderCode(id)
        # print(ordercode[0]["ordercode"])
        salesvolume = getSalesVolume(ordercode[0]["ordercode"])
        #  and  salesvolume[0].shipstatus==2 and salesvolume[0].orderstatus != 0
        if len(salesvolume)>0 :
            saleorderpricebydiscountnum = saleorderpricebydiscountnum+salesvolume[0].saleorderpricebydiscount
            profitestimatenum = profitestimatenum + salesvolume[0].profitestimate
            
    print(saleorderpricebydiscountnum)
    print(profitestimatenum)
    print(profitestimatenum/saleorderpricebydiscountnum)
