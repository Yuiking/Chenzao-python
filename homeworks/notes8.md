###第八章：字符串
======
字符串是一个 序列(sequence) ，这就意味着 它是其他值的一个有序的集合。
####字符串是一个序列
>b是 'banana' 的第0个字母(“zero-eth”)， a是第一个字母(“one-eth”)，n是第二个字 母(“two-eth”)。

- 可以使用一个包含变量名和运算符的表达式作为索引
- 索引值必须使用整数

####len
- len是一个内建函数，其返回字符串中的字符数量：
- 从0开始计数，六个字母的编号是0到5
- 可以使用负索引，即从字符串的结尾往后数。表达式 fruit[-1] 返回最后一个字母， fruit[-2] 返回倒数第二个字母

####使用for循环遍历
- 从字符串的头部开始，依次选择每个字符，对其做一些处理， 然后继续直到结束。 这种处理模式被称作 遍历(traversal) 
- 
####字符串切片
- 字符串的一个片段被称作 切片(slice)
- 空字符串（empty string）空字符串不包括字符而且长度为0，但除此之外， 它和其它任何字符串一样
####字符串是不可变的
- 字符串是 不可变的(immutable) ，这意味着你不能改变一个已存在的字符串。 你最多只能创建一个新的字符串
####搜索
- 遍历一个序列并在找到寻找的东西时返回——被称作 搜索(search) 
####字符串方法
- upper 方法接受一个字符串，并返回一个都是大写字母的新字符串。
####in运算符
- 单词 in 是一个布尔运算符，接受两个字符串。如果第一个作为子串出现在第二个中，则返回True

####字符串比较
- 关系运算符也适用于字符串。可以这样检查两个字符串是否相等
- Python处理大写和小写字母的方式和人不同。所有的大写字母出现在所有小写字母之前
> 解决此问题的常见方式是，在执行比较之前，将字符串转化为标准格式，例如都是小写字母。

 

