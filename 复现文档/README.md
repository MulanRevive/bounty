从需求、设计、实现等各个层次对「木兰」编程语言进行分析。

之前用基于逆向工程的python演示版的交互环境进行了[初步的功能测试](https://github.com/program-in-chinese/team_website/blob/master/_posts/2020-01-23-%E6%9C%A8%E5%85%B0%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80%E5%9F%BA%E6%9C%AC%E5%8A%9F%E8%83%BD%E6%91%B8%E7%B4%A2(%E4%B8%80).markdown)后，发现几个问题：

- 有原版exe没有的bug： [1](https://github.com/MulanRevive/mulan/issues/2), [2](https://github.com/MulanRevive/mulan/issues/3)
- 代码难以自动测试
- 用python官方入门文档无法涵盖大部分用例

下面的语言设计文档，内容基于[原始资料](../原始资料/)、[逆向工程](https://github.com/MulanRevive/mulan)。格式参考[Lua](https://www.lua.org/manual/5.3/), [Python](https://docs.python.org/3/reference/)等。

***限于个人水平和对「木兰」功能理解的粗浅，必有错漏之处。欢迎指摘。***，

将使用原版exe进行测试验证，并且尽量形成测试代码集。

### 一、简介

【待确认】
「木兰」编程语言在语言规范上借鉴了Lua语言的特性并进行了扩展，增加数据表达方法等新的特性。先将木兰语言的源程序转换为Python的中间表示（AST），再在Python虚拟机上运行。[原设计者](../原始资料/设计文档/刘雷关于“木兰”编程语言的情况说明.png)

在 AST 上进行了对象命名标准化和 lambda 表达式扩展。[调查](../原始资料/设计文档/中科院20200123.pdf)

### 二、基本概念

#### 2.1 值和类型

「木兰」是动态类型语言。变量不指定类型，值自带类型。

值可以存于变量，作为参数传递给函数，也可以作为结果返回。

「木兰」中有几种基本类型：nil，布尔值，数，字符串，函数 （Lua 中有userdata, thread, and table，待确认）。

nil 只有“空”值，与其他所有值不同，用于表示有用值的反面。

布尔值有 true/false 两种值。nil 和 false 都使条件为假；任何其他值都为真。
```python
> nil
> nil or "a"
a
> nil and 10
> false or nil
> nil or false
false
> if (nil) {
>>   print(2)
>> } else {
>>   print(1)
>> }
1>
```

数包括整数和小数。

（参考 Python 文档）字符串为不可变的 Unicode 码序列，范围为 U+0000 - U+10FFFF，没有“字符”概念。`ord()`可以将字符转为编码值。

「木兰」可以调用 Python 的部分（？）内置函数，但有些改名(chr->char)：
```python
> ord('a')
97
> char(97)
a
```


【待续】