# 获取销售人员的销售额，销售利润
from django.db import connection  # 导入connection


def getSalesVolumeBySalespersonData(startTime, endTime):
    sql = (
        "SELECT rank() over(order by SUM(t2.RealPrice*t2.OrderNumber) desc) as Rank,t1.Surname + t1.Name as PersonName,count(distinct(sd.OrderCode)) as OrderNumber,SUM(t2.RealPrice*t2.OrderNumber) as SaleAmount,SUM(t2.RealPrice * t2.NumberShiped) as ShipedSaleAmount,SUM(t2.RealPrice*t2.OrderNumber- t2.CostEstimate) as ProfitEstimate,SUM(t2.RealPrice * t2.NumberShiped - case when t2.OrderNumber=0 then (t2.CostEstimate) else (t2.CostEstimate/t2.OrderNumber*t2.NumberShiped) end) as ShipedProfitEstimate FROM ABP.[Users] t1 join SaleOrders sd on sd.CreatorUserId = t1.Id join Bills bl on bl.Id = sd.BillId join SaleOrderDetails as t2 on t2.SaleOrderId = sd.Id join Customers as cm on cm.Id = sd.SaleOrderCustomerId Where t1.IsDeleted = 0 and t2.IsDeleted = 0 and t2.ProductId is not null and sd.IsDeleted =0 and (sd.OrderStatus=2 or sd.OrderStatus=1) and sd.MyCompanyId = 1 and sd.NewAddedDate >= '"
        + startTime
        + "' and sd.NewAddedDate< '"
        + endTime
        + "' and bl.IsDeleted =0 group by t1.UserName, t1.Name,t1.Surname order by SaleAmount desc, OrderNumber desc"
    )
    # print(sql)
    cursor = connection.cursor()  # 用建立好的connection对象创建cursor游标对象
    cursor.execute(sql)  # 执行自定义SQL语句
    dataInfo = cursor.fetchall()  # 取出执行返回的记录，返回的tuple类型数据
    # print(dataInfo)
    # 这个给饼图\
    data_bypeople = {}
    data_bylist = []
    
    Data_list = []
    for data in dataInfo:
        # 包装图表的数据
        name = data[1]
        ShipedSaleAmount = str(round(int(data[4]) / 10000, 1))
        # print(ShipedSaleAmount)
        ShipedProfitEstimate = str(round(int(data[6]) / 10000, 1))
        data_list = [name, ShipedSaleAmount, ShipedProfitEstimate]
        Data_list.append(data_list)
        # 包装饼图数据
        data_bypeople = {"value": ShipedSaleAmount, "name": name}
        data_bylist.append(data_bypeople)
    # 全部封装
    Data = {"Data_list": Data_list, "data_bylist": data_bylist}
    print(Data_list)
    cursor.close()  # 执行完，关闭
    connection.close()

    return Data
