# -*- coding: utf-8 -*-
'''
Created on 2019年1月2日
'''
import os
import fileopts as fo
import mathopts as mo

'''
url:
https://mp.weixin.qq.com/s/YMAgZ7DE-bt9mPXjCwPgCQ
'''

if __name__ == '__main__':
    print(u'1、排序算法')
    lis = [56, 12, 1, 8, 354, 10, 100, 34, 56, 7, 23, 456, 234, -58]
    print(mo.sortport(lis))

    print(u'2、计算x的n次幂')
    print(mo.power(10,4))

    print(u'3、计算a*a + b*b + c*c + ... 平方和')
    print(mo.calc(1,2,3,4,5))

    print(u'4、计算num的阶乘')
    print(mo.fac(5))
    print(mo.factorial(5))
    print(mo.fact(5))

    print(u'5、列出目录下的所有文件和目录名')
    ld = fo.listdirectory('D:/')
    print(ld)

    print(u'6、把一个list中所有的字符串变成小写')
    sld = [s.lower() for s in ld]
    print(sld)

    print(u'7、输出某个路径下的所有文件和文件夹的路径')
    ad = fo.absdir(u'D:/')
    print(ad)

    print(u'8、输出某个路径及其子目录下的所有文件路径')
    sd = fo.showdir(u'C:\\Users\\banshu\\Downloads')
    print(sd)

    print(u'9、输出某个路径及其子目录下所有以.log为后缀的文件')
    sf = fo.showfiles(u'D:\\logs\\ncss2service', '.log')
    print(sf)

    print(u'10、把原字典的键值对颠倒并生产新的字典')
    dic1 = {"a":"A", "b":"B", "c":"C"}
    dic2 = {y:x for x,y in dic1.items()}
    print(dic1)
    print(dic2)
    dic3 = mo.reversal(dic1)
    print(dic3)

    print(u'11、打印九九乘法表')
    print(mo.multitable())

    print(u'12、替换列表中所有的3为3a')
    lis1 = ["harden", "lampard", 3, 34, 45, 56, 76, 87, 45, 3, 3, 3, 87666, 98, 76]
    print(lis1)
    lis2 = mo.replaceone(3, '3a', lis1)
    print(lis2)

    print(u'13、打印每个名字')
    Names = ["James", "Ming", "Xin"]
    for i in range(len(Names)):
        print("hello, %s"%Names[i])

    print(u'14、合并去重，集合set没有顺序')
    list1 = ['A',2,3,4,5,6,7,8,9]
    list2 = [7,8,9,10,'J','Q','K','tetrarch', 'monarch']
    print(list1)
    print(list2)
    print(mo.mergelist(list1, list2))

    print(u'15、随机生成验证码的两种方式 - 1')
    print(mo.CAPTCHA1(4))
    print(u'15、随机生成验证码的两种方式 - 2')
    print(mo.CAPTCHA2(6))

    print(u'16、计算平方根')
    num1 = [1,2,3,4,5,6,7,8,9,10]
    print(num1)
    num1_sqrt = [s ** 0.5 for s in num1]
    print(num1_sqrt)

    print(u'17、判断字符串是否只有数字组成')
    isnumber="1234567890.987654321"
    isnotnumber="!@#$%^&*()_+"
    print(mo.isNumber(isnumber))
    print(mo.isNumber(isnotnumber))

    print(u'18、判断奇偶数')
    isevennum='1233312'
    isnotevennum='1'
    print(mo.isEvenNum(isevennum))
    print(mo.isEvenNum(isnotevennum))

    print(u'19、判断闰年')
    year = 2000
    print(mo.isLeapYear1(year))
    print(mo.isLeapYear2(year))

    print(u'20、获取最大值')
    import random
    numlist1 = [random.randint(1,100) for i in range(0,10)]
    import numpy as np
    numlist2 = np.random.randint(100,size=10)
    print(numlist1)
    print(max(numlist1))
    print(numlist2)
    print(max(numlist2))

    print(u'21、斐波那契数列')
    print(mo.Fibonacci(2))
    print(mo.Fibonacci(8))
    print(mo.Fibonacci(16))

    print(u'22、十进制转二进制、八进制、十六进制')
    num22 = 21
    print("数字[%s]: 二进制 [%s], 八进制 [%s], 十六进制 [%s]" % (num22, bin(num22), oct(num22), hex(num22)) )

    print(u'23、最大公约数')
    numx = 18
    numy = 9
    print(mo.hcf(numx,numy))

    print(u'23、最小公倍数')
    num23x = 20
    num23y = 30
    print(mo.lcm(num23x, num23y))

    print(u'24、简单计算器')
    print('......')

    print(u'25、生成日历')
    import calendar as cld
    yy = random.randint(2018, 2020)
    mm = random.randint(1, 12)
    print(cld.month(yy, mm))

    print(u'26、文件IO')
    str261 = "26、文件IO\n"
    str262 = "写入文本的内容是什么？\n"
    with open("test.txt", "wt", encoding='utf-8') as outfile:
        outfile.write(str261)
        outfile.write(str262)

    with open("test.txt", "rt", encoding='utf-8') as infile:
        result = infile.read()
    print(result)

    print(u'27、字符串判断')
    str27 = "25a"
    print(str27.isalnum()) # 判断所有字符都是数字或字母
    print(str27.isalpha()) # 判断所有字符都是字母
    print(str27.isdigit()) # 判断所有字符都是数字
    print(str27.islower()) # 判断所有字符都是小写
    print(str27.isupper()) # 判断所有字符都是大写
    print(str27.istitle()) # 判断所有字符都是首字大写
    print(str27.isspace()) # 判断所有字符都是空白、\t、\n、\r、

    print(u'28、字符串大小写转换')
    str28 = "test a string"
    print(str28.upper()) # 转换成大写
    print(str28.lower()) # 转换成小写
    print(str28.capitalize()) # 转换成每句首字大写
    print(str28.title()) # 转换成每个词首字大写

    print(u'29、计算每个月天数')
    monthrange = cld.monthrange(yy, mm)
    print(yy,"年",mm,"月 共", max(monthrange), "天")

    print(u'30、获取昨天的日期')
    print(mo.getYestoday())

