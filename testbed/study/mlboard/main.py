# -*- coding: utf-8 -*-
'''
Created on 2019年1月2日
'''
import os

'''
https://mp.weixin.qq.com/s/YMAgZ7DE-bt9mPXjCwPgCQ
'''

if __name__ == '__main__':
    print(u'1、排序算法')
    from mathopts import sortport
    lis = [56, 12, 1, 8, 354, 10, 100, 34, 56, 7, 23, 456, 234, -58]
    print(sortport(lis))

    print(u'2、计算x的n次幂')
    from mathopts import power
    print(power(10,4))

    print(u'3、计算a*a + b*b + c*c + ... 平方和')
    from mathopts import calc
    print(calc(1,2,3,4,5))

    print(u'4、计算num的阶乘')
    from mathopts import fac
    print(fac(5))
    from mathopts import factorial
    print(factorial(5))
    from mathopts import fact
    print(fact(5))

    print(u'5、列出目录下的所有文件和目录名')
    from fileopts import listdirectory
    ld = listdirectory('D:/')
    print(ld)

    print(u'6、把一个list中所有的字符串变成小写')
    sld = [s.lower() for s in ld]
    print(sld)

    print(u'7、输出某个路径下的所有文件和文件夹的路径')
    from fileopts import absdir
    ad = absdir(u'D:/')
    print(ad)

    print(u'8、输出某个路径及其子目录下的所有文件路径')
    from fileopts import showdir
    sd = showdir(u'C:\\Users\\banshu\\Downloads')
    print(sd)

    print(u'9、输出某个路径及其子目录下所有以.log为后缀的文件')
    from fileopts import showfiles
    sf = showfiles(u'D:\\logs\\ncss2service', '.log')
    print(sf)

    print(u'10、把原字典的键值对颠倒并生产新的字典')
    dic1 = {"a":"A", "b":"B", "c":"C"}
    dic2 = {y:x for x,y in dic1.items()}
    print(dic1)
    print(dic2)
    from mathopts import reversal
    dic3 = reversal(dic1)
    print(dic3)

    print(u'11、打印九九乘法表')
    from mathopts import multitable
    print(multitable())
