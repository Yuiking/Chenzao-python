###第五章：条件和递归
=======
中心话题是能够根据程序的状态执行不同命令的if语句

**地板除和求余**
- 地板除 运算符(floor division operator) // 先做除法，然后将结果保留到整数。
- 求余运算符(modulus operator) % ，它会将两个数相除，返回余数。
> 可以查看一个数是否可以被另一个数整除——如果　x % y　的结果是 0，那么 x 能被 y　整除

> Python2,除法运算符 /　在被除数和除数都是整数的时候，会进行地板除，但是当被除数和除数中任意一个是浮点数的时候，则进行浮点数除法
    Python3中，无论任何类型都会保持小数部分

**布尔表达式**
- 布尔表达式（boolean expression）的结果要么为真要么为假
- True 和 False 是属于bool类型的特殊值；它们不是字符串。
- 关系运算符（relational operators）:==,!=,>,<,>=,<=
- 逻辑运算符（logical operators）：and 、or 和 not

**有条件的执行**
- 条件语句（Conditional statements）,最简单的形式是 if 语句, 能够检测条件，并相应地改变程序行为
> if 语句和函数定义有相同的结构：一个语句头跟着一个缩进的语句体。

- 由于条件要么为真要么为假，选择中只有一个会被执行。 这些选择被称作分支（branches）
- 链式条件（chained conditional): 多于两个的分支
- 嵌套条件（nested conditionals）: 一个条件可以嵌到另一个里面
> 1 避免使用嵌套条件
> 2 逻辑运算符通常是一个简化嵌套条件语句的方法

**递归**
- 一个调用它自己的函数是递归的（recursive）； 这个过程被称作递归（recursion）
- 无限递归（infinite recursion）， 通常这不是一个好主意,大多数编程环境里，一个具有无限递归的程序并非永远不会终止。 当达到最大递归深度时，Python会报告一个错误信息：
```
File "<stdin>", line 2, in recurse
  File "<stdin>", line 2, in recurse
  File "<stdin>", line 2, in recurse
                  .
                  .
                  .
  File "<stdin>", line 2, in recurse
RuntimeError: Maximum recursion depth exceeded
```

**键盘输入**
- python3 中,内建函数 input ，可以暂停程序运行，并等待用户输入

> python2 中,这个函数的名字叫raw_input




