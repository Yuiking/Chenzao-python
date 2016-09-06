#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

#半径为5的球体积
r = 5
V = 4 * math.pi * r ** 3 / 3
print "此球体体积为: ","%.2f" % V

#求60本书的总价
book_num = 60
book_price = 24.95
total_price = book_num*book_price*0.4 + 3 +0.75*(60-1)
print "60本书的总价是:",total_price,"美元"

#习题2-2.3 求回家的时间
time1 = 8*60 +15 #放松跑每公里所需秒数
time2 = 7*60 + 12 #节奏跑每公里所需秒数
minites = (time1*2 + time2*3)/60 #总共所需分钟数
seconds = (time1*2 + time2*3)%60#求余下的秒数

#定义时间的类和打印时间的函数
class time:
     def print_tiem(time):
         print ('%.2d:%.2d:%.2d' % (time.hour,time.minite,time.second))

end = time()#定义end数组
end.hour = 6 + (52 + minites)/60 #求时数
end.minite = (52 + minites)%60#求分数
end.second = seconds #求秒数


print "回家吃饭的时间为：","end.print_tiem()"

