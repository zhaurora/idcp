# weatherman.py
# 主程序
# P.S.这里抓不到，因为没有准备函数代码在文件夹中

import report  #把 report.py 放在相同的文件夹中，即可对其调用
description = report.get_description()  #使用report中的get_description函数

print("report.get_description() \t Today's weather:", description)

from report import get_description as get

print("get_description as get \t Today's weather:", get())
