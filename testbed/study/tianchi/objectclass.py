'''
第6章 Python对象和类
CHAPTER 6 Oh Oh: Objects and Classes
对象和类
'''
# 6.1 什么是对象
print('===========6.1 什么是对象===========')
'''
第二章提到，python裡面所有的东西都是对象(objects)，连同一个整数也是一种对象，python的语法设计可以巧妙的隐藏诸多细节
本章节将会介绍自定义新的对象以及修改现有的对象。
对象包含属性(attribute)与方法(methods)，
例如整数5和7都是整数object，都包含了基本的+-*/方法，
'cat' 和 'duck'都是字符串Object，都包含了 capitalize() 和 replace() 两种方法
所以当你要创建一个新的object时，就必须先定义一个新的类，用它来清楚规范其类别可以创造出来的对象有什么样的属性(attribute)与方法(methods)
Object像名词，方法就像个动词。Object代表一个独立的事物，方法用来定义它如何与其他Object相互作用。
与模块不同的是，你可以同时创建多个同类别的Object，他们之间的属性值可能各有不同，对象像是个结构，包含着数据。
'''

# 6.2 使用Class定义类
print('===========6.2 使用Class定义类===========')
# 我们可以通过class来定义自己的类，就可以创造出新的Object

# 自定义一个Person()
# __init__为定义属性部分
# self为object自己
class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def XDD(self, tem):
        return 'I am ' + self.name + tem
 
hunter = Person('Elmer Fudd', "QQ@WW.tw")
Husky = Person('Hsuky', "XDD@WW.tw")
 
print(hunter.name)
print(hunter.email)
print(hunter.XDD('!!!'))
 
print(Husky.name)
print(Husky.email)


# 6.3 继承
print('===========6.3 继承===========')
# 在编写类时，如果发现已经有前人开发过，那就可以不用整段赋值，可以采用继承的方法取得他的属性与方法。 
# 并且补充自己会用的功能，一方面可以减少去改已有的类的辛苦，也可以省去复制粘贴的功夫。
class math():
    def add(self, a, b):
        print("add:", a + b)
 
class mean63(math):
    pass
    
ab = mean63()
ab.add(1, 3)
 
ac = math()
ac.add(1,3)

# 6.4 覆盖方法
print('===========6.4 覆盖方法===========')
# 当然我们也可以覆盖掉原有的方法
class mean64(math):
    def add(self, a, b):
        print("add+1:", a + b + 1)
    
ab = mean64()
ab.add(1, 3)

ac = math()
ac.add(1,3)


# 6.5 添加新方法
print('===========6.5 添加新方法===========')
# 前面的都是复制与修改接着我们也可以在新的类中加入新的方法
class mean65(math):
    def less(self, a, b):
        print("less:", a - b)
    
ab = mean65()
ab.add(1, 3)
ab.less(1, 3)
 
ac = math()
ac.add(1, 3)

# 6.6 使用super从父类得到帮助
print('===========6.6 使用super从父类得到帮助===========')
# 那如果我们要修改属性部分( __int__ )，除了直接重写一个盖掉以外还有super()方法可以用來扩充既有的屬性，这样才有达到继承的目的
class Person66(Person):
    def __init__(self, name, email, birthday):
        super().__init__(name, email)
        self.birthday = birthday

hunter = Person('Elmer Fudd', 'QQ@CC.tw')
husky = Person66('Elmer Fudd', 'QQ@CC.tw', '2016/05/07')
 
print(hunter.name)
print(hunter.email)
# print(hunter.birthday) #AttributeError: 'Person' object has no attribute 'birthday'
print('=============')
print(husky.name)
print(husky.email)
print(husky.birthday)


# 6.7 self
print('===========6.7 self===========')
'''
在定义属性時常常会看到self，self指的就是被创建出來的Object本身。
所以在__int__(self, name)的参数部分，实际上不需要传入self参数。

class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email

XDD = Person('QQ', 'QQ@gmail.com')  #不需要传入self参数
'''

