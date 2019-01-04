######################

'''
第7章 像高手一下玩转数据
CHAPTER 7 Mangle Data Like a Pro
像高手一下玩转数据
'''

# 7.1.1 Unicode
print('===========7.1.1 Unicode===========')
'''
早起电脑所使用的ASCII只有128种，只能应付英文和数字以及一些基本的符号，所以发展出了Unicode來面對全世界所有的符号
\\u 加上4位16进制的数字表示Unicode 中的 256 个基本语言，前两位为类别，后两位为索引
\\U 加上8位16进制的数字表示超出上述范围內的字符，最左一位须为0，\\N{name}用来指定字符名称 (完整清单 http://www.unicode.org/charts/charindex.html)
python的unicodedata模块提供了下面两个方向的转换函数：
lookup() - 接受不区分大小写的标准名称，返回一個Unicode的字符;
name() - 接受一个的Unicode字符，返回大写形式的名称。
'''

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"'  % (value, name, value2))

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')
unicode_test('\u2603')

# 想知道é这个符号的编码
place = 'café'
print(place)
unicode_test('é')
print('é'.encode('unicode-escape'))   #这里
unicode_test('\u00e9')

'''
使用utf-8进行编码与解码
将字符串编码为字节；
将字节解码为字符串；
使用encode()来编码字符串成我们看得懂的

编码    说明
'ascii'    ASCII 编码
'utf-8'    最常用的编码
'latin-1'    ISO 8859-1 编码
'cp-1252'    Windows 常用编码
'unicode-escape'    Python 中 Unicode 的文本格式， \\uxxxx 或者 \\Uxxxxxxxx
'''
#编码
snowman = '\u2603'
print('unicode :',snowman)
print('unicode string :',snowman.encode('unicode-escape'))
print('unicode lengh :', len(snowman))
ds = snowman.encode('utf-8')
print('utf-8 lengh :',len(ds))
print('utf-8 string :',ds)
string1 = '☃'
print(string1, '--', unicode_test(string1) )

#解码
place = 'caf\u00e9'
print(place)
place_bytes = place.encode('utf-8')
print(place_bytes)
place2 = place_bytes.decode('utf-8')
print(place2)


# 7.1.2 格式化
print('===========7.1.2 格式化===========')
'''
有两种方法可以格式化文字
string % data
{}.format (新的写法，推荐使用)
f"{Variable Name}" (Python 3.6之後才有)
第一种搭配的format符號表如下
    符号    种类
    %s    字串
    %d    十进制整数
    %x    十六进制整数
    %o    八进制整数
    %f    十进制浮点数
    %e    以科学计数法表示的浮点数
    %g    十进制或科学计数法表示的浮点数
    %%    文本值 % 本身
'''
# 方法一
print('1. %s' % 42)
print('2. %d' % 42)
print('3. %x' % 42)
print('4. %o' % 42)
print('5. %s' % 7.03)
print('6. %f' % 7.03)
print('7. %e' % 7.03)
print('8. %g' % 7.03)
print('9. %d%%' % 100)
print('10. 混合搭配文字[%s]，以及数字[%f]' % ('我是文字',87))

#可搭配数字做位数控制
print('11. %10d' % 42)
print('12. %10.4d' % 42)
print('13. %10.1f' % 42)
print('14. %.1f' % 42)
print('15. %-10d' % 42)
print('16. %-10.1f' % 42)

# 方法二
n = 42
f = 7.03
s = 'string cheese'
print('20. {} {} {}'.format(n, f, s))
print('21. {2} {0} {1}'.format(n, f, s))
print('22. {n} {f} {s}'.format(n=42, f=7.03, s='string cheese'))
 
