从需求、设计、实现等各个层次对「木兰」编程语言进行分析。

之前用基于逆向工程的python演示版的交互环境进行了[初步的功能测试](https://github.com/program-in-chinese/team_website/blob/master/_posts/2020-01-23-%E6%9C%A8%E5%85%B0%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80%E5%9F%BA%E6%9C%AC%E5%8A%9F%E8%83%BD%E6%91%B8%E7%B4%A2(%E4%B8%80).markdown)后，发现几个问题：

- 有原版exe没有的bug： [1](https://github.com/MulanRevive/mulan/issues/2), [2](https://github.com/MulanRevive/mulan/issues/3)
- 代码难以自动测试
- 用python官方入门文档无法涵盖大部分用例

下面打算根据[Lua](https://www.lua.org/manual/5.3/), [Python](https://docs.python.org/3/reference/)等的Language Specification文档进行测试验证。