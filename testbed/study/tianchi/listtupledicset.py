'''
Created on 2018年10月10日

@author: banshu
'''

if __name__ == '__main__':
    pass


'''
第2章 Python容器：列表、Tuples、字典与集合
CHAPTER 2 Py Filling: Lists, Tuples, Dictionaries, and Sets
'''
    
# 3.1 列表(list)与Tuples
# 两者差异再与，List可以改变其內容，增減长度 or 替换等等皆可以
# Tuples一旦赋值之后，就不能再修改。
# 以性能和内存使用量来说，Tuples皆较佳


# 3.2 列表(list)类型
#List可以使用 [] 或是 list() 來创建空的，或是直接加入值进去，使用逗号区分即可。內容可以重复出现，且具有順序性。
print("------列表(list)类型------")
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
print(empty_list)
print(weekdays)
print(big_birds)
print(first_names)

#可以使用 list() 来作为转换其他类型到List，或是前面2.3小节提到的字串split()函数
print(list('cat'))
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))
birthday = '1/6/1952'
print((birthday.split('/')))

#提取內容時跟字符串一样使用[ ]， index 从0开始，-1为最后一个， index 数值的范围请务必在总长度内，不然会出现IndexError。
#也可以将其修改替换內容。 提取多个以上也如同字符串中的用法 [start : end : step]，注意这边只会提取到index为end -
XD = ['a', 'b', 'c', 'd']
print(XD[0])
print(XD[1])
print(XD[-1])
print(XD[-2])
XD[0] = 'QQ'
print(XD)
print(XD[0:2])
print(XD[2:-2])
print(XD[::2])

#List里面可以包含不同类型的Object，当然也包括List
#可以使用List的內建函数append()来向后面添加元素
XDObject = ['a', 'b']
XDObject2 = ['e', 'f']
print(XDObject, XDObject2)
 
XDObject.append('QQ~')
print(XDObject)
XDObject.extend(XDObject2)
print(XDObject)
 
XDObject += XDObject2
print(XDObject)
XDObject.append(XDObject2)
print(XDObject)
 
XDObject.insert(2, 'c')
print(XDObject)
XDObject.insert(500, 'ker')
print(XDObject)
 
del XDObject[8]
print(XDObject)
XDObject.remove('e')
print(XD)
 
QQ = XDObject.pop(3)
print(XDObject, QQ)
print(XDObject.index('f'))
print('ker' in XDObject)
print(XDObject.count('f'))

# 前面2.3节提到的string.join()，可以用来组装List成为字串， 书中提到这边的用法看起來有点别扭，如果改成List.join(', ')会更加直觉，
#  但是当初设计的理念就是join的方法是在字符串类型中， 这样后面我想要针对List、Tuples或是字串使用字串做组装，就只要一中方法就好， 
#  不用针对每种类型都去设计一个相同的方法來做使用，如下所示。 string.join() 与 string.split()两个互相对应的用法!!
print(', '.join(['a', 'b', 'c']))
print(', '.join('abc'))
print(', '.join(('a', 'b', 'c')))
print('a, b, c'.split(', '))

# list.sort()为list排序方法，
# sorted()为通用的排序函数 其中的差异在与sort()會直接改变輸入的list，sorted()则会另外回传一个排序好的Object
# len()可以获取list的长度。
# 使用 '=' 设定变量则会是传址，等同于前面說的标签概念，把两张标签贴在同一个物件上(number or srting 除外) 这样当我改变Object后，
# 则Object上所有的标签所指到的值都会跟着改变， 若要改成赋值的话可以使用copy() 、 list.list() 与 list[:] 来达到目的
a = [1, 2, 3]
b = a
a[0] = 4
print(a, b)
c = a.copy()
d = list(a)
e = a[:]
a[0] = 'surprises'
print(a, b, c, d, e)

# 3.3 Tuples类型
print("------Tuples类型------")
# Tuples也是一个List，差別只在不能做修改，一旦给定后，无法再进行增加 刪除 修改等操作，所以可以当作一个常数的List
# 创建为空的时候使用()，一个以上时括号可以省略，但是只有一个时最后一个逗号不可以省略。
tuplesa = ()   #空Tuples
tuplesb = 'tem', #b:(tem,) 括号可以省略，但是一个的時候逗号不能省略
tuplesc = 'tem1', 'tem2', 'tem3'  #('tem1', 'tem2', 'tem3')
tuplesd, tuplese, tuplesf = tuplesc   #d:'tem1', e:'tem2', f:'tem3'
 
