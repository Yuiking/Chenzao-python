#!/usr/bin/python
# -*- coding: UTF-8 -*-


import time

#获得当前时间时间戳
now = int(time.time())

#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
clocktime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

days = now/(60*60*24)
hours = (now%(60*60*24))/24
minites = ((now%(60*60*24))%24)/60
seconds = (((now%(60*60*24))%24)%60)/60

print "现在时间为:", clocktime
print "纪元以来经过了",days,"天",hours,"小时",minites,"分钟",seconds,"秒"
