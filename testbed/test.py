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
    # url = 'http://www.qceit.org.cn/kpzg/infolist.aspx'
    # url2 = 'http://www.qceit.org.cn/calldata/calldata.aspx?datatype=getreportdatainfolist'
    # url3 = 'http://www.qceit.org.cn/kpzg/content.aspx?news_uid='
    # headers = {
    #     'Accept': 'application/json, text/javascript, */*; q=0.01',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    # }
    # values = {
    #     'config_name': 'data_sql',
    #     'data_id': 'get_news_list',
    #     'wheres': '%3Cwheres%3E%3Cand%3E%3Cand%20field_name%3D%22sns_folder.full_folder_name%22%20field_symbol%3D%22like%22%20field_value%3D%22%E4%BF%A1%E6%81%AF%E5%88%86%E7%B1%BB%2F%E6%96%B0%E9%97%BB%E5%85%AC%E5%91%8A%22%20%2F%3E%3C%2Fand%3E%3C%2Fwheres%3E',
    #     'file_path': 'fileroot%2Fsqldatacfg',
    #     'cur_page': '1',
    #     'records_per_page': '50'
    # }
    # home_page = requests.post(url, data=headers)
    # print(home_page.text)
    # home_page2 = requests.post(url2, data=values, headers=headers)
    # responsejson = json.loads(home_page2.text)
    # responsedate = responsejson['date']
    # print(responsedate)
    # datalist = []
    # for data in responsejson['data']:
    #     info = {}
    #     info['uid'] = data['news_uid']
    #     info['url'] = url3 + data['news_uid']
    #     info['title'] = data['news_subject']
    #     info['brief'] = data['news_brief']
    #     info['date'] = data['release_time']
    #     datalist.append(info)
    # print(datalist)
    # print(len(datalist))

    # SQLite 演示
    # import sqlite3
    # # 连接到SQLite数据库
    # # 数据库文件是test.db
    # # 如果文件不存在，会自动在当前目录创建:
    # conn = sqlite3.connect('test.db')
    # # 创建一个Cursor:
    # cursor = conn.cursor()
    # # 执行一条SQL语句，创建user表:
    # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # # 继续执行一条SQL语句，插入一条记录:
    # cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    # # 通过rowcount获得插入的行数:
    # print('rowcount =', cursor.rowcount)
    # # 关闭Cursor:
    # cursor.close()
    # # 提交事务:
    # conn.commit()
    # # 关闭Connection:
    # conn.close()
    # # 查询记录：
    # conn = sqlite3.connect('test.db')
    # cursor = conn.cursor()
    # # 执行查询语句:
    # cursor.execute('select * from user where id=?', '1')
    # # 获得查询结果集:
    # values = cursor.fetchall()
    # print(values)
    # cursor.close()
    # conn.close()

    # mysqldb
    # import time
    # import mysql.connector as MySQLdb
    # # 连接
    # conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="test", charset="utf8")
    # cursor = conn.cursor()
    # # 写入
    # sql = "insert into user(name,created) values(%s,%s)"
    # param = ("ccc", int(time.time()))
    # n = cursor.execute(sql, param)
    # conn.commit()
    # print(n)
    # # 更新
    # sql = "update user set name=%s where id=3"
    # param = ("ddd",)
    # n = cursor.execute(sql, param)
    # print(n)
    # # 查询
    # n = cursor.execute("select * from user")
    # for row in cursor.fetchall():
    #     print(row)
    #     # for r in row:
    #     #     print(r)
    # # 删除
    # sql = "delete from user where name=%s"
    # param = ("aaa",)
    # n = cursor.execute(sql, param)
    # print(n)
    # cursor.close()
    # # 关闭
    # conn.close()

    # # 遍历dict
    # dict_of_lists = {}
    # dict_of_lists['模型评估'] = 'https://13.cdn-vod.huaweicloud.com/asset/54a9a8824395b738959af87ab09096c1/play_video/35496d8c036b9d5514ae2243a5db2b18_1_1920X1080_3000_0_'
    # dict_of_lists['机器学习助力客户分群（上）'] = 'https://13.cdn-vod.huaweicloud.com/asset/3cb5973fe4ec0e7f24dfa5f5f734dcb8/play_video/6694ebc4fdd642b83d5ed5a5ce3490f5_1_1280X720_1000_0_'
    # dict_of_lists['机器学习助力客户分群（下）'] = 'https://13.cdn-vod.huaweicloud.com/asset/49ff970daba8b44883655836fdee7b63/play_video/921485b7b2c7381ed670347996a3c724_1_1280X688_500_0_'
    # dict_of_lists['机器学习助力商品质量分类（上）'] = 'https://13.cdn-vod.huaweicloud.com/asset/11d07a7d98d37e7f621f0c0597b48cc5/play_video/156f7666a3143eacec32e7109ae62f94_1_1280X720_1000_0_'
    # dict_of_lists['机器学习助力商品质量分类（下）'] = 'https://13.cdn-vod.huaweicloud.com/asset/7d83b1d81fb21a46586a54e4b9ff4c40/play_video/6069bb0f65488f4dc35a974888287413_1_1280X720_1000_0_'
    # dict_of_lists['机器学习助力预测性维护（上）'] = 'https://13.cdn-vod.huaweicloud.com/asset/3df9a4b880e1989331c84cacd5419500/play_video/101a7050a9958bac4d97e2fe862cd0b0_1_1280X720_1000_0_'
    # dict_of_lists['机器学习助力预测性维护（下）'] = 'https://13.cdn-vod.huaweicloud.com/asset/27237084abb1fc5dec3ce3e6ce11ec4d/play_video/f83150e577d76c21b87e88c8f0c225b4_1_1920X1080_3000_0_'
    #
    # for k,v in dict_of_lists.items():
    #     print(u'正在处理页面：', k, ' ', v)

    # def delfile(path):
    #     '''
    #     删除指定path下的所有文件和子文件
    #     :param path:
    #     :return:
    #     '''
    #     ls = os.listdir(path)
    #     for i in ls:
    #         c_path = os.path.join(path, i)
    #         if os.path.isdir(c_path):
    #             delfile(c_path)
    #         else:
    #             os.remove(c_path)
    #             print(c_path)
    # #
    # delfile('./ttt/')

    url = 'https://bbs.huaweicloud.com/forum/thread-10102-1-1.html'
    r = requests.get(url)
    if r.status_code is 200:
        str = r.content
        print(str.decode('utf-8'))
    else:
        print('error:', r.status_code)

    print('test program is end.')