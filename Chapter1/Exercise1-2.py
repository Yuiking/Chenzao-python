#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'Yui'

print "你好，世界"

#42分42秒总秒数
minites = 42
seconds = 42
totalsecond = minites*60+seconds
print "42分42秒总秒数为：",totalsecond,"秒"

#将公里转换为英里
distance_km = 10
distance_mail = distance_km/1.61
print "10公里转为英里为: ","%.2f" % distance_mail,"英里"#打印出来取两位小数

#求此次配速
pace = totalsecond/distance_mail#求得配速,单位是秒
min = int (pace/60)#分钟取整
sec = int(pace%60)#秒数取余的整数
print "配速(英里)为: ",min,"分",sec,"秒"

#求平均速度,英里/小时
speed = distance_mail*60*60/totalsecond
print "平均速度为: ","%.2f" % speed,"英里/小时"#打印出来取两位小数