# 使用字典传入
d = {'n': 42, 'f': 7.03, 's': 'string cheese'}
print('23. {0[f]} {0[s]} {0[n]} {1}'.format(d, 'other')) #0表示format的第一个参数，1表示第二个参数
# 方法一中的format也可以用在新方法，采用:來做衔接
print('===========分隔线===========')
print('24. {0:x} {1:f} {2:s}'.format(n, f, s))
print('25. {n:d} {f:e} {s:s}'.format(n=42, f=7.03, s='string cheese'))
print('===========分隔线===========')
print('26. {0:10d} {1:10f} {2:10s}'.format(n, f, s))        #指定宽度10，默认右对齐
print('27. {0:>10d} {1:>10f} {2:>10s}'.format(n, f, s))     #右对齐
print('28. {0:<10d} {1:<10f} {2:<10s}'.format(n, f, s))     #左对齐
print('29. {0:^10d} {1:^10f} {2:^10s}'.format(n, f, s))     #置中对齐
print('30. {0:>010d} {1:>10.4f} {2:>10.4s}'.format(n, f, s)) #与旧方法不同，整数沒有经度设定项
print('31. {0:!^20s}'.format('BIG SALE'))                   #指定填充符号


# 7.1.3 正则表达式
print('===========7.1.3 正则表达式===========')
'''
采用wiki的说法
正则表示式，又称正规表达式、正规表示法、正则运算式（英语：Regular Expression，在代码中常简写为regex、regexp或RE），
电脑科学的一个概念。正规表示式使用单个字符串来描述、符合一系列符合某个句法规则的字符串。
在很多文字编辑器里，正则表达式通常被用來检索、取代那些符合某个模式的文字。

简单来说，就是可以用來匹配字符串(source)中的规则(pattern)
    import re  #从标准函数库引入
function    功能
    re.match( pattern, source )    查看字串是否以规定的规则开头
    re.search( pattern, source )    会返回第一次成功的匹配值 (如果有成功)
    re.findall( pattern, source)    会返回所有成功且不重复的匹配值 (如果有成功)
    re.split( pattern, source )    会根据 规则 将 字符串 切分成若干段，返回由这些片段组成的list
    re.sub( pattern, replacement, source )    还需一个额外的参数 replacement，它会把 字串 中所有匹配规则的字串 替換成 replacement
'''
import re
# .group()可以叫出符合正则表达式的字符串部分
print('----------match----------')
# 检查'Young Frankenstein'是否以'You'开头
result = re.match('You', 'Young Frankenstein')
if result:
    print(result.group())

print('----------compile后match----------')
# 针对较复杂情況可以先编译一个对象出來加速判断
youpattern = re.compile('You')
result = youpattern.match('Young Frankenstein')
print(result)
if result:
    print(result.group())

print('----------match使用.*找任何位置----------')
# "."为除「\n」之外的任何单个字符。  "*"为符合前面的子运算式零次或多次。
# 组合在一起则成为匹配任意长度任意字元(除「\n」)的规则
m = re.match('.*Frank', 'Young Frankenstein')
if m:
    print(m.group())
 
print('----------search----------')
# 可以不用通过".*"來找任意位置的符合值
m = re.search('Frank', 'Young Frankenstein')
if m: # search返回物件
    print(m.group())

print('----------findall----------')
# 寻找所有符合的
m = re.findall('n', 'Young Frankenstein')
print(m) # findall返回了一个列表
print('共找到', len(m), '个符合值')
#寻找后方至少有一个字符的
m = re.findall('n..', 'Young Frankenstein')
print(m) # findall返回了一个列表
#寻找后方有一个字符(可以沒有)的
m = re.findall('n.?', 'Young Frankenstein')
print(m) # findall返回了一个列表

print('----------split----------')
# 利用规格做切割字符串
m = re.split('n', 'Young Frankenstein')
print(m) # split返回了一个列表

print('----------sub----------')
# 利用字符串替换字符串
m = re.sub('n', '?', 'Young Frankenstein')
print(m) # sub返回了一个列表
#寻找英文单词边界
m = re.findall(r'\bFra', 'Young Frankenstein')
print(m) # findall返回了一个列表

