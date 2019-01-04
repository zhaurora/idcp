'''
Created on 2018年9月30日

@author: banshu
'''
import random
if __name__ == '__main__':
    pass

'''
第4章 Python外壳，代码结构
CHAPTER 4 Py Crust: Code Structures
'''

# 4.1 4.2 注释与连接
# 使用 # 可以注释单行
# 使用 \ 可以连接多行

# 我是注释，別理我
print('===========4.1 4.2 注释与连接===========')
print('两种不同的连接多行方法:')
alphabet = ''
alphabet += 'abcdefg'
alphabet += 'hijklmnop'
alphabet += 'qrstuv'
alphabet += 'wxyz'
print(alphabet)

alphabet = 'abcdefg' + \
    'hijklmnop' + \
    'qrstuv' + \
    'wxyz'
print(alphabet)
 
print('运算式也可以切断')
aformula = 1 + 2 + \
    3
print(aformula)


# 4.3 使用if、elif与else进行逻辑判断
# 注意!!!记得使用冒号(：)做结尾!!!
# 使用4个空格作为区域划分
print('===========4.3 使用if、elif与else进行逻辑判断===========')
disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

# 槽状判断式结构
furry = False
small = True
if furry:
    if small:
        print("It's a cat.")
    else:
        print("It's a bear!")
else:
    if small:
        print("It's a skink!") #answer is here
    else:
        print("It's a human. Or a hairless bear.")

# 值的判断
color = "puce"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color) #answer is here

''''
以下判断结果会返回 True 或 False
判断式    判断符号
相等    ==
不等于    !=
小于    <
小于等于    <=
大于    >
大于等于    >=
属于    in
'''
# and 可以连接判断结果，两者都为True才是True
# or 前后两者只要有一个为True就会返回True
# not 取反T → F 或是 F → T
x = 7
print(5 < x or x < 10) #T
print(5 < x and x > 10) #F
print(5 < x and not x > 10) #T
print(5 < x < 10) #T

'''
以下集中在判断时为False，其余都是True
类型    值
布尔值    False
null类型    None
整数    0
浮点数    0.0
空字符串    ''
空Tuples    ()
空Lists    []
空Dictionaries    {}
空Set    set()
'''
some_list = []
if some_list: #F
    print("There's something in here")
else:
    print("Hey, it's empty!")

# 4.4 使用while进行循环
print('===========4.4 使用while进行循环===========')
# 一样记得冒号和空4格!!!
# 使用break可以跳出循环
# 使用continue可以跳过次循环的后续，进行下一次循环
# 使用else可以判断沒有使用break时的情況
print('Case 1：一般使用while时')
count = 1
while count <= 5:
    print(count, end=', ')
    count += 1
 
print('\nCase 2：使用break，遇到3跳出循环')
count = 1
while count <= 5:
    if count == 3:
        break
    print(count, end=', ')
    count += 1
 
print('\nCase 3：使用continue，跳过值是3时的输出')
count = 1
while count <= 5:    
    if count == 3:
        count += 1
        continue
    print(count, end=', ')
    count += 1
 
print('\nCase 4：使用else，若没有使用break则执行段')
count = 1
while count <= 5:
    if count == 6:
        break
    print(count, end=', ')
    count += 1
else:
    print('NO break!')


# 4.5 使用for迭代
print('===========4.5 使用for迭代===========')
# 还是老话一句!!記得冒号和空4格!!!
# python中频繁的使用迭代器，可以遍历整个容器结构，不须知道长度。就可以调出元素，符合python的精神!!
# 一样也可以使用break, continue 与 else语法作为迭代的控制
print('方法一：使用while方法遍历每一个Object')
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1
 
print('\n方法二：使用for方法遍历每一个Object')
for i in rabbits:
    print(i)
 
print('\n列举出字符串的每一个字母')
word = 'cat'
for letter in word:
    print(letter)
 
print('\n列举出Dictionaries中的每一个key值')
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation: # 或者是for card in accusation.keys():
    print(card)
 
print('\n列举出Dictionaries中的每一个value值')
for value in accusation.values():
    print(value)
 
print('\n列举出Dictionaries中的每一组Object，以Tuples输出')
for item in accusation.items():
    print(item)
 
print('\n更改上面写法，改为使用两个参数去接key和value')
for card, contents in accusation.items():
    print('key：', card, ',\t value：', contents)


abc = 'abcdefghi'
for chart in abc:
    if chart == 'c':
        continue
    if chart == 'g':
        break
    print(chart)
else:
    print('g is not in here')