# 6.8 使用属性对特性进行访问和设置
print('===========6.8 使用属性对特性进行访问和设置===========')
'''
在其他語言中，可以设置getter 和 setter來确保私有属性的读写，但是在python一切都是公开的，
可以通过property()來达到python风格的写法，即可將属性值藏起來，不用通过调用每个getter()和setter()來达到改变私有变量
若沒有给定setter函数，则无法通过property()來改变属性值，当然前提是在別人不知道实际存储变量的属性名称是什么
'''
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    #取的 name 的函数
    def get_name(self):
        print('---使用get函数---')
        return self.hidden_name + '!!'
    #设定 name 的函数
    def set_name(self, input_name):
        print('---使用set函数---')
        self.hidden_name = input_name + '??'
    #使用property(get,set)來包裝，让使用上更方便
    name = property(get_name, set_name)

#定义Object为Duck类，并给定name，从头到尾都沒有直接抄作hidden_name來改变属性值
fowl = Duck('Howard')
print('提取名称时，则调用get函数')
print(fowl.name)
print('设定名称时，则调用set函数')
fowl.name = 'Daffy'
print('nname被改成Daffy')
print(fowl.name)
 
print('当然也可以通过原始的set_name()与get_name()进行修改私有属性')
print(fowl.get_name())
fowl.set_name('Daffyyyy')
print(fowl.get_name())

print('===============')

#当然可以通过装饰器，来写得更漂亮!!!
class Duck2():
    def __init__(self, input_name):
        self.hidden_name = input_name
    
    @property
    def name(self):
        print('---使用get函数---')
        return self.hidden_name
 
    @name.setter
    def name(self, input_name):
        print('---使用set函数---')
        self.hidden_name = input_name
        
#定义Object为Duck类，并给定name
fowl2 = Duck2('Howard')
 
print('提取名称时，则调用get函数')
print(fowl2.name)
print('设定名称时，则调用set函数')
fowl2.name = 'Daffy'
print('nname被改成Daffy')
print(fowl2.name)


# 6.9 使用名称重整保护私有特性
print('===========6.9 使用名称重整保护私有特性===========')
# 前面的用法如果被知道实际储存属性的名称为什么，也是可以对其修改 所以可以通过名称重整来把实际储存的名称改写
# 在属性名称前面加上( __ )來重整名称，虽然不能完全的防止修改私有属性，但可以通过有效的方法降低有意或无意的修改
class Duck3():
    def __init__(self, input_name):
        self.__name = input_name
    
    @property
    def name(self):
        print('---使用get函數---')
        return self.__name
    
    @name.setter
    def name(self, input_name):
        print('---使用set函數---')
        self.__name = input_name

fowl3 = Duck3('Howard')
print(fowl3.name)
fowl3.name = 'Donald'
print(fowl3.name)
#fowl.__name        #直接修改會錯誤
#fowl._Duck__name   #重整完的名稱


# 6.10 方法的类型
print('===========6.10 方法的类型===========')
'''
前面教的都是Object的方法，对于类本身也是可以设定属性以及方法
分別使用 类.属性 以及 @classmethod
在类的方法中，调用自己使用 cls 或是 类名称 皆可以
还有一中 @staticmethod 可以设定类的函數，差异在于

@staticmethod不需使用cls参数
@classmethod第一个参数需为cls参数
在使用上來说，若@staticmethod要调用到这个类的属性只能直接用名称來取得，而@classmethod因为有cls参数传入，所以可以通过cls来调用类函数
'''
class A():
    count = 0           #类属性
    def __init__(self):
        A.count += 1    #修改类属性
    
    def exclaim(self): #你是谁
        print("I'm an A!")
    
    @classmethod        #类方法(methond)
    def kids(cls):
        print("A has ", cls.count, " little objects.")
        
    @classmethod        #类方法(methond)
    def kids2(A):
        print("A has ", A.count, " little objects.")
 
easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()
nify_a = A()
A.kids2()
  
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')
        
