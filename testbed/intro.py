# -*- coding:utf-8 -*-

# 导入NumPy函数库，一般都是用这样的形式(包括别名np，几乎是约定俗成的)
import numpy as np
import matplotlib as mpl
import time
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import math

if __name__ == "__main__":
    # # 开场白：
    # numpy是非常好用的数据包，如：可以这样得到这个二维数组
    # [[ 0  1  2  3  4  5]
    #  [10 11 12 13 14 15]
    #  [20 21 22 23 24 25]
    #  [30 31 32 33 34 35]
    #  [40 41 42 43 44 45]
    #  [50 51 52 53 54 55]]
    a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
    print(a)

    # 正式开始  -:)
    # 标准Python的列表(list)中，元素本质是对象。
    # 如：L = [1, 2, 3]，需要3个指针和三个整数对象，对于数值运算比较浪费内存和CPU。
    # 因此，Numpy提供了ndarray(N-dimensional array object)对象：存储单一数据类型的多维数组。

    # # 1.使用array创建
    # # 通过array函数传递list对象
    # L = [1, 2, 3, 4, 5, 6]
    # print("L = ", L)
    # a = np.array(L)
    # print("a = ", a)
    # print(type(a), type(L))
    # # 若传递的是多层嵌套的list，将创建多维数组
    # b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    # print(b)
    # #
    # # # # # # # 数组大小可以通过其shape属性获得
    # print(a.shape)
    # print(b.shape)
    #
    # # # # 也可以强制修改shape
    # b.shape = (4, 3)
    # print(b)
    # # # 注：从(3,4)改为(4,3)并不是对数组进行转置，而只是改变每个轴的大小，数组元素在内存中的位置并没有改变
    #
    # # # # 当某个轴为-1时，将根据数组元素的个数自动计算此轴的长度
    # b.shape = 2, -1
    # print(b)
    # print(b.shape)
    # #
    # b.shape = 3, 4
    # print(b)
    # # # # # 使用reshape方法，可以创建改变了尺寸的新数组，原数组的shape保持不变
    # c = b.reshape((4, -1))
    # print("b = \n", b)
    # print('c = \n', c)
    # #
    # # # # 数组b和c共享内存，修改任意一个将影响另外一个
    # b[0][1] = 20
    # print("b = \n", b)
    # print("c = \n", c)
    # #
    # # # # 数组的元素类型可以通过dtype属性获得
    # print(a.dtype)
    # print(b.dtype)
    # # # # #
    # # # # # 可以通过dtype参数在创建时指定元素类型
    # d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=np.float)
    # f = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=np.complex)
    # print(d)
    # print(f)
    # #
    # # # 如果更改元素类型，可以使用astype安全的转换
    # f = d.astype(np.int)
    # print(f)
    # # # #
    # # # # 但不要强制仅修改元素类型，如下面这句，将会以int来解释单精度float类型
    # d.dtype = np.int
    # print(d)

    # 2.使用函数创建
    # 如果生成一定规则的数据，可以使用NumPy提供的专门函数
    # arange函数类似于python的range函数：指定起始值、终止值和步长来创建数组
    # 和Python的range类似，arange同样不包括终值；但arange可以生成浮点类型，而range只能是整数类型
    # np.set_printoptions(linewidth=100, suppress=True)
    # a = np.arange(1, 10, 0.5)
    # print(a)
    # # #
    # # # # # linspace函数通过指定起始值、终止值和元素个数来创建数组，缺省包括终止值
    # b = np.linspace(1, 10, 10)
    # print('b = ', b)
    # # #
    # # # # 可以通过endpoint关键字指定是否包括终值
    # c = np.linspace(1, 10, 10, endpoint=False)
    # print('c = ', c)
    # # #
    # # # # # 和linspace类似，logspace可以创建等比数列
    # # # # 下面函数创建起始值为10^1，终止值为10^2，有10个数的等比数列
    # d = np.logspace(1, 4, 4, endpoint=True, base=2)
    # print(d)
    # # # # # # #
    # # # # # # # 下面创建起始值为2^0，终止值为2^10(包括)，有10个数的等比数列
    # f = np.logspace(0, 10, 11, endpoint=True, base=2)
    # print(f)
    # #
    # # # # # 使用 frombuffer, fromstring, fromfile等函数可以从字节序列创建数组
    # s = 'abcdzzzz'
    # g = np.fromstring(s, dtype=np.int8)
    # print(g)
    # #
    # # 3.存取
    # # 3.1常规办法：数组元素的存取方法和Python的标准方法相同
    # a = np.arange(10)
    # print(a)
    # # # # 获取某个元素
    # print(a[3])
    # # # # # # 切片[3,6)，左闭右开
    # print(a[3:6])
    # # # # 省略开始下标，表示从0开始
    # print(a[:5])
    # # # # 下标为负表示从后向前数
    # print(a[-3:])
    # # # # 步长为2
    # print(a[1:9:2])
    # # # # # # # # 步长为-1，即翻转
    # print(a[::-1])
    # # # # 切片数据是原数组的一个视图，与原数组共享内容空间，可以直接修改元素值
    # a[1:4] *= 10
    # print(a)
    # # # # 因此，在实践中，切实注意原始数据是否被破坏，如：
    # b = a[2:5]
    # b[0] = 200
    # print(a)

    # 3.2 整数/布尔数组存取
    # 3.2.1
    # 根据整数数组存取：当使用整数序列对数组元素进行存取时，
    # 将使用整数序列中的每个元素作为下标，整数序列可以是列表(list)或者数组(ndarray)。
    # 使用整数序列作为下标获得的数组不和原始数组共享数据空间。
    # a = np.logspace(0, 9, 10, base=2)
    # print(a)
    # i = np.arange(0, 10, 2)
    # print(i)
    # # # # # 利用i取a中的元素
    # b = a[i]
    # print(b)
    # # # # # b的元素更改，a中元素不受影响
    # b[2] = 1.6
    # print(b)
    # print(a)

    # # 3.2.2
    # 使用布尔数组i作为下标存取数组a中的元素：返回数组a中所有在数组b中对应下标为True的元素
    # 生成10个满足[0,1)中均匀分布的随机数
    # a = np.random.rand(10)
    # print(a)
    # # # 大于0.5的元素索引
    # print(a > 0.5)
    # # # # 大于0.5的元素
    # b = a[a > 0.5]
    # print(b)
    # # # # 将原数组中大于0.5的元素截取成0.5
    # a[a > 0.5] = 0.5
    # print(a)
    # # # # # # b不受影响
    # print(b)

    # 3.3 二维数组的切片
    # [[ 0  1  2  3  4  5]
    #  [10 11 12 13 14 15]
    #  [20 21 22 23 24 25]
    #  [30 31 32 33 34 35]
    #  [40 41 42 43 44 45]
    #  [50 51 52 53 54 55]]
    # a = np.arange(0, 60, 10)    # 行向量
    # print('a = ', a)
    # b = a.reshape((-1, 1))      # 转换成列向量
    # print(b)
    # c = np.arange(6)
    # print(c)
    # f = b + c   # 行 + 列
    # print(f)
    # # # 合并上述代码：
    # a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
    # print(a)
    # # # # # 二维数组的切片
    # print(a[[0, 1, 2], [2, 3, 4]])
    # print(a[4, [2, 3, 4]])
    # print(a[4:, [2, 3, 4]])
    # i = np.array([True, False, True, False, False, True])
    # print(a[i])
    # print(a[i, 3])

    # # 4.1 numpy与Python数学库的时间比较
    # for j in np.logspace(0, 7, 8):
    #     x = np.linspace(0, 10, j)
    #     start = time.clock()
    #     y = np.sin(x)
    #     t1 = time.clock() - start
    #
    #     x = x.tolist()
    #     start = time.clock()
    #     for i, t in enumerate(x):
    #         x[i] = math.sin(t)
    #     t2 = time.clock() - start
    #     print(j, ": ", t1, t2, t2/t1)

    # # 4.2 元素去重
    # # 4.2.1直接使用库函数
    # a = np.array((1, 3, 2, 4, 5, 5, 7, 3, 2, 2, 8, 8))
    # print('原始数组：', a)
    # # # # 使用库函数unique
    # b = np.unique(a)
    # print('去重后：', b)
    # # 4.2.2 二维数组的去重，结果会是预期的么？
    # c = np.array(((1, 2), (3, 4), (5, 6), (1, 3), (3, 4), (7, 6)))
    # print('二维数组：\n', c)
    # print('去重后：', np.unique(c))
    # # # # 4.2.3 方案1：转换为虚数
    # x = c[:, 0] + c[:, 1] * 1j
    # print('转换成虚数：', x)
    # print('虚数去重后：', np.unique(x))
    # print(np.unique(x, return_index=True))   # 思考return_index的意义
    # idx = np.unique(x, return_index=True)[1]
    # print('二维数组去重：\n', c[idx])
    # # # # 4.2.3 方案2：利用set
    # print('去重方案2：\n', np.array(list(set([tuple(t) for t in c]))))

    # # 4.3 stack and axis
    # a = np.arange(1, 7).reshape((2, 3))
    # b = np.arange(11, 17).reshape((2, 3))
    # c = np.arange(21, 27).reshape((2, 3))
    # d = np.arange(31, 37).reshape((2, 3))
    # print('a = \n', a)
    # print('b = \n', b)
    # print('c = \n', c)
    # print('d = \n', d)
    # s = np.stack((a, b, c, d), axis=0)
    # print('axis = 0 ', s.shape, '\n', s)
    # s = np.stack((a, b, c, d), axis=1)
    # print('axis = 1 ', s.shape, '\n', s)
    # s = np.stack((a, b, c, d), axis=2)
    # print('axis = 2 ', s.shape, '\n', s)

    # a = np.arange(1, 10).reshape(3,3)
    # print(a)
    # b = a + 10
    # print(b)
    # print(np.dot(a, b))
    # print(a * b)

    # a = np.arange(1, 10)
    # print(a)
    # b = np.arange(20, 25)
    # print(b)
    # print(np.concatenate((a, b)))

    # # 5.绘图
    # mpl.rcParams['font.sans-serif'] = [u'SimHei']  #FangSong/黑体 FangSong/KaiTi
    # mpl.rcParams['axes.unicode_minus'] = False
    # # 5.1 绘图基础
    # plt.title('第一个示例')
    # data = np.arange(100, 201)  # 生成一个[100, 200]之间的整数数组
    # plt.plot(data)  # 绘图，绘制出来的值对应了图中的纵坐标（y轴）
    #             # 而matplotlib本身为我们设置了图形的横坐标（x轴）：[0,100]
    #             # 因为我们刚好有100个数值
    # plt.show()  # 图形显示

    # # 5.2 绘制多个子图
    # # 有些情况下，我们是希望在同一个窗口显示多个图形。
    # # 此时就这可以用多个subplot。
    # plt.title('子图示例')
    # data = np.arange(100, 201)
    # plt.subplot(221)    # 2行1列subplot中的第1个subplot
    # plt.plot(data)
    #
    # data2 = np.arange(200, 301)
    # plt.subplot(224)    #2行1列subplot中的第2个subplot
    # plt.plot(data2)
    #
    # plt.show()

    # # 5.3 线形图（折线图）
    # plt.title('折线图')
    # plt.plot([1, 2, 3], [3, 6, 9], '-r')    #详见matplotlib.pyplot.plot的API
    # plt.plot([1, 2, 3], [2, 4, 9], ':g')
    #
    # plt.show()

    # # 5.4 散点图，参考matplotlib.pyplot.scatter的API
    # plt.title('随机散点图')
    # N = 20
    #
    # plt.scatter(np.random.rand(N) * 100,
    #     np.random.rand(N) * 100,
    #     c = 'r', s = 100, alpha = 0.5)
    #
    # plt.scatter(np.random.rand(N) * 100,
    #     np.random.rand(N) * 100,
    #     c = 'g', s = 200, alpha = 0.5)
    #
    # plt.scatter(np.random.rand(N) * 100,
    #     np.random.rand(N) * 100,
    #     c = 'b', s = 300, alpha = 0.5)
    #
    # plt.show()

    # # 5.5 饼图，参考matplotlib.pyplot.pie的API
    # plt.title('饼图示例')
    # labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    # data = np.random.rand(7) * 100
    # plt.pie(data, labels=labels, autopct='%1.1f%%')
    # plt.axis('equal')   # 保证饼状图是正圆,否则会有一点角度偏斜
    # plt.legend(loc=3)    # 绘制图例
    #
    # plt.show()

    # # 5.6 条形图（柱状图），参考matplotlib.pyplot.bar的API
    # N = 7
    # x = np.arange(N)
    # data = np.random.randint(low=0, high=100, size=N)
    # colors = np.random.rand(N * 3).reshape(N, -1)
    # print(colors)
    # labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    # plt.title("本周平均销量")
    # plt.bar(x, data, alpha=0.8, color=colors, tick_label=labels)
    # plt.show()

    # # 5.7 直方图，参考matplotlib.pyplot.hist的API
    # # hist函数用来绘制直方图。直方图看起来是条形图有些类似。
    # # 但它们的含义是不一样的，直方图描述了数据中某个范围内数据出现的频度。
    # data = [np.random.randint(0, n, n) for n in [3000, 4000, 5000]]
    # print(data)
    # # # 生成了包含了三个数组的数组，这其中：
    # # # 第一个数组包含了3000个随机数，这些随机数的范围是 [0, 3000)
    # # # 第二个数组包含了4000个随机数，这些随机数的范围是 [0, 4000)
    # # #第三个数组包含了5000个随机数，这些随机数的范围是 [0, 5000)
    #
    # labels = ['3K', '4K', '5K']
    # bins = [0, 100, 500, 1000, 2000, 3000, 4000, 5000]
    # # # bins数组用来指定我们显示的直方图的边界，
    # # # 即：[0, 100) 会有一个数据点，[100, 500)会有一个数据点，
    # # # 以此类推。所以最终结果一共会显示7个数据点。
    # plt.hist(data, bins=bins, label=labels)
    # plt.legend()
    # # # 在这幅图中，可以看到，三组数据在3000以下都有数据，
    # # # 并且频度是差不多的。但蓝色条只有3000以下的数据，
    # # # 橙色条只有4000以下的数据。这与我们的随机数组数据刚好吻合。
    # plt.show()

    # # 5.8 绘制正态分布概率密度函数
    # mu = 0
    # sigma = 5
    # x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 51)
    # y = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
    # print(x.shape)
    # print('x = \n', x)
    # print(y.shape)
    # print('y = \n', y)
    # plt.figure(facecolor='w')
    # # plt.plot(x, y, 'ro-', linewidth=2)
    # plt.plot(x, y, 'r-', x, y, 'go', linewidth=2, markersize=8)
    # plt.xlabel('X', fontsize=15)
    # plt.ylabel('Y', fontsize=15)
    # plt.title('高斯分布函数', fontsize=18)    #
    # plt.grid(True)
    # plt.show()

    # # 5.9 多种图组合
    # x = np.arange(0, 10, 0.1)
    # y = np.sin(x)
    # plt.bar(x, y, width=0.04, linewidth=0.2) #条形图
    # plt.plot(x, y, 'r--', linewidth=2) #折线图
    # plt.title('Sin曲线')
    # plt.xticks(rotation=-60)
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.grid()
    # plt.show()

    # # 6. 绘制三维图像，参考，自学
    # x, y = np.mgrid[-3:3:7j, -3:3:7j]
    # print(x)
    # print(y)
    # u = np.linspace(-3, 3, 101)
    # x, y = np.meshgrid(u, u)
    # print(x)
    # print(y)
    # # z = x*y*np.exp(-(x**2 + y**2)/2) / math.sqrt(2*math.pi)
    # z = x*y*np.exp(-(x**2 + y**2)/2) / math.sqrt(2*math.pi)
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap=cm.coolwarm, linewidth=0.1)  #
    # # ax.plot_surface(x, y, z, rstride=3, cstride=3, cmap=cm.gist_heat, linewidth=0.5)
    # plt.show()
