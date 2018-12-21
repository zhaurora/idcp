#-*_coding:utf8-*-
'''
定期采集http://www.dlhitech.gov.cn/下的通知公告栏目内容
将其保存到数据库内，定期检查并发送给指定邮件地址
HTTP GET, STATIC HTML
'''
import re
import requests
import time
import random
from urllib.parse import splittype
from urllib.parse import splithost


class spider(object):
    def __init__(self):
        print(u'开始爬取内容。。。')

    @property
    def hostname(self):
        return self.__hostname

    @hostname.setter
    def hostname(self, hostnamein):
        self.__hostname = hostnamein

#getsource用来获取网页源代码
    def getsource(self,url):
        # print(u'getsource(',url,')')
        html = requests.get(url)
        return html.text

# changepage用来生产不同页数的链接
    def changepage(self,url,total_page):
        # http://www.dlhitech.gov.cn/news/list/1.html?pageNumber=2
        # print(u'changepage(', url, ',',total_page,')')
        now_page = int(re.search('pageNumber=(\d+)',url,re.S).group(1))
        page_group = []
        for i in range(now_page,total_page+1):
            link = re.sub('pageNumber=\d+','?pageNumber=%s'%i,url,re.S)
            page_group.append(link)
        return page_group

# gettotalpage用来抓取总页码
    def gettotalpage(self, source):
        # 匹配<span class="p_total">1/126</span> 格式的内容，只获取/后的数字
        temp = re.search('<span class="p_total".*?/(.*?)</span>', source, re.S).group(1)
        totalpage = int(temp)
        return totalpage

# getallnews用来抓取所有新闻
    def getallnews(self,source):
        # 匹配 <div class="fen-news">*</div> 格式的内容，取出正文新闻块，舍弃其他块
        newsdiv = re.search('<div class="fen-news">(.*?)</div>', source, re.S).group(1)
        # 匹配 <li * deg= * </li> 格式的内容，包括换行符和空格
        allnews = re.findall('(<li>[\s\S]*?</li>)',newsdiv,re.S)
        return allnews

#g etinfo用来从每个新闻雷暴中提取出需要的信息
    def getinfo(self,news):
        # news 格式为：
        # '<li><a href="/news/view_54701.html" target="_blank"
        # title="关于公布大连高新区第一批政府补贴职业培训机构名单的通知">关于公布大连高新区第一批政府补贴职业培训机构名单的通知</a>
        # <span>2018-12-20</span></li>'
        info = {}
        info['title'] = re.search('<a href=.*?title=.*?>(.*?)</a>',news,re.S).group(1)
        info['title'] = info['title'].strip()
        info['url'] = re.search('<a href="(.*?)" target=.*?</a>',news,re.S).group(1)
        info['url'] = self.__hostname + info['url'].strip()
        info['date'] = re.search('<span>(.*?)</span>',news,re.S).group(1)
        info['date'] = info['date'].replace('\n', ' ')
        return info

# saveinfo用来保存结果到notice.txt文件中
    def saveinfo(self,classinfo):
        f = open('./notice.txt','w',encoding='utf-8')
        for each in classinfo:
            f.writelines(each['title'] + '\t' + each['date'] + '\t' + each['url'] + '\n')
        f.close()

if __name__ == '__main__':
    notices_info = []
    # base url
    url = 'http://www.dlhitech.gov.cn/news/list/1.html?pageNumber=1'
    dlhtspider = spider()
    home_page = dlhtspider.getsource(url)
    # print(home_page)

    # 获取主站域名hostname
    proto, rest = splittype(url)
    host, rest = splithost(rest)
    dlhtspider.hostname = host
    # print(dlhtspider.hostname)

    # 准备最大页码，获取所有分页链接
    total_page = dlhtspider.gettotalpage(home_page)
    # print(total_page)
    all_links = dlhtspider.changepage(url, total_page)
    # print(all_links)

    # 处理每个分页对应的页面新闻
    for link in all_links:
        print(u'正在处理页面：', link)
        html = dlhtspider.getsource(link)
        # 抽取页面中的所有新闻条目
        all_news = dlhtspider.getallnews(html)
        # 对每个新闻，分解其通知的标题、日期、链接，并临时保存
        for each in all_news:
            info = dlhtspider.getinfo(each)
            notices_info.append(info)
        # 随机暂停0-1秒
        time.sleep(random.random())

    # 保存到文件中
    dlhtspider.saveinfo(notices_info)
    print(u'处理完毕')