CoyoteWeapon.commercial()


# 6.11 鸭子类型
print('===========6.11 鸭子类型===========')
'''
在Object导向的语言中多态(polymorphism)的使用，可以让我们更方便地调用Object的函数
不用管Object本身的类型是什么，只要拥有相同的方法就可以调用到
鸭子一词的由来，如果能像鸭子一样叫，像鸭子一样走路，那他就是一只鴨子。
所以我們不用太在意是什么Object，只要他能够有一样的方法可以使用，那我们就可以安心的使用了
'''
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    
    def who(self):
        return self.person
 
    def says(self):
        return self.words + '.'
    
class BabblingBrook():
    def who(self):
        return 'Brook'
    
    def says(self):
        return 'Babble'
    
hunter = Quote('Elmer Fudd', "I'm hunting rabbits")
brook = BabblingBrook()
 
#尽管两者完全独立没有关系，但只要有相同名称的函数就可以调用到
def who_says(obj):
    print(obj.who(), 'says', obj.says())
    
who_says(hunter)
who_says(brook)


# 6.12 特殊方法
print('===========6.12 特殊方法===========')
'''
在python中，存在一些特殊方法( special method )或者称为( magic method )，
这些方法为双下划线( __ )开头与结尾的用法，前面介绍过的( __init__ )就是一个特殊方法，他是用來对新Object初始化用
假设我有一个class里面有个method可以用來判断两个字符串的小写是否相同
'''
#---------------采用一般方法写法
class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

#创建3个字符Object
first = Word('ha')
second = Word('HA')
third = Word('eh')

#进行比较
print(first.equals(second))  #True
print(first.equals(third))   #False

#---------------采用特殊方法写法
class Word2():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

#创建3个字符对象
first2 = Word2('ha')
second2 = Word2('HA')
third2 = Word2('eh')

#进行比较
print(first2 == second2)  #True
print(first2 == third2)   #False

'''
一些常用的特殊用法整理如下

比较用
方法名称    使用
__eq__(self, other)    self == other
__ne__(self, other)    self != other
__lt__(self, other)    self < other
__gt__(self, other)    self > other
__le__(self, other)    self <= other
__ge__(self, other)    self >= other
数学用
方法名    使用
__add__(self, other)    self + other
__sub__(self, other)    self - other
__mul__(self, other)    self * other
__floordiv__(self, other)    self // other
__truediv__(self, other)    self / other
__mod__(self, other)    self % other
__pow__(self, other)    self ** other
其他常用
方法名    使用
__str__(self)    str(self)
__repr__(self)    repr(self)
__len__(self)    len(self)
完整清单请看官方文件。 https://docs.python.org/3/reference/datamodel.html#special-method-names
'''
class Word3():
    def __init__(self, text):
        self.text = text
    
    def __str__(self):
        return self.text + 'haha!!'
 
class sqrtt():
    def __init__(self, num):
        self.num = num
    
    def __mul__(self, number):
        return self.num * number.num
    
class minmax():
    def __init__(self, minn, maxx):
        self.minn = minn
        self.maxx = maxx
    
    def __str__(self):
        return 'min:' + str(self.minn) + ',max:'+ str(self.maxx)
    
 
#创建3个单词对象
first3 = Word3('ha')
print(first3)   #print必须为字符串，所以代码自行使用str()转换成字符串
 
XD = sqrtt(4)
XDD = sqrtt(5)
print( XD * XDD )
 
AM = minmax(3, 10)
print(AM)
print('min:' + str(AM.minn) + ',max:'+ str(AM.maxx))

# 6.13 组合
print('===========6.13 组合===========')
'''
如果要新建的类有相似的类可以继承的話就可以采用继承来取得父类的所有，
但若两个类差异太大，或是沒有关系，我们就可以采用组合來合并这些类
例如，鸭子是鸟的一种，所以可以继承鸟的类，
但是嘴巴和尾巴不是鸟的一种，而是鸭子的组成。
'''
class Bill():
    def __init__(self, description):
        self.description = description
        
