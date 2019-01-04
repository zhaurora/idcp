# -*- coding: utf-8 -*-
'''
文件操作相关的方法
'''
import os

def listdirectory(path):
    '''
    列出指定目录下的所有文件和目录
    :param path: 指定的目录
    :return: list[]
    '''
    # 测试path路径是否存在
    if not os.path.exists(path):
        print(u'指定的目录%s不存在', path)
        return []
    result = [d for d in os.listdir(path)]
    return result

def absdir(path):
    '''
    输出某个路径下的所有文件和文件夹的路径
    :param path: 指定的目录
    :return: list[]
    '''
    result = []
    # 测试path路径是否存在
    if not os.path.exists(path):
        print(u'指定的目录%s不存在', path)
    else:
        for i in os.listdir(path):
            result.append(os.path.join(path,i))
    return result

def showdir(path):
    '''
    输出某个路径及其子目录下的所有文件路径，慎重处理
    :param path: 指定的目录
    :return: list[]
    '''
    result = []
    for i in os.listdir(path):
        temp = os.path.join(path, i)
        if os.path.isdir(temp):
            result.append(showdir(temp))
        else:
            result.append(temp)
    return result

def showfiles(path,sufx):
    result = []
    for i in os.listdir(path):
        temp = os.path.join(path, i)
        if os.path.isdir(temp):
            result.append(showfiles(temp, sufx))
        if temp.endswith(sufx):
            result.append(temp)
    return result