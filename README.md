### 重金悬赏，重现「木兰」编程语言编译器

本人特此声明：

**任何人，可以借助于任何现有开源技术，包括 Python 编译器本身。只要实现一个解释器或编译器，能够完成 ulang-0.2.2.exe 的功能，与它的编程语言语法和结果一致（1 月 26 日补：[项目目标](复现文档/README.md)），并且将代码公开开源，以证明实现的原创性，本人将以个人名义奖励*一万元*。奖金将随时间推移逐渐改变（当前收支[见此](https://github.com/MulanRevive/bounty/tree/master/%E6%94%B6%E6%94%AF%E8%B4%A6%E6%9C%AC)）。**

**当然可以组队攻关（只要有明确的贡献，将会提高奖金总额，以便分配），也可以基于之前的逆向工程。**

**当然也可以与我一同努力（演示版已经发布：[木兰编程语言，向您拜年！](https://zhuanlan.zhihu.com/p/103952156)），奖金同上处理。**


毕竟，现在有了设计者的思路（鸣谢《刘雷关于“木兰”编程语言的情况说明》）以及之后中科院的专家分析（见处理报告），以及对逆向工程的分析，技术路线已非常明晰（吧？）。

以至于，听说这几乎是计算机本科生就能完成的类似于专业课作业的难度（吗？）。

那么，请各位千万不要让我这个半路出家、业余摸索的外行人占了先！

来吧，让我看看后浪们的实力！

请广为告之！

----------------

附上：[知乎链接](https://zhuanlan.zhihu.com/p/104001337)

将会至少每周更新！

#### 1月25日

搜集相关[原始资料](原始资料)，为分析和加工打下基础，也为来者提供资料参考。在此基础上开始[复现文档](复现文档)。

号外！悬赏发布短短数小时之后，就有首位响应者[提交了实现代码](https://github.com/MulanRevive/bounty/issues/1)。让我们一同研究一下。

开始编写[「木兰」语言设计文档](复现文档/README.md)。

#### 1 月 26 日

祝贺！第一笔款项[已支付](https://github.com/MulanRevive/bounty/issues/1#issuecomment-578504572)！

正式提出[项目目标](复现文档/README.md)。

#### 1 月 27 日

感激！刚收到[第一笔赞助](https://github.com/MulanRevive/bounty/issues/3#issuecomment-578561078)！

#### 1 月 28 日

已向第一位参与者付酬金[累计 ￥954.88](https://github.com/MulanRevive/bounty/issues/3#issuecomment-579533880)。

创建细分悬赏任务：
- [建立简易账本系统](https://github.com/MulanRevive/bounty/issues/5)
- [对原始可执行文件的功能进行测试](https://github.com/MulanRevive/bounty/issues/4)

#### 1 月 29 日

学习rply用法并通过分析逆向工程获取while和loop的语法并通过[测试代码](https://github.com/MulanRevive/bounty/issues/4#issuecomment-580095743)。

用[脚本](测试代码/README.md)自动运行循环语法的测试，暂时依赖打印输出。exe启动时间较长，大约2秒一个测试，需改进。将在摸索各语法规则时添加对应测试代码。