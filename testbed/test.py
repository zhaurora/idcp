'''
Created on 2018年9月30日

@author: frank
'''
import urllib
import requests
import re
import os
import json

# -*- coding: utf-8 -*-
from urllib.parse import splittype
from urllib.parse import splithost

if __name__ == '__main__':

    # 根据URL获取域名
    # def getdomain(url):
    #     # proto, rest = urllib.splittype(url)
    #     proto, rest = splittype(url)
    #     host, rest = splithost(rest)
    #     return host
    #
    # print(getdomain("http://www.cnblogs.com/goodhacker/admin/EditPosts.aspx?opt=1"))
    # print(getdomain("http://www.dlhitech.gov.cn/news/list/1.html?pageNumber=1"))
    # print(getdomain("https://vcbeat.net/Mzc0MjdjZWVkYjI3YmFmMzhkZDkxZWRhZmJlNGZkMzU="))
    # print(getdomain("www.baidu.com/s?wd=%E8%B6%B3%E5%8D%8F%E9%A2%81%E5%B8%83%E5%B7%A5%E8%B5%84%E5%87%86%E5%88%99"))
    # print(getdomain('http://www.qceit.org.cn/kpzg/content.aspx?news_uid='))

    # 下载视频文件
    # url = 'http://prime-system.jp/did-risk-monitor/en/wp-content/uploads/sites/2/2016/07/English2NoAudio.mp4'
    # folder = './folder/'
    # # test folder is exist
    # if not os.path.exists(folder):
    #     os.makedirs(folder)
    # print(u'正在处理页面：', url)
    # r = requests.get(url)
    # with open(folder + 'English2NoAudio.mp4', "wb") as source:
    #     source.write(r.content)
    # print(u'结束')

    # 用POST方法请求页面数据
    url = 'http://www.qceit.org.cn/kpzg/infolist.aspx'
    url2 = 'http://www.qceit.org.cn/calldata/calldata.aspx?datatype=getreportdatainfolist'
    url3 = 'http://www.qceit.org.cn/kpzg/content.aspx?news_uid='
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    values = {
        'config_name': 'data_sql',
        'data_id': 'get_news_list',
        'wheres': '%3Cwheres%3E%3Cand%3E%3Cand%20field_name%3D%22sns_folder.full_folder_name%22%20field_symbol%3D%22like%22%20field_value%3D%22%E4%BF%A1%E6%81%AF%E5%88%86%E7%B1%BB%2F%E6%96%B0%E9%97%BB%E5%85%AC%E5%91%8A%22%20%2F%3E%3C%2Fand%3E%3C%2Fwheres%3E',
        'file_path': 'fileroot%2Fsqldatacfg',
        'cur_page': '1',
        'records_per_page': '50'
    }
    # home_page = requests.post(url, data=headers)
    # print(home_page.text)
    home_page2 = requests.post(url2, data=values, headers=headers)
    responsejson = json.loads(home_page2.text)
    responsedate = responsejson['date']
    print(responsedate)
    datalist = []
    for data in responsejson['data']:
        info = {}
        info['uid'] = data['news_uid']
        info['url'] = url3 + data['news_uid']
        info['title'] = data['news_subject']
        info['brief'] = data['news_brief']
        info['date'] = data['release_time']
        datalist.append(info)
    print(datalist)
    print(len(datalist))





