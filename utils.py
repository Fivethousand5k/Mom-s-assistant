import datetime
from xlrd import xldate_as_tuple
# 字符串时间转换函数
def Normaltime(datetime1):      # from string to datetime
    Normaltime = datetime.datetime.strptime(datetime1,'%Y-%m-%d %H:%M:%S')
    return Normaltime
def time_diff(stringtime1,stringtime2):
    """
    :param stringtime1:  str
    :param stringtime2:  str
    :return:  the difference between time1 and time2 in minutes
    """
    time1=Normaltime(stringtime1)
    time2=Normaltime(stringtime2)
    diff=(time2-time1) if time2>time1 else (time1-time2)
    return diff.seconds/60+diff.days*24*60

def time_parser(time):
    """
    :param time: 
    :return:  
    """
    if type(time) is float:
        time=datetime.datetime(*xldate_as_tuple(time,0))
        time=time.strftime('%Y-%m-%d %H:%M:%S')  # ('%Y/%m/%d %H:%M:%S')
    return time

