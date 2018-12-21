#-*_coding:utf8-*-
import requests
import os, sys
import time

readsize = 1024

#将指定的formdir下所有文件合并成tofile文件
def join(fromdir, tofile):
    output=open(tofile,"wb")
    #out = open(tofile, "wb")
    parts=os.listdir(fromdir)
    parts.sort()
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
 2016中小学创客教育资源调研报告--S42
 https://jp.hjenglish.com/new/v14944725744893/
 '''    
if __name__ == '__main__':
   
    # 初始化
    url = 'https://record-manual-hls.cctalk.com/cg7kf3NXsPqxRnu6pyYt3aPD7Fk=/lgxhKx-Rhf2A-ck3hLs3PX7o3TPc/'
    folder = './folder/'
    dict_of_lists = {}
    
    # 创建000000.ts - 000645.ts文件名
    current = 0
    while current <= 645:
        name=str(current).zfill(6)+'.ts'
        dict_of_lists[name] = url+name
        current += 1
    
    # 开始处理列表页面的数据，每个片段保存成一个文件
    for link in dict_of_lists.keys():
        print(u'正在处理页面：', link, ' ', dict_of_lists.get(link))
        r = requests.get( dict_of_lists.get(link) )
        with open(folder+link, "wb") as source:
            source.write(r.content)
            #time.sleep(1)
    
    # 输出，将所有片段按照从小到大顺序合并成一个文件
    join(folder, "newfile.ts")
    



