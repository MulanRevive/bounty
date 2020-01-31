import subprocess

# 不确定为何输出是bytes：https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
期望值 = {
    "range.mulan": b'012123-113',
    "for_colon.mulan": b'6',
    "for_in.mulan": b'10',
    "stmt_for_in.mulan": b'3',
    "stmt_for_colon.mulan": b'5',
    "using_mulan_module.mulan": b'ho',
    "using_python_module.mulan": b'hi\r\n',
    "if.mulan": b'1',
    "if_else.mulan": b'2',
    "if_elif.mulan": b'1',
    "if_elif_else.mulan": b'3',
    "stmt_if_true.mulan": b'4',
    "stmt_if_false.mulan": b'',
    "while.mulan": b'10',
    "loop.mulan": b'6'
}

# 多进程参考：https://shuzhanfan.github.io/2017/12/parallel-processing-python-subprocess/
进程表 = {}

# 参考：https://stackoverflow.com/questions/748028/how-to-get-output-of-exe-in-python-script
for 文件 in 期望值:
    进程表[文件] = subprocess.Popen(["..\\原始资料\\可执行文件\\ulang-0.2.2.exe", 文件], stdout=subprocess.PIPE)

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

