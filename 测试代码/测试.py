import subprocess

期望值 = {
    "while.ul": b'10',
    "loop.ul": b'6'
}

for 文件 in 期望值:
    进程 = subprocess.Popen(["..\\原始资料\\可执行文件\\ulang-0.2.2.exe", 文件], stdout=subprocess.PIPE)
    输出 = 进程.communicate()[0]
    if 输出 == 期望值[文件]:
        print("通过： " + 文件)
    else:
        print("失败： " + 文件 + " 期望：" + str(期望值[文件]) + " 实际：" + str(输出))
