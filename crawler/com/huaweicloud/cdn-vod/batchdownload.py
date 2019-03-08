#-*_coding:utf8-*-
import requests
import os, sys
import time
import random

readsize = 1024

def getmls():
    '''
    《7天晋级机器学习》课程
    https://education.huaweicloud.com:8443/courses/course-v1:HuaweiX+CBUCNXE026+Self-paced/about
    :return:
    '''
    result ={}
    result['模型评估'] = 'https://13.cdn-vod.huaweicloud.com/asset/54a9a8824395b738959af87ab09096c1/play_video/35496d8c036b9d5514ae2243a5db2b18_1_1920X1080_3000_0_'
    result['机器学习助力客户分群（上）'] = 'https://13.cdn-vod.huaweicloud.com/asset/3cb5973fe4ec0e7f24dfa5f5f734dcb8/play_video/6694ebc4fdd642b83d5ed5a5ce3490f5_1_1280X720_1000_0_'
    result['机器学习助力客户分群（下）'] = 'https://13.cdn-vod.huaweicloud.com/asset/49ff970daba8b44883655836fdee7b63/play_video/921485b7b2c7381ed670347996a3c724_1_1280X688_500_0_'
    result['机器学习助力商品质量分类（上）'] = 'https://13.cdn-vod.huaweicloud.com/asset/11d07a7d98d37e7f621f0c0597b48cc5/play_video/156f7666a3143eacec32e7109ae62f94_1_1280X720_1000_0_'
    result['机器学习助力商品质量分类（下）'] = 'https://13.cdn-vod.huaweicloud.com/asset/7d83b1d81fb21a46586a54e4b9ff4c40/play_video/6069bb0f65488f4dc35a974888287413_1_1280X720_1000_0_'
    result['机器学习助力预测性维护（上）'] = 'https://13.cdn-vod.huaweicloud.com/asset/3df9a4b880e1989331c84cacd5419500/play_video/101a7050a9958bac4d97e2fe862cd0b0_1_1280X720_1000_0_'
    result['机器学习助力预测性维护（下）'] = 'https://13.cdn-vod.huaweicloud.com/asset/27237084abb1fc5dec3ce3e6ce11ec4d/play_video/f83150e577d76c21b87e88c8f0c225b4_1_1920X1080_3000_0_'
    return result

def getMicroServiceOnCloud():
    '''
    《微服务上云实践》课程
    https://education.huaweicloud.com:8443/courses/course-v1:HuaweiX+CBUCNXV007+Self-paced/courseware/
    :return:
    '''
    result ={}
    result['微服务架构的兴起'] = 'https://13.cdn-vod.huaweicloud.com/asset/d874191af371399234ba1be154c77246/play_video/a15b3e93a69097f4b0db734c651ce773_1_1920X1080_3000_0_'
    result['微服务解决方案课程学习'] = 'https://13.cdn-vod.huaweicloud.com/asset/ca72a0d4b694c0bec051aa5403d7d2e7/play_video/c60c4b943dec8bad9f5c75d8c47f5fee_1_1280X720_0_0_'
    result['微服务解决方案实践作业'] = 'https://13.cdn-vod.huaweicloud.com/asset/5c445da3a7436f65260eba4e092cac76/play_video/9158f120c328a1892be5e3dae6a5a2ef_1_1280X720_0_0_'
    result['企业转型微服务详解'] = 'https://13.cdn-vod.huaweicloud.com/asset/865a9726d5a9f20bbe56bc68631561f6/play_video/e818b39fa642354ce096462d4111ff52_1_1920X1080_3000_0_'
    result['Springboot实践作业'] = 'https://13.cdn-vod.huaweicloud.com/asset/b51305b90ec35c2fe3225ffe03c58f4e/play_video/0a7c3bc391ca574dabab647e070f6505_1_1280X720_0_0_'
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
                # time.sleep(random.random())
        else:
            print('error:', r.status_code)
            break

    # 输出，将所有片段按照从小到大顺序合并成一个文件
    join(tofolder, tofile)

    # 删除临时文件夹下的内容
    delfile(tofolder)
    return

'''
给定批量的链接地址，给定文件名，程序批量下载链接指定的ts流，然后另存为指定的文件名
针对每个链接地址，需要默认
 https://13.cdn-vod.huaweicloud.com/asset/7d8a2dd966906ffdd8f573f668057e4e/play_video/66c3c58382aa468c3c93d8346d24896f_1_1920X1080_0_0_{k}.ts
 {k} = 0 - 999
 到999的时候还没结束，继续加数据下载
 '''

if __name__ == '__main__':
   
    # 初始化
    folder = './folder/'
    url_lists = getMicroServiceOnCloud()

    # 检测临时目录是否存在，不存在就删除
    if not os.path.exists(folder):
        print(u'创建临时目录', folder)
        os.makedirs(folder)

    # 开始处理每个下载页面
    for k, v in url_lists.items():
        print(u'正在处理页面：', k, ' ', v)
        download(v,folder,k+'.ts')

    print(u'处理完成。')