print(tuplesa)
print(tuplesb)
print(tuplesc)
print(tuplesd, tuplese, tuplesf)

# 结合以上的用法可以有一个超级方便直觉的用法，任意交换变量间的值。
# (在等号右边的东西会先形成一个Tuples，再分配给前面的变量。)
tuplesaa = '1'
tuplesbb = '2'
tuplescc = '3'
print(tuplesaa, tuplesbb, tuplescc)
tuplesbb, tuplescc, tuplesaa = tuplesaa, tuplesbb, tuplescc
print(tuplesaa, tuplesbb, tuplescc)

# Tuples相对于List一定也有其他好处
# 空间较小
# 不会不小心修改到值
# 可以当作dictionary的key值 (后一小节有说明)
# 命名Tuples，可以做为Object的替代 (第六章会说明)
# 函数的传递是以Tuples形式传递


# 3.4 字典(Dictionaries)类型
print("------字典(Dictionaries)类型------")
# 为一种没有顺序的的容器，其使用的是大括弧{}，里面包含键值与值(key : value)
# 可以使用dict()来转换其他类型至dictionary

# D.update()    合并不同dictionary
# del Object    刪除某项
# in Object    是否存在里面(key)
# *D.keys() *    获得所有key值
# D.values()    获得所有value值
# *D.items() *    获得全部的key: value( Tuples类型 )
# *D.copy() *    复制一个dictionary
# *D.clear() *    清除所有內容
dic = { 'a':'v','b':'w', }  #最后一个逗号可以省略
dic_ = { 'd':'y','c':'x' }  #最后一个逗号可以省略
print("dic,dic_ ",dic, dic_)
 
lol1 = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
lol2 = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
lol3 = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] )
print(dict(lol1), dict(lol2), dict(lol3))
 
tos1 = [ 'ab', 'cd', 'ef' ]
tos2 = ( 'ab', 'cd', 'ef' )
print("dict(tos1)=",dict(tos1), "dict(tos2)=",dict(tos2))
 
print('============分割线============')
print(dic_['c'])
dic_['c'] = 'z'
print(dic_['c'])

print(dic)
dic.update(dic_)
print(dic)

print('============分割线============')
tos3 = ( 'cd', )
print("dict(tos3)=",dict(tos3))
dic.update(dict(tos3))
print(dic)

del dic['d']
print(dic)
 
print('a' in dic)
 
print('============分割线============')
print(dic.keys())         # dict_keys(['a', 'b', 'c'])
print(dic.values())       # ['v', 'w', 'x']
print(list(dic.items()))  # [('a', 'v'), ('b', 'w'), ('c', 'x')]
 
print('============分割线============')
dic_new = dic
dic_new['a'] = 'n'
print(dic, dic_new)
 
dic_cp = dic.copy()
dic_cp['a'] = 'm'
print(dic, dic_cp)
 
dic.clear() 
print(dic)

# 3.5 集合(set)类型
# 集合就好比沒有value的dictionary，一样没有顺序，使用大括弧{}。
# 空白集合为set()，也合相当于False。
# 使用set()可以转换其他类型至集合，dictionary转换至set只会保留key值。
# in也可以检查特定元素是否存在其中。
empty_set = set()
even_numbers = {0, 2, 4, 6, 8}
print(empty_set, even_numbers)
print(set( 'letters' ))
print(set( ['D', 'A', 'P', 'M'] ))
print(set( ('U', 'Echoes', 'Atom') ))
print(set( {'apple': 'red', 'orange': 'orange'} ))
print(4 in even_numbers)


# 3.6 比较类型差別
# 比较不同容器之间的使用差别，使用方括号([])创建列表，使用逗号创建元组，使用花括号({})创建字典。
marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'} 
print(marx_list[2])
print(marx_tuple[2])
print(marx_dict['Harpo'])


