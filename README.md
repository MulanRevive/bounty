```
木兰诗 / 木兰辞

南北朝：佚名

唧唧复唧唧，木兰当户织。不闻机杼声，唯闻女叹息。

问女何所思，问女何所忆。女亦无所思，女亦无所忆。昨夜见军帖，可汗大点兵，军书十二卷，卷卷有爷名。阿爷无大儿，木兰无长兄，愿为市鞍马，从此替爷征。

东市买骏马，西市买鞍鞯，南市买辔头，北市买长鞭。旦辞爷娘去，暮宿黄河边，不闻爷娘唤女声，但闻黄河流水鸣溅溅。旦辞黄河去，暮至黑山头，不闻爷娘唤女声，但闻燕山胡骑鸣啾啾。

万里赴戎机，关山度若飞。朔气传金柝，寒光照铁衣。将军百战死，壮士十年归。

归来见天子，天子坐明堂。策勋十二转，赏赐百千强。可汗问所欲，木兰不用尚书郎，愿驰千里足，送儿还故乡。

爷娘闻女来，出郭相扶将；阿姊闻妹来，当户理红妆；小弟闻姊来，磨刀霍霍向猪羊。开我东阁门，坐我西阁床。脱我战时袍，著我旧时裳。当窗理云鬓，对镜帖花黄。出门看火伴，火伴皆惊忙：同行十二年，不知木兰是女郎。

雄兔脚扑朔，雌兔眼迷离；双兔傍地走，安能辨我是雄雌？
```

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

### 2020 年

#### 1 月

