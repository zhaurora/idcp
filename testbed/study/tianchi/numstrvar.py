'''
Created on 2018年9月30日
@author: banshu
'''

if __name__ == '__main__':
    pass

'''
【Python入门】Python数据处理编程基础
https://tianchi.aliyun.com/learn/liveDetail.html?spm=5176.11510288.0.0.76f2b7bd4SQN3W&classroomId=218
第1章 Python的基本元素：数字，字符串和变量
CHAPTER 1 Numbers, Strings,and Variables
'''
#第一个语句
print("Python的基本元素：数字，字符串和变量")

#Python是强类型的(Strongly typed)
print("int('1') + 2 = " + str(int('1') + 2) )
print("'1' + str(2) = " + str('1' + str(2)) )

#在使用print()指令时，会自动将转义字符转换成正确的显示方式(ex. \n转换成换行等等)
print('a','b','c') # 'a' 'b' 'c'

#字串连接接可以使用 + 号或是直接把两字串摆在前后即可。( print('a'+'b') print('a''b') 都可以得到 'ab'的结果 )
#使用 * 可以快速建立重复字串。
print('a' * 5) # 'aaaaa'

#前面提到字符串为字符的阵列，故可以使用[ ]來提取特定位置之字符
arra = 'bcd'    
print(arra[0]) #'b' 
print(arra[-1]) #'d'
#index从0开始，-1为最后一个字符

#更多方法
arrb = 'abcde'
print(arrb[::-1]) #'edcba' 可以变成反序排列
print(arrb[-2:0:-1]) #'dcb'
print(arrb[0:2]) #'ab'

#其中变量內的字符串是不能替换內容(因为容器为类似TUPLES的类型，CH3会说明)， 若要替换內容，则可以使用重组或是 string.replace()
name = 'Henny'
#name[0] = 'P' #错误!!!!!!
namea = name.replace('H', 'P') #'Penny'
print(namea)
print('Po' + name[2:]) #'Ponny'

#len() 可以获取字符串长度
lena = 'abc'
print(len(lena))

#string.split()可以分割字串成list，( )內可以指定符号，默认会切割\n(换行) 、 \t(tab)与空格三种
splita = 'get gloves,get mask,give cat vitamins,call ambulance'
print(splita.split(','))
print(splita.split())

joina = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
print(', '.join(joina))

#string.startswith() 与 string.endswith() 分別可以检查开头結束字串是否为特定字串，返回True或False
witha = 'abcdef'
print(witha.startswith('ab'))
print(witha.endswith('eef'))

#string.find() 与 string.rfind() 可以查询第一次与最后一次出现搜索字串的index，string.count()可以查询字串出现次数
finda = 'abcdefbcd'
print(finda.find('bc'))
print(finda.rfind('bc'))
print(finda.count('bc'))

#string.isalnum()可以查询字符串中是否都是字母或数字，返回True或False
allnum = 'abc@def'
print(allnum.isalnum())

#其他还有一些方便的string內建function可以使用
setupstring = 'a duck goes into a bar...'
print(setupstring.strip('.'))                      #刪除結尾特定符号 'a duck goes into a bar'
print(setupstring.capitalize())                    #字串第一個字符大写 'A duck goes into a bar...'
print(setupstring.title())                         #每个单词的首字母大写'A Duck Goes Into A Bar...'
print(setupstring.upper())                         #全部大写 'A DUCK GOES INTO A BAR...'
print(setupstring.lower())                         #全部小写'a duck goes into a bar...'
print(setupstring.swapcase())                      #大小写交换 'a DUCK GOES INTO A BAR...'
print(setupstring.center(30))                      #将字符串中心移动至30个字符的中间 '  a duck goes into a bar...   '
print(setupstring.ljust(30))                       #左对齐 'a duck goes into a bar...     '
print(setupstring.rjust(30))                       #右对齐 '     a duck goes into a bar...'
print(setupstring.replace('duck', 'marmoset'))     #'a marmoset goes into a bar...'
print(setupstring.replace('a ', 'a famous ', 100)) #只替换前100个'a '


'''
本章介绍了 Python 最基本的元素:数字、字符串以及变量。我们试着在notebook里完成一些相关的练习。
(1) 一个小时有多少秒?这里，请把交互式解释器当作计算器使用，将每分钟的秒数(60) 乘以每小时的分钟数(60)得到结果。
(2) 将上一个练习得到的结果(每小时的秒数)赋值给名为 seconds_per_hour 的变量。
(3) 一天有多少秒?用你的 seconds_per_hour 变量进行计算。
(4) 再次计算每天的秒数，但这一次将结果存储在名为 seconds_per_day 的变量中。
(5) 用 seconds_per_day 除以 seconds_per_hour，使用浮点除法(/)。
(6) 用 seconds_per_day 除以 seconds_per_hour，使用整数除法(//)。除了末尾的 .0，本 练习所得结果是否与前一个练习用浮点数除法得到的结果一致?
'''

print("练习");

#(1)
print("(1) 1小时="+str(60*60)+"秒")

#(2)
seconds_per_hour = 60*60
print("(2) 1小时="+str(seconds_per_hour)+"秒")

#(3)
print("(3) 1天="+str(60*60*24)+"秒")

#(4)
seconds_per_day = seconds_per_hour * 24
print("(4) 1天="+str(seconds_per_day)+"秒")

#(5)
print("(5)  seconds_per_day / seconds_per_hour="+ str(seconds_per_day/seconds_per_hour) )

#(6)
print("(6)  seconds_per_day // seconds_per_hour="+ str(seconds_per_day//seconds_per_hour) )

