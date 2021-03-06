#-*_coding:utf8-*-
import requests
import re
import sys

class spider(object):
    def __init__(self):
        print(u'开始爬取内容。。。')

#getsource用来获取网页源代码
    def getsource(self,url):
        html = requests.get(url)
        return html.text

#changepage用来生产不同页数的链接
    def changepage(self,url,total_page):
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group = []
        for i in range(now_page,total_page+1):
            link = re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)
            page_group.append(link)
        return page_group

#geteveryclass用来抓取每个课程块的信息
    def geteveryclass(self,source):
        # 匹配 <li * deg= * </li> 格式的内容，包括换行符和空格
        everyclass = re.findall('(<li id=[\s\S]*?</li>)',source,re.S)
        return everyclass

#getinfo用来从每个课程块中提取出我们需要的信息
    def getinfo(self,eachclass):
        info = {}
        info['title'] = re.search('<h2 class=.*?target="_blank".*?>(.*?)</a>',eachclass,re.S).group(1)
        info['title'] = info['title'].strip()
        info['content'] = re.search('</h2>.*?<p .*?>(.*?)</p>',eachclass,re.S).group(1)
        info['content'] = info['content'].strip()
        timeandlevel = re.findall('<em>(.*?)</em>',eachclass,re.S)
        info['classtime'] = timeandlevel[0].replace('\n', ' ')
        info['classtime'] = info['classtime'].strip()
        info['classlevel'] = timeandlevel[1]
        info['classlevel'] = info['classlevel'].strip()
        info['learnnum'] = re.search('"learn-number">(.*?)</em>',eachclass,re.S).group(1)
        info['learnnum'] = info['learnnum'].strip()
        return info

#saveinfo用来保存结果到info.txt文件中
    def saveinfo(self,classinfo):
        f = open('./info.txt','w',encoding='utf-8')
        for each in classinfo:
            f.writelines('title:' + each['title'] + '\n')
            f.writelines('content:' + each['content'] + '\n')
            f.writelines('classtime:' + each['classtime'] + '\n')
            f.writelines('classlevel:' + each['classlevel'] + '\n')
            f.writelines('learnnum:' + each['learnnum'] +'\n\n')
        f.close()

#saveinfo用来打印结果到终端
    def printinfo(self,classinfo):
        for each in classinfo:
            print('title:' + each['title'])
            print('content:' + each['content'])
            print('classtime:' + each['classtime'])
            print('classlevel:' + each['classlevel'])
            print('learnnum:' + each['learnnum'] +'\n')


if __name__ == '__main__':

    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jikespider = spider()
    all_links = jikespider.changepage(url,1)
    for link in all_links:
        print(u'正在处理页面：', link)
        html = jikespider.getsource(link)
        everyclass = jikespider.geteveryclass(html)
        for each in everyclass:
            info = jikespider.getinfo(each)
            classinfo.append(info)
    jikespider.saveinfo(classinfo)
    jikespider.printinfo(classinfo)