- 25日，搜集相关[原始资料](原始资料)，为分析和加工打下基础，也为来者提供资料参考。在此基础上开始[复现文档](复现文档)。

  号外！悬赏发布短短数小时之后，就有首位响应者[提交了实现代码](https://github.com/MulanRevive/bounty/issues/1)。让我们一同研究一下。

  开始编写[「木兰」语言设计文档](复现文档/README.md)。
- 26 日，祝贺！第一笔款项[已支付](https://github.com/MulanRevive/bounty/issues/1#issuecomment-578504572)！

  正式提出[项目目标](复现文档/README.md)。
- 27 日，感激！刚收到[第一笔赞助](https://github.com/MulanRevive/bounty/issues/3#issuecomment-578561078)！
- 28 日，已向第一位参与者付酬金[累计 ￥954.88](https://github.com/MulanRevive/bounty/issues/3#issuecomment-579533880)。

  创建细分悬赏任务：
  - [建立简易账本系统](https://github.com/MulanRevive/bounty/issues/5)
  - [对原始可执行文件的功能进行测试](https://github.com/MulanRevive/bounty/issues/4)
- 29 日，学习rply用法并通过分析逆向工程获取while和loop的语法并通过[测试代码](https://github.com/MulanRevive/bounty/issues/4#issuecomment-580095743)。

  用[脚本](测试代码/README.md)自动运行循环语法的测试，暂时依赖打印输出。exe启动时间较长，大约2秒一个测试，需改进。将在摸索各语法规则时添加对应测试代码。
- 30 日，继续分析语法，if/导入模块等等。开始编写[用户手册](https://github.com/MulanRevive/bounty/blob/master/%E5%A4%8D%E7%8E%B0%E6%96%87%E6%A1%A3/%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C/%E5%9F%BA%E6%9C%AC.md)。
- 31 日，继续基于逆向工程中的 ply 代码，确认语法和功能。编写用户手册第二章——[控制走向](https://zhuanlan.zhihu.com/p/104548740)

#### 2 月

- 1 日，尝试了基于「木兰」定制[新语法](https://zhuanlan.zhihu.com/p/104723661)，比较简单。
- 3 日，木兰编程语言[知乎专栏](https://zhuanlan.zhihu.com/ulang)创建，收录了之前的文章，欢迎指教。
- 7 日，编写用户手册第三章——[函数和类型](https://zhuanlan.zhihu.com/p/105687154)，类型部分还有不少没有摸索出来。
- 14 日, 摸索导入[Python 模块](https://github.com/MulanRevive/bounty/issues/4#issuecomment-586520874)功能，有些疑问，需要对 Python 模块导入机制作深入研究。
- 19 日，初步[构建可执行文件](https://zhuanlan.zhihu.com/p/107836848), 但测试未完全通过, 待深究.
- 22 日，编写用户手册第四章——[模块](https://zhuanlan.zhihu.com/p/108632734)。

#### 3 月

- 5 日，[项目首月小结](https://zhuanlan.zhihu.com/p/111216467)
- 8 日，编写用户手册第五章——[数据结构](https://zhuanlan.zhihu.com/p/111947851)
- 18 日，通过[修改逆向工程中的bug](https://zhuanlan.zhihu.com/p/114194675)，生成了exe能够通过所有当前测试用例。
- 22 日，木兰编译器技术验证——[用 cmd 模块实现最简单交互控制台](https://zhuanlan.zhihu.com/p/115587722)
- 24 日，木兰编译器技术验证——[交互控制台集成 rply 语法分析器](https://zhuanlan.zhihu.com/p/116663288)
- 25 日，木兰编译器技术验证——[通过 AST 转换和 eval 实现语法定制](https://zhuanlan.zhihu.com/p/117481247)

#### 4 月

- 10 日 [木兰逆向工程中的 bug（三）——交互控制台，以及下一步](https://zhuanlan.zhihu.com/p/128981286)
- 12 日，木兰编译器技术验证——[源文件解析与 exec](https://zhuanlan.zhihu.com/p/129740212)
- 15 日，暂时不实现 REPL 部分，开始搭建原型[加法部分](https://zhuanlan.zhihu.com/p/130906719)
- 16 日，延伸调研 [RPly 和 PyPy](https://zhuanlan.zhihu.com/p/131780649)，作了简单[性能对比试验](https://zhuanlan.zhihu.com/p/132503029)
- 19 日，原型搭建——[调用 print](https://zhuanlan.zhihu.com/p/133449850)
- 21 日，原型搭建——[整数的減、乘、除](https://zhuanlan.zhihu.com/p/134029658)，其中除较特别
- 24 日，原型搭建——[行号，多行支持](https://zhuanlan.zhihu.com/p/136142507)

#### 5 月

- 1 日，为方便调试[改进语法树格式化输出](https://zhuanlan.zhihu.com/p/137651939)
- 2 日，原型搭建——[行列号，语法树比照](https://zhuanlan.zhihu.com/p/137785657)
- 四日，原型搭建——[赋值语句](https://zhuanlan.zhihu.com/p/138253566)
- 11 日，原型搭建——[“块”结构（{}）支持](https://zhuanlan.zhihu.com/p/140430769)
- 16 日，原型搭建——[条件语句（if...elif...else)](https://zhuanlan.zhihu.com/p/141426111)
- 19 日，原型搭建——[大小比较、while循环，不允许无效果表达式](https://zhuanlan.zhihu.com/p/141426111)
- 23 日 [木兰编程语言体验版更新，附带 VS Code 支持插件](https://zhuanlan.zhihu.com/p/143038381)，通过更多测试。短期内，将基于体验版编写一些例程，过程中改进周边设施，包括对反馈信息进行中文化。此过程中原型项目将以技术验证（包括体验版中的 bug 重现和修复）为主要目的。
- 30 日 [木兰编程语言体验版更新：中文交互环境、调用 Python 库](https://zhuanlan.zhihu.com/p/144809020). 原型项目推进到引用本地 python.

#### 6 月

- 3 日, 原型项目: 开始类型定义部分.
- 13 日，原型项目搬家到[OSChina](https://www.oschina.net/p/mulan-rework)，并发布[阶段小结](https://zhuanlan.zhihu.com/p/148065426)。下面除了继续完善语言功能，打算向编辑器方向摸索。
- 19 日，原型进展：[支持列表操作，演示编辑器高亮](https://www.oschina.net/news/116577/grasspy-updated)
- 26 日，[儿歌查询实例，引用模块、字符串列表操作](https://www.oschina.net/news/116734/grasspy-updated)

#### 7 月

- 6 日，[范围语法“下限..上限 by 间隔”，重构](https://www.oschina.net/news/116967/grasspy-updated)
- 10 日，[无参数函数、字典基本功能，语法设计的取舍有感](https://www.oschina.net/news/117081/grasspy-updated)
- 16 日，[匿名函数，lambda表达式初步](https://zhuanlan.zhihu.com/p/161263901)
- 24 日，[完善函数功能，常用字拆分数据处理实例](https://zhuanlan.zhihu.com/p/163588221)

#### 8 月
- 7 日，[通过玩三岁游戏完善语言功能](https://zhuanlan.zhihu.com/p/174263153)
- 8 日，小结了[木兰编程语言待重现语法和功能](https://zhuanlan.zhihu.com/p/176769490)，在[此 issue](https://gitee.com/MulanRevive/mulan-rework/issues/I1SEU5) 持续更新。
- 18 日，[引用本地木兰模块；模拟凑十法加法](https://zhuanlan.zhihu.com/p/190043049)
- 28 日，[支持乘法省略乘号（2长+3宽）等等](https://zhuanlan.zhihu.com/p/205190684)

#### 9 月
- 3 日，[优先级实现细节阶段小结与问题](https://zhuanlan.zhihu.com/p/215864788)
- 7 日，[阶段小结，重申悬赏](https://zhuanlan.zhihu.com/p/224600854)
- 9 日，[整理测试用例，回归测试](https://zhuanlan.zhihu.com/p/230155471)
- 11 日，[木兰 vs. Python 之语法对用户体验的影响（一）](https://zhuanlan.zhihu.com/p/237379701)
- 14 日，[交互环境复现，新添新手入门](https://zhuanlan.zhihu.com/p/245390062)
- 21 日，[150 行木兰代码为木兰自身实现高亮效果](https://zhuanlan.zhihu.com/p/257726779)
- 25 日，[$ 的妙用，更多编辑器高亮](https://zhuanlan.zhihu.com/p/259467288)

#### 10 月
- 1 日，[更多 $ 的妙用，self 的拓展语义](https://zhuanlan.zhihu.com/p/261048633)
- 6 日，[木兰代码格式化之自动调整缩进的 150 倍性能优化](https://zhuanlan.zhihu.com/p/262210417)
- 8 日，[与 Python 生态的兼容问题；字符串插值](https://zhuanlan.zhihu.com/p/262835743)
- 11 日，[重温初见木兰的那个战场——二零二零年一月「木兰」编程语言风暴亲历记](https://zhuanlan.zhihu.com/p/265091649)
- 14 日，[PyPI 发布 ulang 0.0.14.1](https://zhuanlan.zhihu.com/p/265695809)
- 17 日，[0.0.14.3：井字棋演示，tuple、枚举等](https://zhuanlan.zhihu.com/p/266428706)
- 21 日，[0.0.14.4：中文报错信息规整，枚举引用新发现](https://zhuanlan.zhihu.com/p/267686876)
- 25 日，[0.0.14.6：网络服务演示；with...as 的替代语法](https://zhuanlan.zhihu.com/p/268660973)

#### 11 月
- 1 日，[0.0.14.7：功能覆盖初版用户手册；Gitee Go 流水线尝鲜](https://zhuanlan.zhihu.com/p/271636727)
- 6 日，[0.0.14.8：websocket 聊天演示；部分比较 Python 语法](https://zhuanlan.zhihu.com/p/277557485)
- 18 日，[0.0.15.0：基于网络的运行环境；词法错误处理](https://zhuanlan.zhihu.com/p/301086221)
- 25 日，[为木兰开发环境雏形添加输入补全，功能测试大提速](https://zhuanlan.zhihu.com/p/313557385)
- 30 日，为简化正则表达式读写，[构思相关 API](https://zhuanlan.zhihu.com/p/323940002)

#### 12 月
- 4 日，[用木兰编程语言编写文字冒险游戏（前八章）](https://zhuanlan.zhihu.com/p/331747102)
- 6 日，[小结正则表达式 API，寻觅合作者](https://zhuanlan.zhihu.com/p/333137600)
- 12 日，[文字冒险游戏九到十一章](https://zhuanlan.zhihu.com/p/336568481)
- 14 日，[0.0.15.1：继续改写 Python 冒险游戏；引用包路径规则小结](https://zhuanlan.zhihu.com/p/337101227)
- 23 日，[木兰语言的引用相关功能与问题新发现](https://zhuanlan.zhihu.com/p/339033162)
- 28 日，[对 PyPI 发布版和 PyInstaller 生成版在 Python 路径方面的差异分析](https://zhuanlan.zhihu.com/p/340410951)

### 2021 年
#### 1 月

- 4 日，继续[改写 Python 文字冒险游戏（十三、四章），又一个特性发现](https://zhuanlan.zhihu.com/p/342058152)
- 17 日，[重现木兰编程语言的基本 try……catch 语法](https://zhuanlan.zhihu.com/p/345139002)
- 21 日，[木兰编程语言一岁了！](https://zhuanlan.zhihu.com/p/345851006)

#### 2 月
- 9 日，[木兰语言多次引用模块的行为小结](https://zhuanlan.zhihu.com/p/350337192)
- 19 日，[木兰编程语言报错信息分类与可用性简析](https://zhuanlan.zhihu.com/p/351483957)
- 24 日，[从木兰的 1[0] = [0] 有感编程语言语法设计的舍与得](https://zhuanlan.zhihu.com/p/352660693)

#### 四月
- 2 日，[木兰语言 0.0.17：着手由 Python 语法树生成木兰源码](https://zhuanlan.zhihu.com/p/362071943)
- 20 日，[0.0.17.1：源码生成支持更多函数、类相关语法](https://zhuanlan.zhihu.com/p/366408277)
- 30 日，[0.0.17.2：实现简易网页浏览器，又一次碰到语法歧义](https://zhuanlan.zhihu.com/p/369268306)

#### 五月

- 5 日，[木兰 0.0.17.3 支持不需 __init__的 super 调用](https://zhuanlan.zhihu.com/p/370117192)
- 13 日，[木兰语言 0.0.17.4 发现依赖库风险、不支持 in；发布 Gitee Reward 首批悬赏任务](https://zhuanlan.zhihu.com/p/372021884)
- 17 日，[木兰语言 0.0.18 补完所有内置函数，悬赏任务合作顺利](https://zhuanlan.zhihu.com/p/373278659)
- 27 日，[木兰语言 0.0.19 补完二元运算；重现 yield 语法；赋值时可指定变量类型](https://zhuanlan.zhihu.com/p/376747637)

#### 七月

- 10 日，[木兰语言 0.0.21 查缺补漏；rply 改进、接口中文化](https://zhuanlan.zhihu.com/p/388440048)
- 18 日，[木兰语言 0.0.22 继续 py 转木兰；探路 py 3.8](https://zhuanlan.zhihu.com/p/391093875)

#### 尝试借助 rply 实现无空格语法

- [用 rply-ulang 实现“求8的oct值”语法](https://zhuanlan.zhihu.com/p/378353764)
- 九月 [解析中文编程语法诸如“删除钟表表”的一次粗糙尝试（上）](https://zhuanlan.zhihu.com/p/411793590)
- [解析中文编程语法诸如“删除钟表表”的一次粗糙尝试（下）](https://zhuanlan.zhihu.com/p/411991539)
- [用rply按语法分词实现中文无空格语法设计（一）](https://zhuanlan.zhihu.com/p/412465957)
- [用 RPly 按语法分词实现中文编程无空格语法设计（二）——生成对应SQL演示](https://zhuanlan.zhihu.com/p/413837369)
- [从“零”开始设计中文编程语言——SQL领域演示](https://zhuanlan.zhihu.com/p/415732605)

### 2022 年
#### 1 月

- 17日 [木兰编程语言两岁了](https://zhuanlan.zhihu.com/p/458489345)

#### 12 月

- 18 日, [木兰语言 0.1.0 展示今年悬赏任务成果](https://zhuanlan.zhihu.com/p/592786914)

### 2023 年

#### 1 月

- 5 日, [木兰语言 0.1.3 复现大多数命令行选项](https://zhuanlan.zhihu.com/p/596938996)
- 25 日，[木兰编程语言工具设计与实现中的巧思](https://zhuanlan.zhihu.com/p/601321957)

#### 2 月

- 11 日，北京时间二月十一日一点 [知乎 live 讲座《木兰编程语言重现项目三年小结》](https://www.zhihu.com/lives/1596877608825921536)。自行整理后发布到 [哔哩哔哩](https://space.bilibili.com/35262584/channel/seriesdetail?sid=3044931)、[知乎视频](https://www.zhihu.com/zvideo/1608797608780156930)。

### 2024 年

- 3 月，[木兰编程语言重现发布 0.1.6——支持到py3.11与其他](https://zhuanlan.zhihu.com/p/689843237)
- 6 月，长期悬赏 [查漏任务](https://gitee.com/MulanRevive/mulan-rework/issues/I90KWQ) 首个发现：[不同系统下测试发布版(v0.1.6)、开发版(v0.1.7)及原始木兰的最大递归深度不同](https://gitee.com/MulanRevive/mulan-rework/pulls/70)
- 8 月
  - [从例程看仓颉与木兰编程语言设计（一）](https://zhuanlan.zhihu.com/p/714163596)
  - pypi 发布 0.1.6.4，支持 py 到 3.12，修正报错信息等
