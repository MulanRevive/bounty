
## 更多木兰相关文章，欢迎关注[木兰编程语言](https://zhuanlan.zhihu.com/ulang)知乎专栏。

续[前文](https://zhuanlan.zhihu.com/p/115587722)，集成了[四则运算语法分析器](https://zhuanlan.zhihu.com/p/104345761)。运行效果如下：
```
$ python3 交互环境.py 
Welcome to ulang's REPL..
Type 'help' for more informations.
> 2*5/3
3.3333333333333335
> 1-4
-3
> (1+2)*3-4
5
> quit

```

除了之前的语法分析器，只加了此方法：
```python
class 木兰(cmd.Cmd):
...
    def default(self, line):
        print(分析器.parse(分词器.lex(line)).求值())
```

接下去还需验证将代码转换为 Python 语法树后再执行的关键技术。