# 3.7 建立大型结构
# 容器中可以包含不同类型的元素，也可以包含其他的容器物件。
dict_of_lists = {'Stooges': ['Moe', 'Curly', 'Larry'],
                'Marxes': ['Groucho', 'Chico', 'Harpo'],
                'Pythons': ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']}
print(dict_of_lists)
print(dict_of_lists['Marxes'])
print(dict_of_lists['Marxes'][1])


# 3.8 练习
# (1) 创建一个叫作 years_list 的列表，存储从你出生的那一年到五岁那一年的年份。例 如，如果你是 1980 年出生的，
# 那么你的列表应该是 years_list = [1980, 1981, 1982, 1983, 1984, 1985]。 如果你现在还没到五岁却在阅读本书，那我真的没有什么可教你的了。
years_list = [1981, 1982, 1983, 1984, 1985, 1986]
print("(1), ",years_list)


# (2) 在 years_list 中，哪一年是你三岁生日那年?别忘了，你出生的第一年算 0 岁。
print("(2), ",'三岁=',years_list[3])

# (3) 在 years_list 中，哪一年你的年纪最大?
numofmax = len(years_list)-1
print(numofmax)
print("(3), ",'最大=',years_list[numofmax])


# (4)创建一个名为 things 的列表，包含以下三个元素:"mozzarella"、"cinderella" 和"salmonella"。
#3个单词的意思分别是：意大利干酪、灰姑娘、沙门氏菌
things_list = ["mozzarella","cinderella" ,"salmonella"]
print("(4), ",things_list)

# (5) 将 things 中代表人名的字符串变成首字母大写形式，并打印整个列表。看看列表中的元素改变了吗?
#capitalize()，upper();
things_list[1] = things_list[1].capitalize()
print("(5), ",things_list)

#将list中的单词首字母变成大写
# current = 0
# while current < len(things_list):
#     things_list[current] = things_list[current].capitalize()
#     current += 1
# print(things_list)

# (6) 将 things 中代表奶酪的元素全部改成大写，并打印整个列表。
things_list[0] = things_list[0].upper()
print("(6), ",things_list)
#将list中的所有字母变成大写
# current2 = 0
# while current2 < len(things_list):
#     things_list[current2] = things_list[current2].upper()
#     current2 += 1
# print(things_list)

# (7) 将代表疾病的元素从 things 中删除，收好你得到的诺贝尔奖，并打印列表。
things_list.remove("salmonella")
print("(7), ",things_list)

# (8) 创建一个名为 surprise 的列表，包含以下三个元素:"Groucho"、"Chico" 和 "Harpo"。
surprise = []
surprise.append("Groucho")
surprise.append("Chico" )
surprise.append("Harpo")
print("(8), ",surprise)


# (9) 将 surprise 列表的最后一个元素变成小写，翻转过来，再将首字母变成大写。
surprise[2] = surprise[2].lower()
surprise.reverse()
print("(9), ",surprise)


# (10) 创建一个名为 e2f 的英法字典并打印出来。这里提供一些单词对:dog 是 chien，cat是 chat，walrus 是 morse。
e2f = {"dog":"chien","cat":"chat","walrus":"morse"}
print("(10), ",e2f)

# (11) 使用你的仅包含三个词的字典 e2f 查询并打印出 walrus 对应的的法语词。
print("(11), ",e2f.get('walrus'))
print("(11), ",e2f['walrus'])

# (12) 利用 e2f 创建一个名为 f2e 的法英字典。注意要使用 items 方法。
f2e = {e2f.get('dog'):'dog', e2f.get('cat'):'cat', e2f.get('walrus'):'walrus'}
#怎么使用items？？？？？
print("(12), ",f2e)

# (13) 使用 f2e，查询并打印法语词 chien 对应的英文词。
print("(13), ",f2e['chien'])

# (14) 创建并打印由 e2f 的键组成的英语单词集合。
print("(14), ",set( f2e.values() ) )

# (15) 建立一个名为 life 的多级字典。将下面这些字符串作为顶级键:'animals'、'plants'以及 'others'。
# 令 'animals' 键指向另一个字典，这个字典包含键 'cats'、'octopi' 以及 'emus'。令 'cat' 键指向一个字符串列表，这个列表包括 'Henri'、'Grumpy' 和 'Lucy'。
# 让其余的键都指向空字典。
# : ['Henri', 'Grumpy' , 'Lucy' ]
life = {'animals': {'cats': {'Henri', 'Grumpy', 'Lucy' }, 
                    'octopi': {}, 
                    'emus': {} }, 
        'plants': {'earth', 'mars' , 'venas'} , 
        'others': {}}

octopi_dic = {'prof', 'dr' }
life['animals']['octopi' ] = octopi_dic

print("(15), ",life)

# (16) 打印 life 的顶级键。
print("(16), ", list(life.keys()) )

# (17) 打印 life['animals'] 的全部键。
print("(17), ", life['animals'] )

# (18) 打印 life['animals']['cats'] 的值。
print("(18), ", life['animals']['cats'] )

   
    