#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
import time
import datetime


#半径为5的球体积
r = 5
V = 4 * math.pi * r ** 3 / 3
print "此球体体积为: ","%.2f" % V

#求60本书的总价
book_num = 60
book_price = 24.95
totalprice = book_num*book_price*0.4 + 3 +0.75*(60-1)
print "60本书的总价是:",totalprice,"美元"

#
starttime = datetime.datetime(6,52)

timeArray = time.strptime(starttime, "%M:%S")
timeStamp = int(time.mktime(timeArray))
print "time=",timeArray

#