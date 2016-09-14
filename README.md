## Chenzao-python
#####趁早python小分队作业
-----------
###第一次作业
[前4章笔记](https://github.com/Yuiking/Chenzao-python/blob/master/homeworks/notes1-4.md)
=====
###第二次作业
[第五章笔记](https://github.com/Yuiking/Chenzao-python/blob/master/homeworks/notes5.md)
[第六章笔记](https://github.com/Yuiking/Chenzao-python/blob/master/homeworks/notes6.md)
[第七章笔记](https://github.com/Yuiking/Chenzao-python/blob/master/homeworks/notes7.md)
[第八章笔记](https://github.com/Yuiking/Chenzao-python/blob/master/homeworks/notes8.md)

####代码题
检查一个字母在一段字符中出现的次数。
答案如下:
```
def find(a):
    x = raw_input('please write down a string.')
    print(x)
    n = 0
    for letter in x:
        if letter[n] == a:
            n = n + 1
            return n

print find('a')
```
更简洁的答案:
```
def find(a):
    x = raw_input('please write down a string.')
    print(x)
    print x.count(a)

find('a')
```
####问题
Q:为啥要把爬到的数据存到数据库,而不是一个TXT文档中

A:爬虫爬取的海量数据只是第一部,用合适的方法处理数据并得出有效结论才是真正有价值的,大量数据存放在TXT中不仅读取速度不佳,处理上也有困难。
