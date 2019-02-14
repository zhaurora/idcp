# -*- coding: utf-8 -*-
'''
数学计算相关的方法
'''
import random
import string


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

def replaceone(s, d, lis):
    '''
    把lis中的s字符（数字）替换为d字符
    :param s: 原字符
    :param d: 目标字符
    :param lis: 原list
    :return:  list[]
    '''
    result = lis
    for i in range(lis.count(s)):
        idx = lis.index(s)
        result[idx] = d
    return result

def mergelist(list1, list2):
    '''
    利用set的特性合并list并去重
    :param list1: list[]
    :param list2: list[]
    :return: list[]，合并去重无序
    '''
    result = list1 + list2
    temp = set(result)
    return list(temp)

def CAPTCHA1(bitnum):
    '''
    生成bitnum位的验证码，09azAZ
    :param bitnum: 验证码位数
    :return: string
    '''
    temp = []
    #遍历ascii的字符
    for i in range(65,91):
        temp.append(chr(i))
    for j in range(97,123):
        temp.append(chr(j))
    for k in range(48,58):
        temp.append(chr(k))
    # 获取到的时list格式
    result = random.sample(temp, bitnum)
    # 转换为字符串格式
    result = ''.join(result)
    return result

def CAPTCHA2(bitnum):
    '''
    生成bitnum位的验证码，09azAZ
    :param bitnum: 验证码位数
    :return: string
    '''
    str1 = "0123456789"
    # 包含所有字母（大写和小写）的字符串
    str2 = string.ascii_letters
    str3 = str1+str2
    result = random.sample(str3, bitnum)
    result = ''.join(result)
    return result

def isNumber(s):
    '''
    判断字符串是否只有数字组成
    :param s: 输入的字符串
    :return: True / False
    '''
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def isEvenNum(s):
    '''
    判断输入是否为偶数
    :param s: 输入的字符
    :return: True / False
    '''
    try:
        num = int(s)
    except ValueError:
        return False

    if num % 2 == 0:
        return True

    return False

def isLeapYear1(year):
    '''
    判断闰年
    :param year: 输入的年份
    :return: True / False
    '''
    import calendar
    return calendar.isleap(year)

def isLeapYear2(year):
    '''
    判断闰年
    :param year: 输入的年份
    :return: True / False
    '''
    result = year%4 == 0 and year%100 != 0 or year%400 == 0
    return result

def Fibonacci(end):
    '''
    斐波那契数列：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
    :param end: 数列的总项数
    :return: list
    '''
    n1 = 0
    n2 = 1
    count = 2
    result =[]
    result.append(n1)
    result.append(n2)
    while count < end and end > 2:
        nth = n1 + n2
        result.append(nth)
        n1 = n2
        n2 = nth
        count += 1

    return result

def hcf(x, y):
    '''
    highest common factor 最大公约数
    :param x: 数字1
    :param y: 数字2
    :return: 最大公约数
    '''
    result = ''
    smaller = min(x, y)
    for i in range(1, smaller+1):
        if x%i==0 and y%i==0:
            result = i

    return result

def lcm(x, y):
    '''
    Lowest Common Multiple 最小公倍数
    :param x: 数字1
    :param y: 数字2
    :return: 最小公倍数
    '''
    result = ''
    greater = max(x, y)
    while True:
        if greater%x==0 and greater%y==0:
            result = greater
            break
        greater += 1

    return result

def getYestoday():
    '''
    获取昨天的日期
    :return:
    '''
    import datetime as dt
    today = dt.date.today()
    oneday = dt.timedelta(days=1)
    return today-oneday
