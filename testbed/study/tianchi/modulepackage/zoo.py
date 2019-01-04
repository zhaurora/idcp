'''
5.7 练习
(1) 创建文件 zoo.py。在该文件中定义函数 hours()，输出字符串 'Open 9-5 daily'。然后 使用交互式解释器导入模块 zoo 并调用函数 hours()。

(2) 在交互式解释器中，把模块 zoo 作为 menagerie 导入，然后调用函数 hours()。

(3) 依旧在解释器中，直接从模块 zoo 导入函数 hours() 并调用。

(4) 把函数 hours() 作为 info 导入，然后调用它。

(5) 创建字典 plain，包含键值对 'a':1、'b':2 和 'c':3，然后输出它。

(6)创建有序字典 fancy:键值对和练习 (5) 相同，然后输出它。输出顺序和 plain 相同吗?

(7) 创建默认字典 dict_of_lists，传入参数 list。给 dict_of_lists['a'] 赋值 'something for a'，输出 dict_of_lists['a'] 的值。
'''

def hours():
    import datetime
    now_time = datetime.datetime.now()
    now_hour = 'It\'s '  +now_time.strftime('%H') + ' o\'clock now.'
    return now_hour


