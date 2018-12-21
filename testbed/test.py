'''
Created on 2018年9月30日

@author: banshu
'''
import urllib

# -*- coding: utf-8 -*-
from urllib.parse import splittype
from urllib.parse import splithost

if __name__ == '__main__':

    # 根据URL获取域名
    def getdomain(url):
        # proto, rest = urllib.splittype(url)
        proto, rest = splittype(url)
        host, rest = splithost(rest)
        return host

    print(getdomain("http://www.cnblogs.com/goodhacker/admin/EditPosts.aspx?opt=1"))
    print(getdomain("http://www.dlhitech.gov.cn/news/list/1.html?pageNumber=1"))
    print(getdomain("https://vcbeat.net/Mzc0MjdjZWVkYjI3YmFmMzhkZDkxZWRhZmJlNGZkMzU="))
    print(getdomain("www.baidu.com/s?wd=%E8%B6%B3%E5%8D%8F%E9%A2%81%E5%B8%83%E5%B7%A5%E8%B5%84%E5%87%86%E5%88%99"))