# 使用zip()可以对多组Object同时进行循环迭代!!!好用!!!
# 下面示范原本的方法和zip()的用法差异，有点再与自动以最短__的Object做为参考，不会爆掉
# __zip()完的Object为tuple
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
print('原方法：')
for i in range(len(days)):
    print(days[i], ": drink", drinks[i], "- eat", fruits[i], "- enjoy", desserts[i])
 
print('zip()用法：')
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

# 打包list、dict 
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(english, french)
print('转换成list包tuple')
print(list( zip(english, french) ))
print('转换成Dictionarie')
print(dict( zip(english, french) ))

# 使用range()产生自然数序列
# 使用上如同slices()：range( start, stop, step)，start默认为0
print('Case1：迭代0~2')
for x in range(0,3):
    print(x)
 
print('Case2：迭代2~0')
for x in range(2, -1, -1):
    print(x)
 
print('Case3：也可以直接转为list Object')
print(list( range(3) ))
print(list( range(3, 1, -1) ))



# 4.6 Comprehensions 推导式
print('===========4.6 Comprehensions 推导式===========')
# 可以简单漂亮的写出python风格的语法
# 这些方法很好用，代码会更加简洁漂亮!
print('list的推导式')
'''
listObj = [expression for item in iterable if condition]
 简单來說"for item in iterable"为原来的for循环开头 "if condition"为判断式
 "expression"为处理输出结果
 "[]"为转换为list的部分
 不懂的話就直接看看以下示例吧~
 目标创建一个list，包含1~5
'''
 
# 在学到第三章时你要创建一个list可能会使用以下方法
print('Case 1')
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)
# 再稍微前面的一点时你会学到用for循环处理
print('Case 2')
number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)
# 或是把list用上
print('Case 3')
print(list(range(1, 6)))
# 但是，这边起提供一个更为漂亮的写法，而且灵活度高
print('Case 4')
print([number for number in range(1,6)])

# 可以对expression部分进行运算处理
print("运算1=", [(number*2 - 3) for number in range(2,5)])
# 可以放置if判断式
print("运算2=", [number for number in range(1,6) if number % 2 == 1])
# 上面那个改成正常循环的写法如下，你喜欢哪个呢?
a_list = []
for number in range(1,6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list)
print('----')

# 嵌套循环也可以使用隐含式办到
# 嵌套的順序就按照出现的順序依序往內
rows = range(1,4)
cols = range(1,3)
cells = []
for row in rows:
    for col in cols:
        cells.append((row, col))
for cell_r, cell_c in cells:
    print(cell_r, cell_c)
 
print('----')
# 隐含式版本
cells = [(r,c) for r in range(1, 4) for c in range(1, 3)]
for cell_r, cell_c in cells:
    print(cell_r, cell_c)

print('dictionary推导式')
#dictionaryObj = { key_expression : value_expression for expression in iterable if condition}
'''
for expression in iterable为for循环部分
key_expression为key值
value_expression为value值
if condition为判断式
{} 表示为一个dictionary
'''
# 计算一个单字里字母的出现的次数
# 使用Set排除重复字母
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word) if letter.lower() not in 'aeiou'}
print(letter_counts)
oneway = "洗洗睡啦"
print(set(oneway))

print('set推导式')
#set_Obj = {expression for expression in iterable if condition}
#如同list的使用方法
print({number for number in range(1,6) if number % 3 == 1})

print('set推导式')
'''
tuples没有推导式的用法，使用()包起來是generator推导式的用法
简单来说就是可以产生像是range()的Object，亦表示可以直接对齐迭代
记住!!!generator只能使用一次!!!
'''
number_thing = (number*3-2 for number in range(1, 6))
print((1,))
print(number_thing)
for number in number_thing:
    print(number)
 
# 或者转为list使用
number_list = list(number_thing)
print(number_list)
print('因为只能使用一次，所以上面这边找不到东西了')

number_thing = (number*3-2 for number in range(1, 6))
number_list = list(number_thing)
print(number_list)


# 4.7 Function 函数
print('===========4.7 Function 函数===========')
'''
目的，重复使用代码，将代码模块化，方便维护管理
定义函数
调用函數
一样记得冒号和空四格!!
不一定要return，但有return一定要有变量接住他，或是使用他。若此function沒有return则返回None
def function_name():
    return some
result = function_name()
'''
# 定义function
def make_a_sound():
    print('quack')
def agree():
    return True
 
# 使用function
make_a_sound()
# 赋值变量
isagree = agree()
print(isagree)
 
# 或是直接使用返回值
if not agree():
    print('Splendid!')
else:
    print('That was unexpected.')
 
