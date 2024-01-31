# 这个方法是获取当前日期
import time
import datetime

# 注意一点，到真实的时间应该是当年，所以所有的数据的时间应该是往前算


# 获取年份
def getYeay():
    # 返回的时间是int类型的
    year = datetime.date.today()
    year = year.year
    year = 2021
    # print(year)
    return year


# 获取月份
def getMonth():
    month = datetime.date.today()
    month = month.month
    month = 11
    # print(month)
    return month


# 获取年前时间
def getStartTime():
    year = getYeay()
    starttime = str(year) + "-01-01 00:00:00.000"

    # print(starttime)
    return starttime


# 获取年后时间
def getEndTime():
    year1 = getYeay()
    year1 = year1 + 1
    endtime = str(year1) + "-01-01 00:00:00.000"

    # print(endtime)
    return endtime
