# 从这里获得销售人员的销售单数
from django.db import connection  # 导入connection
from sqlproject.utils import getTime


def getSalesQuantityData():
    startTime = getTime.getStartTime()
    endTime = getTime.getEndTime()
    sql_str = (
        "SELECT U.Surname,U.Name, S.CreatorUserId,COUNT(S.CreatorUserId) FROM ABP.Users U LEFT JOIN (SELECT * FROM SaleOrders WHERE CreationTime BETWEEN '"
        + startTime
        + "' AND '"
        + endTime
        + "') S ON U.Id = S.CreatorUserId GROUP BY S.CreatorUserId,S.IsDeleted,U.Surname,U.Name  HAVING S.IsDeleted = 0 ORDER BY COUNT(S.CreatorUserId) DESC"
    )

    cursor = connection.cursor()  # 用建立好的connection对象创建cursor游标对象
    cursor.execute(sql_str)  # 执行自定义SQL语句
    dataInfo = cursor.fetchall()  # 取出执行返回的记录，返回的tuple类型数据
    # print(dataInfo)
    SalesQuantityData = {}
    data_list = []
    for data in dataInfo:
        SalesQuantityData = {"name": data[0] + data[1], "value": data[3]}
        data_list.append(SalesQuantityData)
    list = {"data": data_list, "carousel": "single", "unit": "件"}

    cursor.close()  # 执行完，关闭
    connection.close()
    return list
