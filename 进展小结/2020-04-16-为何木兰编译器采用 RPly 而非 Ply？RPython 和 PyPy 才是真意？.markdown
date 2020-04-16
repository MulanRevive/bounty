
“众所周知”地，木兰实现中使用 [RPly](https://pypi.org/project/rply/) 而非更为人知的 [Ply](http://www.dabeaz.com/ply/) 进行词法和语法分析器生成。

为什么要用这样一个更小众的工具？Ply 自 2006 年开始开发， RPly 自 2012 年，它的 pypi 主页上的介绍是：

> A pure Python parser generator, that also works with RPython. It is a more-or-less direct port of David Beazley’s awesome PLY, with a new public API, and RPython support.

API 的改进感觉不是决定性因素，因为木兰的语法设计规模并不算小，更多的开发精力应该是用于语法设计而非实现。粗浅地比较了 Ply 的例程，感觉两者的 API 虽然有差别，但实现效果仍是大同小异。

假如的确如此，那么是什么动力才使设计者选择了一个看起来风险更高的工具呢？

剩下的区别，就只有 RPly 对 RPython 的支持。

初步了解，RPython 和 PyPy 几乎是绑定的。知乎上相关技术介绍文章寥寥，实战更少。在 PyPy 的这篇近十年前的入门文档中，对它的作用可见一斑：

[Tutorial: Writing an Interpreter with PyPy, Part 1](https://morepypy.blogspot.com/2011/04/tutorial-writing-interpreter-with-pypy.html)

> Wouldn't it be nice if you could write your language in an existing high level language like, for example, Python? That sure would be ideal, you'd get all the advantages of a high level language like automatic memory management and rich data types at your disposal. Oh, but an interpreted language interpreting another language would be slow, right? That's twice as much interpreting going on.

> As you may have guessed, PyPy solves this problem. PyPy is a sophisticated toolchain for analyzing and translating your interpreter code to C code (or JVM or CLI). This process is called "translation", and it knows how to translate quite a lot of Python's syntax and standard libraries, but not everything. ***All you have to do is write your interpreter in RPython, a subset of the Python language carefully defined to allow this kind of analysis and translation, and PyPy will produce for you a very efficient interpreter***.

简单说，用 Python 写出的解释器执行想必很慢。现在可以用 RPython 语言（Python 语言的子集）写个解释器， PyPy 可以直接将 RPython 代码翻译为 C 代码，得到更高执行效率的解释器。

说回到 RPly，它提供了 RPython 的支持，那么用它实现的解释器应该可以用 PyPy 翻译后得到性能提升（待确认）。

这貌似是个更有价值的理由。
