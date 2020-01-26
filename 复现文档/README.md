从需求、设计、实现等各个层次对「木兰」编程语言进行分析。

之前用基于逆向工程的python演示版的交互环境进行了[初步的功能测试](https://github.com/program-in-chinese/team_website/blob/master/_posts/2020-01-23-%E6%9C%A8%E5%85%B0%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80%E5%9F%BA%E6%9C%AC%E5%8A%9F%E8%83%BD%E6%91%B8%E7%B4%A2(%E4%B8%80).markdown)后，发现几个问题：

- 有原版exe没有的bug： [1](https://github.com/MulanRevive/mulan/issues/2), [2](https://github.com/MulanRevive/mulan/issues/3)
- 代码难以自动测试
- 用python官方入门文档无法涵盖大部分用例

下面的语言设计文档，内容基于[原始资料](../原始资料/)。格式参考[Lua](https://www.lua.org/manual/5.3/), [Python](https://docs.python.org/3/reference/)等。

将使用原版exe进行测试验证，并且形成测试代码集。

### 一、简介

【待确认】
「木兰」编程语言在语言规范上借鉴了Lua语言的特性并进行了扩展，增加数据表达方法等新的特性。先将木兰语言的源程序转换为Python的中间表示（AST），再在Python虚拟机上运行。[原设计者](../原始资料/设计文档/刘雷关于“木兰”编程语言的情况说明.png)

在 AST 上进行了对象命名标准化和 lambda 表达式扩展。[调查](../原始资料/设计文档/中科院20200123.pdf)

### 二、基本概念


### 

【待续】