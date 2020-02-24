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

### 木兰

必须首先安装模块 rply 和 codegen。再运行：
```
> pyinstaller -F --hiddenimport rply --hiddenimport codegen ulang\__main__.py
89 INFO: PyInstaller: 3.6
90 INFO: Python: 3.7.6
90 INFO: Platform: Windows-7-6.1.7601-SP1
92 INFO: wrote D:\study\mulan\mulan_reverse\__main__.spec
95 INFO: UPX is not available.
98 INFO: Extending PYTHONPATH with paths
['D:\\study\\mulan\\mulan_reverse', 'D:\\study\\mulan\\mulan_reverse']
99 INFO: checking Analysis
114 INFO: Building because hiddenimports changed
114 INFO: Initializing module dependency graph...
117 INFO: Caching module graph hooks...
131 INFO: Analyzing base_library.zip ...
6242 INFO: Caching module dependency graph...
6423 INFO: running Analysis Analysis-00.toc
6426 INFO: Adding Microsoft.Windows.Common-Controls to dependent assemblies of final executable
  required by c:\users\win7_laptop\appdata\local\programs\python\python37\python.exe
6887 INFO: Analyzing D:\study\mulan\mulan_reverse\ulang\__main__.py
7175 INFO: Processing pre-safe import module hook   win32com
Traceback (most recent call last):
  File "<string>", line 2, in <module>
ModuleNotFoundError: No module named 'win32com'
7359 INFO: Processing pre-safe import module hook   win32com
Traceback (most recent call last):
  File "<string>", line 2, in <module>
ModuleNotFoundError: No module named 'win32com'
10136 INFO: Processing pre-find module path hook   distutils
10137 INFO: distutils: retargeting to non-venv dir 'c:\\users\\win7_laptop\\appdata\\local\\programs\\python\\python37\\lib'
11600 INFO: Processing pre-safe import module hook   win32com
Traceback (most recent call last):
  File "<string>", line 2, in <module>
ModuleNotFoundError: No module named 'win32com'
11827 INFO: Processing pre-find module path hook   site
11828 INFO: site: retargeting to fake-dir 'c:\\users\\win7_laptop\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\PyInstaller\\fake-modules'
17779 INFO: Processing module hooks...
17779 INFO: Loading module hook "hook-appdirs.py"...
17781 INFO: Import to be excluded not found: 'win32com'
17782 INFO: Loading module hook "hook-distutils.py"...
17783 INFO: Loading module hook "hook-encodings.py"...
17976 INFO: Loading module hook "hook-lib2to3.py"...
17986 INFO: Loading module hook "hook-pkg_resources.py"...
18492 INFO: Processing pre-safe import module hook   win32com
Traceback (most recent call last):
  File "<string>", line 2, in <module>
ModuleNotFoundError: No module named 'win32com'
18605 INFO: Processing pre-safe import module hook   win32com
Traceback (most recent call last):
  File "<string>", line 2, in <module>
ModuleNotFoundError: No module named 'win32com'
19096 INFO: Excluding import '__main__'
19099 INFO:   Removing import of __main__ from module pkg_resources
19100 INFO: Loading module hook "hook-pydoc.py"...
19101 INFO: Loading module hook "hook-sqlite3.py"...
19273 INFO: Loading module hook "hook-sysconfig.py"...
19275 INFO: Loading module hook "hook-xml.dom.domreg.py"...
19276 INFO: Loading module hook "hook-xml.etree.cElementTree.py"...
19276 INFO: Loading module hook "hook-xml.py"...
19417 INFO: Looking for ctypes DLLs
19537 INFO: Analyzing run-time hooks ...
19553 INFO: Including run-time hook 'pyi_rth_multiprocessing.py'
19560 INFO: Including run-time hook 'pyi_rth_pkgres.py'
19595 INFO: Looking for dynamic libraries
19922 INFO: Looking for eggs
19922 INFO: Using Python library c:\users\win7_laptop\appdata\local\programs\python\python37\python37.dll
19923 INFO: Found binding redirects:
[]
19938 INFO: Warnings written to D:\study\mulan\mulan_reverse\build\__main__\warn-__main__.txt
20193 INFO: Graph cross-reference written to D:\study\mulan\mulan_reverse\build\__main__\xref-__main__.html
20249 INFO: checking PYZ
20264 INFO: Building because toc changed
20265 INFO: Building PYZ (ZlibArchive) D:\study\mulan\mulan_reverse\build\__main__\PYZ-00.pyz
22902 INFO: Building PYZ (ZlibArchive) D:\study\mulan\mulan_reverse\build\__main__\PYZ-00.pyz completed successfully.
22978 INFO: checking PKG
22980 INFO: Building because toc changed
22980 INFO: Building PKG (CArchive) PKG-00.pkg
26351 INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
26356 INFO: Bootloader c:\users\win7_laptop\appdata\local\programs\python\python37\lib\site-packages\PyInstaller\bootloader\Windows-64bit\run.exe
26357 INFO: checking EXE
26361 INFO: Building because toc changed
26363 INFO: Building EXE from EXE-00.toc
26365 INFO: Appending archive to EXE D:\study\mulan\mulan_reverse\dist\__main__.exe
26380 INFO: Building EXE from EXE-00.toc completed successfully.
```

的确生成了 exe，但1）比原 exe 大一些，2）[积累的测试用例](https://github.com/MulanRevive/bounty/blob/master/%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/%E6%B5%8B%E8%AF%95.py)未能完全通过：
```
TypeError: required field "lineno" missing from stmt
通过： func_no_params.mulan
TypeError: object of type 'int' has no len()
通过： func_params.mulan
通过： break.mulan
通过： continue.mulan
通过： using_mulan_module.mulan
通过： using_python_module.mulan
通过： if.mulan
通过： if_else.mulan
通过： stmt_if_true.mulan
通过： stmt_if_false.mulan
通过： while.mulan
通过： loop.mulan
===================
失败： type.mulan 期望：b'Mulan' 实际：b''
失败： range.mulan 期望：b'012123-113' 实际：b'012123'
失败： for_colon.mulan 期望：b'6' 实际：b'0'
失败： for_in.mulan 期望：b'10' 实际：b'1'
失败： stmt_for_in.mulan 期望：b'3' 实际：b'0'
失败： stmt_for_colon.mulan 期望：b'5' 实际：b'0'
失败： if_elif.mulan 期望：b'1' 实际：b''
失败： if_elif_else.mulan 期望：b'3' 实际：b''
```

先[用的](https://github.com/MulanRevive/mulan/tree/31705846e538576c6fbe2754a919a07a86227600)并非原始的逆向工程，再试了[我修改之前的版本](https://github.com/MulanRevive/mulan/commit/fe5fefd38806e1955c236889f0e3eaf46df8c2f7)，仍然同样结果。

待深究。

不过至少构建过程初步走通。

也许要自己逆向一下。

相关内容在：[MulanRevive/bounty](https://github.com/MulanRevive/bounty/tree/master/%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/%E6%8E%A2%E7%B4%A2/%E6%9E%84%E5%BB%BA)