# return的类型不限
def echo(anything):
    return anything + ' ' + anything
print(echo('HEY~'))
def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."
 
print(commentary('blue'))
# 若此function沒有return则返回None
print(make_a_sound())

print('位置参数与关键字参数')
# 要把参数传进function中有两种方法，位置参数与关键字参数，示例如下 (如果同时出现，则以位置参数优先)
# 可以在定义函数时，设定默认值，若使用function时沒有填入改参数，則使用默认值，有的话则覆盖
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert} #酒、主餐、晚餐
print(menu('chardonnay', 'chicken', 'cake')) #夏敦埃酒、鸡肉、蛋糕
print(menu(entree='beef', dessert='bagel', wine='bordeaux')) #牛肉、面包圈、波尔多酒
print(menu('frontenac', dessert='flan', entree='fish')) #特纳克红酒、果馅饼、鱼肉

#默认
def menu2(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
print(menu2('chardonnay', 'chicken'))
print(menu2('dunkelfelder', 'duck', 'doughnut')) #丹科飞德红酒、鸭肉、炸面圈

# 特別注意!!!!若把空list当做默认值会发生意料之外的事情
def buggy(arg, result=[]):
    result.append(arg)
    print(result)
# 第一次使用时OK
buggy('a')
# 第二次使用时就会残存上次的结果 ！！！！
buggy('b')

# 可以使用以下方法修改function
def works(arg):
    result = []
    result.append(arg)
    return result
def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

works('a')
works('b')
nonbuggy('a')
nonbuggy('b')

print('使用 * 与 ** 收集位置参数与关键字参数')
# *收集而成的参数会以Tuples储存
# **收集到的会以Dictionary储存
print('全部都给收集器')
def print_args(*args):
    print('Positional argument tuple:', args)
print_args()
print_args(1,2,3)

print('混合位置参数使用，剩下的都给收集器')
def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args) #tuples
print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax') #“帽子”、“手套”、“围巾”、“单片眼镜”、“胡须蜡”

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs) #dictionary
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon') #墨尔乐红酒、羊肉、小杏仁饼

print('function 说明文字')
# 为了提高代码的可读性，可以对自行定义出的函数加上说明文字，他人在使用时就可以使用help叫出文字
def echo2(anything):
    'echo2 returns its input argument'
    return anything
 
def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The operation is:
    1. Check whether the *second* argument is true.
    2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)
 
help(echo2)
print('--------------------------------')
help(print_if_true)
 
print('仅叫出文字↓')
print(echo2.__doc__)
print('--------------------------------')
print(print_if_true.__doc__)

print('一等公民：function')
# 在python的设计中，function是一级公民。
# 换句话说python是Object导向的语言，所有的东西都是Object，连function也是。
# 所以说function可以当成参数传入其他function，也可以将function当成结果回传。
def run_something(func, a, b):
    print(func(a, b))
def add(a, b):
    return a + b

run_something(add, 2, 3)
test = add
print(test(3,5)) #add(3,5)

print('內部函数')
# function內部可以再定义function
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(4, 7))

print('闭包')
# 可以动态生成函數，可用来记录外部传入的变量
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2
 
a = knights2('XDD')
print(a())
print(a) #object

print('匿名函数：lambda()')
# 当想要传入一个小function作为使用时，却又不想定义出來，可以使用匿名函數
def edit_story(words, func):
    for word in words:
        print(func(word))
stairs = ['thud', 'meow', 'thud', 'hiss']
def enliven(word):
    return word.capitalize() + '!'
 
# 原做法
edit_story(stairs, enliven)
print('-----')
# 匿名函数做法
edit_story(stairs, lambda word: word.capitalize() + '!')



# 4.8 Generators 生成器
print('===========4.8 Generators 生成器===========')
'''
生成器式用来创建一个序列Object，但是又可以不用事前将一整个序列存到内存中，会随着每一次执行而改变数值
每次循环生成器时，它会记录上一次调用的位置，并返回下一个值。
这一点和普通的函数是不一样的，一般函數都不记录前一次调用用，而且都会在函数的第一行开始执行。
內建的range()就是一种生成器。
'''
# 自制range函数
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number 
        #yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。
        #重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。
        number += step
        
ranger = my_range(1, 5)
print(ranger)
for x in ranger:
    print(x)
 
print('------')
print(my_range)
for x in my_range(1, 5):
    print(x)


# 4.9 Decorators 装饰器
print('===========4.9 Decorators 装饰器===========')
# 用来修改已经存在的函数，可以针对结果进行再次包装处理产生新的函数。
#装饰器1
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function
def add_ints(a, b):
    return a + b
 