'''
特殊字元    功能
.    代表任意除 \n 外的字符
*    表示任意多个字符(包括 0 个)
?    表示可选字符( 0 个或 1 个)
\d    一个数字字符。等价于[0-9]
\D    一个非数字字符。等价于[^0-9]
\w    一个 字母 或 数字 包括下划线字符。等价于[A-Za-z0-9_]
\W    一个 非字母 非数字 非下划线字符。等价于[^A-Za-z0-9_]
\s    空白字元。等价于[ \f\n\r\t\v]
\S    非空白字元。等价于[^ \f\n\r\t\v]
\b    单词边界（一个 \w 与 \W 之间的范围，顺序可逆）
\B    非单词边界
'''
import string
printable = string.printable  #100个ASCII字符
print(len(printable))
print('2'.zfill(6))
print('20'.zfill(6))
print('200'.zfill(6))
 
print(printable[0:50])
print(printable[50:])
 
print(re.findall('\d', printable))  #找数字
print(re.findall('\w', printable))  #找字母与数字
print(re.findall('\s', printable))  #找空白
 
'''
规则    功能
abc    文本值 abc
(expr)    expr
expr1|expr2    expr1 或 expr2
.    除 \n 外的任何字元
^    源字符串的开头
$    源字符串的结尾
prev?    0 个或 1 个 prev
prev*    0 个或多个 prev，尽可能多地匹配
prev*?    0 个或多个 prev，尽可能少地匹配
prev+    1 个或多个 prev，尽可能多地匹配
prev+?    1 个或多个 prev，尽可能少地匹配
prev{m}    m 个连续的 prev
prev{m, n}    m 到 n 个连续的 prev，尽可能多地匹配
prev{m, n}?    m 到 n 个连续的 prev，尽可能少地匹配
[abc]    a 或 b 或 c(和 a|b|c一样)
[^abc]    非(a 或 b 或 c)
prev (?=next)    如果后面为 next，返回 prev
prev (?!next)    如果后面非 next，返回 prev
(?<=prev) next    如果前面为 prev，返回 next
(?<!prev) next    如果前面非 prev，返回 next
'''
source = '''I wish I may, I wish I might
... Have a dish of fish tonight。'''
 
# 1. 找wish
print("1.", re.findall('wish', source))
 
# 2. 找wish或fish
print("2.", re.findall('wish|fish', source))
 
# 3. 找wish开头
print("3.", re.findall('^wish', source))
 
# 4. 找I wish开头
print("4.", re.findall('^I wish', source))
 
# 5. 找fish结束
print("5.", re.findall('fish$', source))
 
# 6. 找fish tonight(后面可以有无一个字符)
print("6.", re.findall('fish tonight.$', source))
 
# 7. 找fish tonight.(使用转义字符，表示\.为一个点而不是万用字符)
print("7.", re.findall('fish tonight\.$', source))
 
# 8. 找wish与fish
print("8.", re.findall('[wf]ish', source))
 
# 9. 找w、s、h组合出來的字串
print("9.", re.findall('[wsh]+', source))
 
# 10. 找ght开头，后面接着非字母 非数字 非下划线字元
print("10.", re.findall('ght\W', source))
 
# 11. 找I开头，后面是wish，但只返回前面
print("11.", re.findall('I (?=wish)', source))
 
# 12. 找前面开头是I的wish，只返回后面
print("12.", re.findall('(?<=I) wish', source))
 
# 13. 原定希望找到fish然后前面是单词的地方，但是\b被当做是转义字符返回符号了
print("13.", re.findall('\bfish', source))
 
# 14. 所以采用r來声明说我这是一个原始的字符串，不需要自动转换
print("14.", re.findall(r'\bfish', source))
 
print('\n--------------------')
#用括号规则做区分后可以通过groups()取得分开的tuple，並且可以通过<name>设定名称
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())
 
m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
 
print(m.group('DISH'))
print(m.group('FISH'))


# 7.2.1 bytes and bytearray
print('===========7.2.1 bytes and bytearray===========')


# 7.2.2 使用struct转换二进制数据
print('===========7.2.2 使用struct转换二进制数据===========')


# 7.2.3 其他二进制数据工具
print('===========7.2.2 使用struct转换二进制数据===========')


# 7.2.4 binascii函数
print('===========7.2.4 binascii函数===========')


# 7.2.5 位运算符
print('===========7.2.5 位运算符===========')


# 7.3 练习
print('===========7.3 练习===========')
print("(1). " )



