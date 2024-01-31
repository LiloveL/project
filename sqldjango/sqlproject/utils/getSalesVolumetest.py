from django.db import connection  # 导入connection


# 获得年销售额、年利润和利润率
def getValueFromOrdercontractdetails(startTime, endTime):
    # 后来可以换时间
    print("startTime=",startTime,endTime)
    
    sql_str = (
        "SELECT rank() over(order by SUM(t2.RealPrice * t2.OrderNumber) desc) as Rank,t5.BrandName as BrandName,SUM(t2.RealPrice * t2.OrderNumber) as SaleAmount ,SUM(t2.RealPrice * t2.NumberShiped) as ShipedSaleAmount ,SUM(t2.RealPrice * t2.OrderNumber - t2.CostEstimate) as ProfitEstimate,SUM(t2.RealPrice * t2.NumberShiped - case when t2.OrderNumber=0 then (t2.CostEstimate) else (t2.CostEstimate/t2.OrderNumber*t2.NumberShiped) end) as ShipedProfitEstimate ,SUM(case when sd.OrderStatus=2 then t2.RealPrice * t2.OrderNumber - t2.RealCost else  0 end ) as ProfitAmount ,COUNT(distinct(sd.Id)) as OrderNumber,SUM(t2.OrderNumber) as ProductNumber,SUM(t2.NumberShiped) as ShipedProductNumber FROM SaleOrderDetails as t2 join SaleOrders as sd on sd.Id = t2.SaleOrderId join Bills as t1  on t1.Id = sd.BillId join Products as t3 on t3.Id = t2.ProductId join ProductTypes as t4 on t4.Id = t3.ProductType_Id join Brands as t5 on t5.Id = t4.TypeBrand_Id join Customers as cm on cm.Id = sd.SaleOrderCustomerId where t2.IsDeleted = 0 and sd.IsDeleted = 0 and t1.IsDeleted = 0 and t2.ProductId is not null and t2.FinishShipDate >= '"
        + startTime
        + "' and t2.FinishShipDate< '"
        + endTime
        + "' group by t5.Id,t5.BrandName "
    )

    cursor = connection.cursor()  # 用建立好的connection对象创建cursor游标对象
    cursor.execute(sql_str)  # 执行自定义SQL语句
    dataInfo = cursor.fetchall()  # 取出执行返回的记录，返回的tuple类型数据
    # print(dataInfo)
    brand_name = []
    saleorderpricebydiscount_num = []
    profitestimate_num = []
    ratedata = []
    for data in dataInfo:
        brand_name.append(data[1])
        saleorderpricebydiscount_num.append(round(data[2]/10000, 1))
        profitestimate_num.append(round(data[4]/10000, 1))
    data_value = {
        "category": brand_name,
        "lineData": saleorderpricebydiscount_num,
        "barData": profitestimate_num,
        "rateData": ratedata,
    }
    cursor.close()  # 执行完，关闭
    connection.close()
    return data_value
