#-*_coding:utf8-*-
import requests
import os, sys
import time
import random

readsize = 1024

#将指定的formdir下所有文件合并成tofile文件
def join(fromdir, tofile):
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

'''
获取下面地址中的视频子文件，都是ts文件
 7天入门机器学习
 第一天，机器学习概述
 https://13.cdn-vod.huaweicloud.com/asset/7d8a2dd966906ffdd8f573f668057e4e/play_video/66c3c58382aa468c3c93d8346d24896f_1_1920X1080_0_0_{k}.ts
 {k} = 0 - 111
 第一天，机器学习服务介绍
 https://13.cdn-vod.huaweicloud.com/asset/14937c9cb6102f5de89dd8ba6a40ab60/play_video/4a4cb66bbaaf93e9466bda9ffb5da8e3_1_1920X1080_0_0_{k}.ts
 {k} = 0 - 45
 第一天，机器学习服务基本操作
 https://13.cdn-vod.huaweicloud.com/asset/e57284d65a63972e664818fc8631820c/play_video/393e9c84e77417d71d95dfff6fedff48_1_1920X1078_0_0_{k}.ts
 {k} = 0 - 54
 第二天，机器学习中的数据处理
 https://13.cdn-vod.huaweicloud.com/asset/439c55c79e8bab3c4fbfdacd1e057963/play_video/5d20b10818227fc6ae3309d5b8402df3_1_720X480_600_0_{k}.ts
 {k} = 0 - 204
 第三天，机器学习中的分类问题上
 https://13.cdn-vod.huaweicloud.com/asset/ca4a51e7516dbae5d31309f46420853e/play_video/51c9ed149ee3a3666a36ed5b2bd4a980_1_854X480_600_0_{k}.ts
 {k} = 0 - 171
 第四天，机器学习中的分类问题下
 https://13.cdn-vod.huaweicloud.com/asset/adb219c91ca6a59a4da2221ef3f6ed9e/play_video/199f46367c0f4f95339c586a9f5b438b_1_854X480_600_0_{k}.ts
 {k} = 0 - 206
 第五天，机器学习中的回归问题上
 https://13.cdn-vod.huaweicloud.com/asset/7df34dc82b0825b9f8b883d9d642f971/play_video/3c7037eea0ded7d25714756930811ac5_1_1920X1078_0_0_{k}.ts
 {k} = 0 - 206
 第六天，机器学习中的回归问题下
 https://13.cdn-vod.huaweicloud.com/asset/441940dc2771100d4b91a0a555a3991e/play_video/dcf3bcc5ddbc26b44de6cf52e401150c_1_1920X1078_0_0_{k}.ts
 {k} = 0 - 107
 第七天，
 
 云享V课堂
 第一讲-TensorFlow Estimator实战分享-云视界live 12.05 周三 20:00-21:00
 http://vod.mudu.tv/watch/2018-12-05/4axrf4/{k}.ts
 {k} = 48 - 142
 第二讲-实战派带你上车，0门槛体验AI超能力-12.19 19:00-20:00
 http://cdn12.mudu.tv/uploads/85181/640_480/9ca578485113d326f5d3dc85bc4f8bd6-{k}.ts
 {k} = 00001 - 00530
 第三讲-刷脸时代已经到来，快速构建专属人脸库-2018.12.27 19:00-20:00
 http://cdn12.mudu.tv/uploads/85181/640_480/ffcb254930d584453651390db32810ba-{k}.ts
 {k} = 00001 - 00343
 '''    
if __name__ == '__main__':
   
    # 初始化
    url = ''
    folder = './folder/'
    dict_of_lists = {}
    
    # 创建0.ts - 500.ts文件名
    current = 0
    while current <= 10000:
        name=str(current)+'.ts'
        dict_of_lists[name] = url+name
        current += 1

    # 创建00000.ts - 99999.ts文件名
    # while current <= 600:
    #     name=str(current).zfill(5)+'.ts'
    #     dict_of_lists[name] = url+name
    #     current += 1

    # test folder is exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # 开始处理列表页面的数据，每个片段保存成一个文件
    for link in dict_of_lists.keys():
        print(u'正在处理页面：', link, ' ', dict_of_lists.get(link))
        r = requests.get( dict_of_lists.get(link) )
        if r.status_code is 200:
            with open(folder + link, "wb") as source:
                source.write(r.content)
                # time.sleep(random.random())
        else:
            print('error:',r.status_code)
            break

    # 输出，将所有片段按照从小到大顺序合并成一个文件
    join(folder, "file8.ts")
    



