# 该方法是获取近一年的销售额,返回数值是今年的销售额
from django.db import connection  # 导入connection


def getSumSalesVolume(sTime, eTime):
    startTime = str(sTime) + "-01-01 00:00:00.000"
    endTime = str(eTime) + "-01-01 00:00:00.000"
    sql_list = (
        "SELECT rank() over(order by SUM(t2.RealPrice * t2.OrderNumber) desc) as Rank,t5.BrandName as BrandName,SUM(t2.RealPrice * t2.OrderNumber) as SaleAmount ,SUM(t2.RealPrice * t2.NumberShiped) as ShipedSaleAmount  FROM SaleOrderDetails as t2 join SaleOrders as sd on sd.Id = t2.SaleOrderId join Bills as t1  on t1.Id = sd.BillId join Products as t3 on t3.Id = t2.ProductId join ProductTypes as t4 on t4.Id = t3.ProductType_Id join Brands as t5 on t5.Id = t4.TypeBrand_Id join Customers as cm on cm.Id = sd.SaleOrderCustomerId where t2.IsDeleted = 0 and sd.IsDeleted = 0 and t1.IsDeleted = 0 and t2.ProductId is not null and t2.FinishShipDate >= '"
        + startTime
        + "' and t2.FinishShipDate< '"
        + endTime
        + "' group by t5.Id,t5.BrandName "
    )
    cursor = connection.cursor()  # 用建立好的connection对象创建cursor游标对象
    cursor.execute(sql_list)  # 执行自定义SQL语句
    dataInfo = cursor.fetchall()  # 取出执行返回的记录，返回的tuple类型数据
    print(dataInfo)
    sum_Sales = 0
    for data in dataInfo:
        sum_Sales = data[3] + sum_Sales
    # print(sum_Sales)
    sum_Sales = round(sum_Sales / 10000, 1)
    sum_SalesList = {"name": sTime, "value": sum_Sales}
    print(sum_Sales)
    cursor.close()  # 执行完，关闭
    connection.close()
    return sum_SalesList