class Tail():
    def __init__(self, length):
        self.length = length
    
class Duck4():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('这只鸭子有一个', bill.description, '嘴巴，然后有', tail.length, '长的尾巴')
 
bill = Bill('红色的')
tail = Tail('白色，15cm')
 
duck4 = Duck4(bill, tail)
duck4.about()


# 6.14 何时使用类和对象而不是模块
print('===========6.14 何时使用类和对象而不是模块===========')
'''
有一些方法可以帮助你決定是把你的代码封裝到类里还是模块里。
    当你需要许多具有相似行为（方法），但不同状态（特性）的实例时，使用对象是最好的选择。
    类支持继承，但模块不支持。
    如果你想要保证实例的唯一性，使用模块是最好的选择。不管模块在程序中被引用多少次，始终只有一个实例被加载。
    如果你有一系列包含多个值的变量，并且他们能作为参数传入不同的函数，那么最好將它们封裝到类里面。举个例子，你可能会使用以大小和颜色为键的字典代表一张 彩色图片。
        你可以在程序中为每张图片创建不同的字典，并把它们作为参数传递给像规模（）或者变换（）之类的函数。但这么做的话，一旦你想要添加其他的键或者函数会变得非常麻烦。
        为了保证统一性，应该定义一个图片类，把大小和颜色作为特性，把规模（）和变换（）定义为方法。这么一来，关于一张图片的所有数据和可执行的操作都存储在了统一的位置。
    用最简单的方式解決问题。使用字典，列表和元組往往要比使用模块更加简单，简介且快速。而使用类则更为复杂。
'''
'''
命名Tuple(named tuple)
可以用來创造可以用名称访问的Tuple子类
跟Tuple一样，不可被改变，但是可以透过替换來产生新的命名Tuple
'''
from collections import namedtuple #引入函数库
 
Duck5 = namedtuple('Duck5', 'bill tail') #定义为命名Tuple，並且有bill和tail两种名称
duck5 = Duck5('wide orange', 'long')     #赋值
 
print(duck5)
print(duck5.bill)
print(duck5.tail)
 
parts = {'bill': 'wide red', 'tail': 'short'}  #使用dictionary赋值
duck52 = Duck5(**parts)
print(duck52)
 
duck53 = duck52._replace(tail='magnificent', bill='crushing')  #替换內容
print(duck53)


# 6.15 练习
print('===========6.15 练习===========')
# (1) 创建一个名为 Thing 的空类并将它打印出来。接着，创建一个属于该类的对象 example， 同样将它打印出来。看看这两次打印的结果是一样的还是不同的?
print("(1). " )
class Thing():
    def __init__(self):
        print("class name:", self.__class__.__name__)
    
exampleThing = Thing()
print(exampleThing)

# (2) 创建一个新的类 Thing2，将 'abc' 赋值给类特性 letters，打印 letters。
print("(2). " )
class Thing2():
    def __init__(self, text):
        self.letters = text
        print("class name:", self.__class__.__name__)
        print("Thing2.letters:", self.letters)
        
exampleThing2 = Thing2('abc')
print(exampleThing2)

# (3) 再创建一个新的类，叫作 Thing3。这次将 'xyz' 赋值给实例(对象)特性 letters，并试着打印 letters。看看你是不是必须先创建一个对象才可以进行打印操作?
print("(3). " )
class Thing3():
    def __init__(self, text):
        self.letters = text
        print("class name:", self.__class__.__name__)
        print("Thing3.letters:", self.letters)
    
    def set_letters(self, text):
        self.letters = text
        
    def get_letters(self):
        return self.letters
    
    #name = property(get_name, set_name)

exampleThing3 = Thing3('')
exampleThing3.letters = 'xyz'
print(exampleThing3)
print(exampleThing3.letters)

