### 环境搭建

安装 [Beancount](https://pypi.org/project/beancount/) v2.3.4。

### 查看收支状况

运行`$ bean-web 总账.beancount`后，访问 http://localhost:8080/

账本中，正数说明该账号增加了数额；负数是减少了数额。比如赞助人支出了 50，那么 ta 的账号（钱包）就减少了 50，因此为-50。

### 检查账本正确性

运行`$ bean-check 总账.beancount`，应该没有错误输出。如有"Invalid Token"，也许是因为 beancount [暂不支持中文账号名](https://github.com/beancount/beancount/issues/423) 。