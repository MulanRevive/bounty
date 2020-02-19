### 技术验证

对单个文件：
```
pyinstaller -F print.py
```
生成`dist\print.exe`，可以拷贝到其他路径，正确运行。参考[文档](https://pyinstaller.readthedocs.io/en/stable/usage.html#what-to-generate)。

对于`printo`模块（可运行`python -m printo`），运行：
```
pyinstaller -F printo\__main__.py
```
生成`__main__.exe`文件，也可单独运行

