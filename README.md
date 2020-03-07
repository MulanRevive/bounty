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

#### 1 月 30 日

继续分析语法，if/导入模块等等。开始编写[用户手册](https://github.com/MulanRevive/bounty/blob/master/%E5%A4%8D%E7%8E%B0%E6%96%87%E6%A1%A3/%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C/%E5%9F%BA%E6%9C%AC.md)。

#### 1 月 31 日

继续基于逆向工程中的 ply 代码，确认语法和功能。编写用户手册第二章——[控制走向](https://zhuanlan.zhihu.com/p/104548740)

#### 2 月 1 日

尝试了基于「木兰」定制[新语法](https://zhuanlan.zhihu.com/p/104723661)，比较简单。

#### 2 月 3 日

木兰编程语言[知乎专栏](https://zhuanlan.zhihu.com/ulang)创建，收录了之前的文章，欢迎指教。

#### 2 月 7 日

编写用户手册第三章——[函数和类型](https://zhuanlan.zhihu.com/p/105687154)，类型部分还有不少没有摸索出来。

#### 2 月 14 日

摸索导入[Python 模块](https://github.com/MulanRevive/bounty/issues/4#issuecomment-586520874)功能，有些疑问，需要对 Python 模块导入机制作深入研究。

#### 2 月 19 日

初步[构建可执行文件](https://zhuanlan.zhihu.com/p/107836848), 但测试未完全通过, 待深究.

#### 2 月 22 日

编写用户手册第四章——[模块](https://zhuanlan.zhihu.com/p/108632734)。

#### 3 月 5 日

[项目首月小结](https://zhuanlan.zhihu.com/p/111216467)。