#-*_coding:utf8-*-
import requests
import os, sys
import time
import random
'''
处理华为云社区的一些资源，最好能够根据关键词下载对应文章、视频，支持有限深度
https://bbs.huaweicloud.com/forum/thread-10102-1-1.html
批量处理在线课程的内容，自动提取页面中的内容、文稿（pdf）和视频文件（ts）

 '''

readsize = 1024

def getAPM():
    '''
    《应用性能管理：速解分布式架构问题》课程
    https://education.huaweicloud.com:8443/courses/course-v1:HuaweiX+CBUCNXP006+2018.5/courseware
    :return:
    '''
    result ={}
    result['APM快速入门'] = 'https://13.cdn-vod.huaweicloud.com/asset/db31b71ecd4c9e7ffe27d7b7ede69467/play_video/16939fe34ab72f8151742f379310a5ce_1_1920X1080_3000_0_'
    result['APM管理操作-事务'] = 'https://13.cdn-vod.huaweicloud.com/asset/0050b2b8f7dfc47387d934faa7132637/play_video/%E4%B8%AD%E6%96%87-PaaS-APM%E7%AE%A1%E7%90%86%E6%93%8D%E4%BD%9C%E4%B9%8B%E4%BA%8B%E5%8A%A1-%E8%A7%86%E9%A2%91-V01-20180409_1_854X480_600_0_'
    result['APM管理操作-拓扑'] = 'https://13.cdn-vod.huaweicloud.com/asset/bf708df40e28990e72273279e8b95b24/play_video/%E4%B8%AD%E6%96%87-PaaS-APM%E7%AE%A1%E7%90%86%E6%93%8D%E4%BD%9C%E4%B9%8B%E6%8B%93%E6%89%91-%E8%A7%86%E9%A2%91-V01-20180409_1_854X480_600_0_'
    result['APM管理操作-调用链'] = 'https://13.cdn-vod.huaweicloud.com/asset/38ad0f39089d0fbf1d6101aab603e621/play_video/%E4%B8%AD%E6%96%87-PaaS-APM%E7%AE%A1%E7%90%86%E6%93%8D%E4%BD%9C%E4%B9%8B%E8%B0%83%E7%94%A8%E9%93%BE-%E8%A7%86%E9%A2%91-V01-20180409_1_854X480_600_0_'
    result['企业应用云化DevOps-云场景下运维挑战'] = 'https://13.cdn-vod.huaweicloud.com/asset/4a31277444f0950f0690d51edf69b8cd/play_video/%E4%B8%AD%E6%96%87-APM-%E4%BA%91%E5%9C%BA%E6%99%AF%E4%B8%8B%E8%BF%90%E7%BB%B4%E6%8C%91%E6%88%98-%E8%A7%86%E9%A2%91-V01-20180422_1_854X480_600_0_'
    result['企业应用云化DevOps-华为APM解决方案'] = 'https://13.cdn-vod.huaweicloud.com/asset/2737696665e34773d5c02cf86150e565/play_video/%E4%B8%AD%E6%96%87-APM-%E5%8D%8E%E4%B8%BAAPM%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88-%E8%A7%86%E9%A2%91-V01-20180422_1_854X480_600_0_'
    result['微服务运维能力实战'] = 'https://13.cdn-vod.huaweicloud.com/asset/f32599ae569fb4e17f20c24ea2a28cbf/play_video/a987229b8a4d15346a20d7c27b6052fb_1_1920X1080_3000_0_'
    return result

def getIOT():
    '''
    《物联网技术与应用》课程
    https://education.huaweicloud.com:8443/courses/course-v1:HuaweiX+CBUCNXT001+Self-paced/courseware/27e12beb190541618c0b399f871369d0/a0c1f6489ad9426cb1be49a45b5fdbb5/
    :return:
    '''
    result = {}
    return result

def join(fromdir, tofile):
    '''
    将指定的formdir下所有文件合并成tofile文件
    :param fromdir:
    :param tofile:
    :return:
    '''
    output=open(tofile,"wb")
    #out = open(tofile, "wb")
    parts=os.listdir(fromdir)
    # 倒着数第三位'.'为分界线，按照‘.’左边的数字从小到大排序
    parts.sort(key=lambda x: int(x[:-3]))
    #parts.sort()
    for filename in parts: 
        filepath=os.path.join(fromdir,filename)
        fileobj=open(filepath,"rb")
        while True: 
            filebytes=fileobj.read(readsize)
            if not filebytes: 
                break
            output.write(filebytes)
        fileobj.close()
    output.close()
    print(u'生成文件：', tofile)

def delfile(path):
    '''
    删除指定path下的所有文件和子文件
    :param path:
    :return:
    '''
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            delfile(c_path)
        else:
            os.remove(c_path)
            print(u'删除临时文件：', c_path)

def download(url, tofolder, tofile):
    dict_of_lists = {}
    # 创建0.ts - 500.ts文件名
    current = 0
    while current <= 999:
        name=str(current)+'.ts'
        dict_of_lists[name] = url+name
        current += 1

    # 创建00000.ts - 99999.ts文件名
    # while current <= 600:
    #     name=str(current).zfill(5)+'.ts'
    #     dict_of_lists[name] = url+name
    #     current += 1

    # 开始处理列表页面的数据，每个片段保存成一个文件
    for link in dict_of_lists.keys():
        print(u'正在处理页面：', link, ' ', dict_of_lists.get(link))
        r = requests.get(dict_of_lists.get(link))
        if r.status_code is 200:
            with open(folder + link, "wb") as source:
                source.write(r.content)
                time.sleep(random.random())
        else:
            print('error:', r.status_code)
            break

    # 输出，将所有片段按照从小到大顺序合并成一个文件
    join(tofolder, tofile)

    # 删除临时文件夹下的内容
    delfile(tofolder)
    return

if __name__ == '__main__':
   
    # 初始化
    folder = './folder/'
    url_lists = getAPM()

    # 检测临时目录是否存在，不存在就删除
    if not os.path.exists(folder):
        print(u'创建临时目录', folder)
        os.makedirs(folder)

    # 开始处理每个下载页面
    for k, v in url_lists.items():
        print(u'正在处理页面：', k, ' ', v)
        download(v,folder,k+'.ts')

    print(u'处理完成。')