# (4) 创建一个名为 Element 的类，它包含实例特性 name、symbol 和 number。使用 'Hydrogen'、'H' 和 1 实例化一个对象。
print("(4). " )
class Element():
    def __init__(self, text1, text2, text3):
        self.name = text1
        self.symbol = text2
        self.number = text3
        print("class name:", self.__class__.__name__)
        print("attributes are :", self.name, self.symbol, self.number)
    def dump(self):
        print("dump attributes")
        print("\t name = ", self.name)
        print("\t symbol = ", self.symbol)
        print("\t number = ", self.number)
    def __str__(self):
        return "__str__ attributes: name = "+self.name+" symbol = "+self.symbol+" number = "+self.number
    
exampleElement = Element('Hydrogen', 'H', '1')

# (5)创建一个字典，包含这些键值对:'name': 'Hydrogen'、'symbol': 'H'和'number': 1。然后用这个字典实例化 Element 类的对象 hydrogen。
print("(5). " )
examdic = {'name':'Hydrogen', 'symbol':'H', 'number':'1',}
hydrogen = Element(examdic['name'], examdic['symbol'], examdic['number'])

# (6) 为 Element 类定义一个 dump() 方法，用于打印对象的特性(name、symbol 和 number)。使用这个新定义的类创建一个对象 hydrogen 并用 dump() 打印。
print("(6). " )
hydrogen2 = Element('duck', 'D', '5')
hydrogen2.dump()

# (7) 调用 print(hydrogen)，然后修改 Element 的定义，将 dump 方法的名字改为 str。再次创建一个 hydrogen 对象并调用 print(hydrogen)，观察输出结果。
print("(7). " )
hydrogen3 = Element('Monkey', 'M', '3')
print(hydrogen3)

# (8) 修改 Element 使得 name、symbol 和 number 特性都变成私有的。为它们各定义一个 getter属性来返回各自的值。
print("(8). " )
class Element2():
    def __init__(self, text1, text2, text3):
        self.__name = text1
        self.__symbol = text2
        self.__number = text3
        print("class name:", self.__class__.__name__)
        print("attributes are :", self.__name, self.__symbol, self.__number)
    
    @property   
    def name(self):
        return self.__name
    @name.setter
    def name(self, inputname):
        self.__name = inputname
    @property   
    def symbol(self):
        return self.__symbol
    @symbol.setter
    def symbol(self, inputsymbol):
        self.__symbol = inputsymbol
    @property   
    def number(self):
        return self.__number
    @number.setter
    def number(self, inputnumber):
        self.__number = inputnumber    


# (9) 定义三个类 Bear、Rabbit 和 Octothorpe。对每个类都只定义一个方法 eats()，分别返回 'berries'(Bear)、'clover'(Rabbit)和 'campers'(Octothorpe)。
# 为每个类创建一个对象并输出它们各自吃的食物(调用 eats())。
print("(9). " )
class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Octothorpe():
    def eats(self):
        return 'campers'

bb = Bear()
rr = Rabbit()
oo = Octothorpe()
print('Bear eat ', bb.eats())
print('Rabbit eat ', rr.eats())
print('Octothorpe eat ', oo.eats())

# (10) 定义三个类 Laser、Claw 以及 SmartPhone。每个类都仅有一个方法 does()，分别返回'disintegrate'(Laser)、'crush'(Claw) 以及'ring'(SmartPhone)。
#  接着，定义 Robot 类，包含上述三个类的实例(对象)各一个。给 Robot 定义 does() 方法用于输 出它各部分的功能。
print("(10). " )
class Laser():
    def does(self):
        return self.__class__.__name__+' disintegrate'

class Claw():
    def does(self):
        return self.__class__.__name__+' crush'

class SmartPhone():
    def does(self):
        return self.__class__.__name__+' ring'

class Robot():
    def __init__(self, obj1, obj2, obj3):
        self.__laser=obj1
        self.__claw=obj2
        self.__smartphone=obj3
    def does(self):
        print('Robot does: ', self.__laser.does(), ', ', self.__claw.does(), ', ', self.__smartphone.does()) 

rbt = Robot(Laser(),Claw(),SmartPhone())
rbt.does()


