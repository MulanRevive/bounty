import subprocess
from sys import platform

路径 = '用例/'

# 不确定为何输出是bytes：https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
期望值 = {
    "加小数.ul": b"5.0",
    "除小数.ul": b"2.0",
    "func_params_return.mulan": b'Mulan1',
    "lambda.mulan": b'[0, 1, 4, 9]',
    "func_no_params.mulan": b'123',
    "range.mulan": b'012123-113',
    "for_colon.mulan": b'6',
    "for_in.mulan": b'10',
    "stmt_for_in.mulan": b'3',
    "stmt_for_colon.mulan": b'5',
    "using_mulan_module.mulan": b'ho',
    # 参考: https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python
    "using_python_module.mulan": b'hi\r\n' if platform == "win32" else b'hi\n',
    "while.mulan": b'10',
    "loop.mulan": b'6',
    "排序/冒泡.ul": b'[1, 2, 4, 5, 8]',
    "排序/插入.ul": b'[1, 2, 4, 5, 8]',
    "排序/快速.ul": b'[1, 2, 4, 5, 8]',
    #"nested_func.mulan": b'5', # TODO: 因为 count 无返回, 因此输出 b'5nil'
}

# 多进程参考：https://shuzhanfan.github.io/2017/12/parallel-processing-python-subprocess/
进程表 = {}

# 参考：https://stackoverflow.com/questions/748028/how-to-get-output-of-exe-in-python-script
for 文件 in 期望值:
    print("开始测试：" + 文件)
    进程表[文件] = subprocess.Popen(["木兰", 路径 + 文件], stdout=subprocess.PIPE) #__main__

失败表 = {}

for 文件 in 进程表:
    输出 = 进程表[文件].communicate()[0]
    if 输出 == 期望值[文件]:
        print("通过： " + 文件)
    else:
        失败表[文件] = 输出

print("===================")
if len(失败表) > 0:
    for 文件 in 失败表:
        print("失败： " + 文件 + " 期望：" + str(期望值[文件]) + " 实际：" + str(失败表[文件]))
else:
    print("！全部通过！")

