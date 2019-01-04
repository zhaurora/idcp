# -*- coding: utf-8 -*-
'''
数学计算相关的方法
'''

def sortport(lis):
    '''
    冒泡排序
    :param lis: [56,12,1,8,354,10,100,34,56,7,23,456,234,-58]
    :return: 排序后的list
    '''
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
    return lis

def power(x, n):
    '''
    计算x的n次幂
    :param x: 底数
    :param n: 幂
    :return:
    '''
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# *是包含其他数字的，在这里面*numbers是一个tuple
def calc(*numbers):
    '''
    计算a*a + b*b + c*c + ... 平方和
    :param numbers: 要计算的目标数，如1,2,3,4,5
    :return: 和
    '''
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def fac(num):
    '''
    计算num的阶乘
    :param num: 目标数
    :return: 阶乘
    '''
    if num < 0:
        print(u'负数不能阶乘')
    elif num == 0:
        print(u'0的阶乘为1')
        return 1
    else:
        result = 1
        for i in range(1, num+1):
            result *= i
        print(u'%d的阶乘为%d' % (num, result))
        return result

def factorial(num):
    '''
    计算num的阶乘
    :param num: 目标数
    :return: 阶乘
    '''
    result = num
    for i in range(1, num):
        result *= i
    return result

def fact(n):
    '''
    计算n的阶乘
    :param n: 目标数
    :return: 阶乘
    '''
    if n==1:
        return 1
    return n*fact(n-1)

def reversal(dict):
    '''
    把原字典的键值对颠倒并生产新的字典
    :param dict: 原字典 dic{}
    :return: 颠倒后的字典 dic{}
    '''
    result = {y: x for x, y in dict.items()}
    return result

def multitable():
    '''
    打印九九乘法表，为什么会打印出None？
    通过指定end参数的值，可以取消在末尾输出回车符，实现不换行。
    :return:
    '''
    for i in range(1, 10):
        for j in range(1, i+1):
            print('%d x %d = %d \t'%(j, i, i*j), end='')
        print()
    return