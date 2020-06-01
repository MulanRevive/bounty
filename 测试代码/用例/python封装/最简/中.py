import os

from ulang.runtime.env import create_globals
from ulang.parser.core import Parser

def 调用(文件名):
    分析器 = Parser()

    with open(文件名, 'r', encoding='utf-8') as f:
        源码 = f.read()
    节点 = 分析器.parse(源码, 文件名)

    code = compile(节点, 文件名, 'exec')
        
    globals = create_globals(argv=[], fname=文件名)
    exec(code, globals)

当前路径 = os.getcwd()
调用(当前路径 + '/回应.ul')