print('---------原函数結果----------')
print(add_ints(3, 5))
print('---------人工对装饰器赋值------------')
cooler_add_ints = document_it(add_ints)
print(cooler_add_ints(3, 5))

print('---------直接添加装饰器------')
@document_it
def add_ints2(a, b):
    return a + b
print('@document_it\ add_ints2(3, 5)')
print(add_ints2(3, 5))

# 装饰器2
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        print("square_it(func)", func.__name__)
        return result * result
    return new_function

print('---------套用一个以上的装饰器-')
@document_it # 后装饰
@square_it # 先装饰
def add_ints(a, b):  #### 看不懂！！！！！！！！！！！
    return a + b
print(add_ints(3, 5))
 
print('\n交换装饰器顺序，若新的处理过程是可以做乘除交换则结果不变，但过程会变')
@square_it # 后装饰
@document_it # 先装饰
def add_ints(a, b):
    return a + b
 
print(add_ints(3, 5))


# 4.10 Namespaces and Scope 命名空间与作用域
print('===========4.10 Namespaces and Scope 命名空间与作用域===========')
# 在主程式(main)中的变量称为全局变量，可以在函数中调用，但不能改变他。
# 在函数內出现与全局变量相同名称的变量则是另一个不同的变量，则可以改变值。
animal = 'fruitbat' #果蝠
def print_global():
    print('inside print_global:', animal)
 
print('可以在函数内调用全部变量。')
print_global()
 
 
def change_and_print_global1():
    # print('inside change_and_print_global1:', animal) #此调用会出错
    animal = 'wombat' #袋熊
    print('inside change_and_print_global1:', animal) #同change_and_print_global2

change_and_print_global1()
print('单无法改变他，会出错。')
# 可以尝试取消注释试试
#change_and_print_global()
 
def change_and_print_global2():
    animal = 'wombat2'
    print('inside change_and_print_global2:', animal)
 
print('\n若要在函数内使用相同名称的变量，且需不同于全局变量，必须先赋值方可使用。')
change_and_print_global2()
 
print('\n若是在函数内想改变全局变量则使用 global即可')
def change_and_print_global3():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)
 
change_and_print_global3()
print('\n外面的同时也会被改变', animal)


# 4.11 Handle Errors with try and except 处理错误
print('===========4.11 Handle Errors with try and except 处理错误===========')
# 代码在出现错误时可以确保他继续执行下去不会停摆!!!也有人用来测试函数存在与否用
'''
try:
    #执行的內容
except:
    #错误后执行的內容
'''
short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list)-1, ' but got',position)
    
# 有一些內建的错误捕捉方法可以使用
def interr(value):
    short_list = [1, 2, 3]
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', err)
    except Exception as other:
        print('Something else broke:', other)
 
interr(0)
interr(1)
interr(2)
interr(3)
interr('two')

''' Exception List
异常名称 描述
BaseException 所有异常的基类
SystemExit 解释器请求退出
KeyboardInterrupt 用户中断执行(通常是输入^C)
Exception 常规错误的基类
StopIteration 迭代器没有更多的值
GeneratorExit 生成器(generator)发生异常来通知退出
SystemExit Python 解释器请求退出
StandardError 所有的内建标准异常的基类
ArithmeticError 所有数值计算错误的基类
FloatingPointError 浮点计算错误
OverflowError 数值运算超出最大限制
ZeroDivisionError 除(或取模)零 (所有数据类型)
AssertionError 断言语句失败
AttributeError 对象没有这个属性
EOFError 没有内建输入,到达EOF 标记
EnvironmentError 操作系统错误的基类
IOError 输入/输出操作失败
OSError 操作系统错误
WindowsError 系统调用失败
ImportError 导入模块/对象失败
KeyboardInterrupt 用户中断执行(通常是输入^C)
LookupError 无效数据查询的基类
IndexError 序列中没有没有此索引(index)
KeyError 映射中没有这个键
MemoryError 内存溢出错误(对于Python 解释器不是致命的)
NameError 未声明/初始化对象 (没有属性)
UnboundLocalError 访问未初始化的本地变量
ReferenceError 弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError 一般的运行时错误
NotImplementedError 尚未实现的方法
SyntaxError Python 语法错误
IndentationError 缩进错误
TabError Tab 和空格混用
SystemError 一般的解释器系统错误
TypeError 对类型无效的操作
ValueError 传入无效的参数
UnicodeError Unicode 相关的错误
UnicodeDecodeError Unicode 解码时的错误
UnicodeEncodeError Unicode 编码时错误
UnicodeTranslateError Unicode 转换时错误
Warning 警告的基类
DeprecationWarning 关于被弃用的特征的警告
FutureWarning 关于构造将来语义会有改变的警告
OverflowWarning 旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning 关于特性将会被废弃的警告
RuntimeWarning 可疑的运行时行为(runtime behavior)的警告
SyntaxWarning 可疑的语法的警告
UserWarning 用户代码生成的警告
'''


