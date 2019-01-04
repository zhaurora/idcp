'''
第5章 Python模块、包和程序
CHAPTER 5 Py Boxes: Modules, Packages, and Programs
Python模块、包和程序
'''

# 5.1 独立程序 Standalone Programs
print('===========5.1 独立程序 Standalone Programs===========')
'''
可以把编写完的py文件用命令提示字符执行
>>> python test1.py
'''

# 5.2 命令行参数 Command-Line Arguments
print('===========5.2 命令行参数 Command-Line Arguments===========')
'''
sys为命令行函数，import后即可在命令行直接输入参数。
    import sys
    print('Program arguments:',sys.argv[1])

test2.py tra la
>>> python test2.py
Program arguments: ['test2.py']
>>> python la
Program arguments: ['test2.py', 'tra', 'la', 'la']
'''

# 5.3 模块与Imoport语句 Modules and the import Statement
print('===========5.3 模块与Imoport语句 Modules and the import Statement===========')
'''
将代码拆成若干模块(Modules)后，即可使用import语句，並且可以用as重新取自己想要的名称
代码默认会搜索主程序相同路径的资料夹，若没有则搜索安装目录的\Lib资料夹

import 函数库( as 別名)
为导入全部的function

from 函数库 import function( as 別名)
为导入函数库中的某个特定function
'''

# 5.4 打包 Packages
print('===========5.4 打包 Packages===========')
'''
非常非常非常好用的功能!!!!
前述用法是把function拆开在同一层目录，但是如果函数库相当的多，在管理上会变得很复杂
所以可以将函数库利用文件夹来管理，简易示意图如下：
boxes
    |-weather.py
    |-sources
        |-__init__.py
        |-daily.py
        |-weekly.py

主程序为 weather.py
modules为daily.py 与 weekly.py
init.py文件则为一个空的文件，目的为使python将sources视为一个函数库用

主程式[weather.py]即可使用import导入sources文件夹中的函数
'''

# 5.5 标准函数库 The Python Standard Library
print('===========5.5 标准函数库 The Python Standard Library===========')
'''
介绍一些Python內建的标准函数库，
PYTHON把一些较不常用的function拆解为标准函数库，使得python更轻巧

详细介绍请看书本，这边不多说
'''

# 5.6 获取更多Python代码 More Batteries: Get Other Python Code
print('===========5.6 获取更多Python代码 More Batteries: Get Other Python Code===========')
'''
如果标准函数库中沒有想到的，可以上到其他网站中寻找，书中介绍了3个网站

PyPi（ http://pypi.python.org ）
github（ http://github.com/Python ）
readthedocs（ https://readthedocs.org/ )
Python Extension Packages，windows( http://www.lfd.uci.edu/~gohlke/pythonlibs/ )
'''

# 5.7 练习
print('===========5.7 练习===========')
#(1) 创建文件 zoo.py。在该文件中定义函数 hours()，输出字符串 'Open 9-5 daily'。然后 使用交互式解释器导入模块 zoo 并调用函数 hours()。

#(2) 在交互式解释器中，把模块 zoo 作为 menagerie 导入，然后调用函数 hours()。

#(3) 依旧在解释器中，直接从模块 zoo 导入函数 hours() 并调用。

#(4) 把函数 hours() 作为 info 导入，然后调用它。

#(5) 创建字典 plain，包含键值对 'a':1、'b':2 和 'c':3，然后输出它。

#(6)创建有序字典 fancy:键值对和练习 (5) 相同，然后输出它。输出顺序和 plain 相同吗?

#(7) 创建默认字典 dict_of_lists，传入参数 list。给 dict_of_lists['a'] 赋值 'something for a'，输出 dict_of_lists['a'] 的值。

from modulepackage import zoo
print("(1). " +zoo.hours())

from modulepackage import zoo as menagerie
print("(2). " +menagerie.hours())

from modulepackage.zoo import hours 
print("(3). " +hours())

from modulepackage.zoo import hours as info
print("(4). " +info())

plain = { 'a':'1', 'b':'2', 'c':'3', }
print("(5). " + str(plain))

import collections
# 通过OrderedDict类创建的字典是有序的
fancy = collections.OrderedDict()
fancy['a'] = '1'
fancy['b'] = '2'
fancy['c'] = '3'
print("(6). " )
print(fancy)

li = ['a1', 'b2', 'c3']
dict_of_lists = dict(li) 
print("(7). " )
print(dict_of_lists)
dict_of_lists['a'] = 'something for a'
print(dict_of_lists)
print(dict_of_lists['a'])