# 4.12 练习
print('===========4.12 练习===========')

# (1) 将 7 赋值给变量 guess_me，然后写一段条件判断(if、else 和 elif)的代码:
# 如果 guess_me 小于 7 输出 'too low';大于 7 则输出 'too high';等于 7 则输出 'just right'。
print('(1)')
guess_me = random.randint(1,10)
if guess_me < 7:
    print("guess_me ", guess_me, " is too low")
elif guess_me > 7:
    print("guess_me ", guess_me, " is too high")
else:
    print("guess_me ", guess_me, " is just right")

# (2) 将 7 赋值给变量 guess_me，再将 1 赋值给变量 start。写一段 while 循环代码，比较 start 和 guess_me:
# 如果 start 小于 guess_me，输出 too low;如果等于则输出 'found it!' 并终 止循环;如果大于则输出 'oops'，然后终止循环。在每次循环结束时自增 start。
print('(2)')
guess_me = 7
start = 1
while start <= guess_me:
    if start < guess_me:
        print("start ", start, " is too low")
    else:
        print("oops!!")
    start += 1

# (3) 使用 for 循环输出列表 [3, 2, 1, 0] 的值。
print('(3)')
for inum in range(3,-1,-1):
    print("inum is ", inum)

# (4) 使用列表推导生成 0~9(range(10))的偶数列表。
print('(4)，列表，中括号[]')
listObj = [ilist for ilist in range(1,10) if ilist%2==0]
print(listObj)

# (5) 使用字典推导创建字典 squares，把 0~9(range(10))的整数作为键，每个键的平方作为对应的值。
print('(5)，字典，大括号{}')
dictionaryObj = { k : k**2 for k in range(1,10) }
print(dictionaryObj)

# (6) 使用集合推导创建集合 odd，包含 0~9(range(10))的奇数。
print('(6)，集合，大括号{}')
set_Obj = {number for number in range(1,10) if number % 2 == 1}
print(set_Obj)

# (7) 使用生成器推导返回字符串 'Got ' 和 0~9 内的一个整数，使用 for 循环进行迭代。
print('(7)，generator，小括号()')
string_thing = ('Got '+str(number) for number in  range(0,10) )
idx = random.randint(0,10)
string_thing = list(string_thing);
print(string_thing[idx])
for wd in string_thing[idx]:
    print(wd)

# (8) 定义函数 good:返回列表 ['Harry','Ron','Hermione']。
print('(8)')
def good():
    return ['Harry','Ron','Hermione']
print(good())

# (9) 定义一个生成器函数 get_odds:返回 0~9 内的奇数。使用 for 循环查找并输出返回的第三个值。
print('(9)')
def get_odds(first=0, last=10, step=1):
    number = first
    while number < last:
        #yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。
        #重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。
        if number%2==1:
            yield number 
        number += step
    

ranger = get_odds(0,10)
for iodd in ranger:
    if iodd == 5:
        print(iodd)

# (10) 定义一个装饰器 test:当一个函数被调用时输出 'start'，当函数结束时输出 'end'。
print('(10)')
def test(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        print(' args :', args)
        return result
    return new_function

def outstr(astr):
    return astr

print(outstr("start")," ",outstr("end"))
toutstr = test(outstr) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(toutstr("start")," ",toutstr("end"))

# (11) 定义一个异常 OopsException:编写代码捕捉该异常，并输出 'Caught an oops'。
print('(11)')
#最简单的自定义异常
class OopsException(Exception):
    pass

def string(value):
    try:
        print(value)
        raise OopsException(value);
    except IndexError as err:
        print('Bad index:', err)
    except OopsException as oper:
        print('Caught an oops:', oper)
    except Exception as other:
        print('Something else broke:', other)

string("xxx")

# (12) 使用函数 zip() 创建字典 movies:匹配两个列表 titles = ['Creature of Habit','Crewel Fate'] 
# 和 plots = ['A nun turns into a monster', 'A haunted yarn shop']。
print('(12)')
titles = ['Creature of Habit','Crewel Fate'] 
plots = ['A nun turns into a monster', 'A haunted yarn shop']
print(dict( zip(titles, plots) ))



