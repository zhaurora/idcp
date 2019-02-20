#-*_coding:utf8-*-
'''
定期采集http://www.qceit.org.cn/kpzg/infolist.aspx下的通知公告栏目内容
将其保存到数据库内，定期检查并发送给指定邮件地址
涉及的知识点：HTML POST, JSON
'''
import re
import requests
import time
import random
import json
from urllib.parse import splittype
from urllib.parse import splithost

class spider(object):
    def __init__(self):
        print(u'开始爬取内容。。。')

    def postsource(self, url, data):
        '''
        postsource用来获取网页源代码
        :param url: 访问的URL
        :param data: POST 参数
        :return: 源码TEXT
        '''
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
        # data = {
        #     'config_name': 'data_sql',
        #     'data_id': 'get_news_list',
        #     'wheres': '%3Cwheres%3E%3Cand%3E%3Cand%20field_name%3D%22sns_folder.full_folder_name%22%20field_symbol%3D%22like%22%20field_value%3D%22%E4%BF%A1%E6%81%AF%E5%88%86%E7%B1%BB%2F%E6%96%B0%E9%97%BB%E5%85%AC%E5%91%8A%22%20%2F%3E%3C%2Fand%3E%3C%2Fwheres%3E',
        #     'file_path': 'fileroot%2Fsqldatacfg',
        #     'cur_page': '1',
        #     'records_per_page': '50'
        # }
        html_post = requests.post(url, headers=headers, data=data)
        return html_post.text

    def saveinfo(self,classinfo):
        '''
        saveinfo用来保存结果到notice.txt文件中
        classinfo结果格式为[{'uid': 'xxx', 'url': 'http://www.qceit.org.cn/kpzg/content.aspx?news_uid=xxx', 'title': '关于xxx的通知', 'brief': '', 'date': '2019-02-12'},...]
        :param classinfo: list
        :return:
        '''
        f = open('./notice.txt','w',encoding='utf-8')
        for each in classinfo:
            f.writelines(each['title'] + '\t' + each['brief'] + '\t' + each['date'] + '\t' + each['url'] + '\n')
        f.close()
        print(u'保存完成')

'''
====请求分页时用的POST====
Request URL: http://www.qceit.org.cn/calldata/calldata.aspx?datatype=getreportdatainfolist
Request Method: POST

====Headers的内容====
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36

====请求的Data====
config_name: data_sql
data_id: get_news_list
wheres: %3Cwheres%3E%3Cand%3E%3Cand%20field_name%3D%22sns_folder.full_folder_name%22%20field_symbol%3D%22like%22%20field_value%3D%22%E4%BF%A1%E6%81%AF%E5%88%86%E7%B1%BB%2F%E6%96%B0%E9%97%BB%E5%85%AC%E5%91%8A%22%20%2F%3E%3C%2Fand%3E%3C%2Fwheres%3E
file_path: fileroot%2Fsqldatacfg
cur_page: 2
records_per_page: 10

====Response====
{
    "id": 0, 
    "id1": 0, 
    "sid": "", 
    "sid1": "cdc6b5b8-19fa-4acc-9dbe-3aef0a59c849", 
    "name": "", 
    "code": "1", 
    "flag": "0", 
    "desc": "", 
    "html": {}, 
    "count": "35", 
    "data": {
        {
            "news_uid": "3127cb89-2fed-4707-9b6d-17f68ad0f230", 
            "news_type_code": "文章", 
            "news_subject": "关于发布《2019年全国青少年机器人技术等级考试师资培训计划》的通知", 
            "news_brief": "", 
            "news_url": "", 
            "news_file": "", 
            "news_pic": "", 
            "release_time": "2019-02-12", 
            "releaser": "", 
            "release_user_uid": "94c44786-164e-4640-a79c-8b615a70f1ae", 
            "news_status_code": "正常", 
            "browse_num": "570", 
            "is_delete": "N", 
            "creator": "管理员", 
            "create_time": "2019-02-12 20:35:15", 
            "modifyer": "管理员", 
            "modify_time": "2019-02-14 09:48:41", 
            "news_code": "", 
            "news_keywords": "", 
            "page_file": ""
        }
    }, 
    "date": "2019-02-20", 
    "datetime": "2019-02-20 10:07:55", 
    "user_host_ip": "223.102.1.120", 
    "run_time": "5"
}

====详情页的URL组成====
http://www.qceit.org.cn/kpzg/content.aspx?news_uid=3127cb89-2fed-4707-9b6d-17f68ad0f230

'''
if __name__ == '__main__':
    # base url
    homeurl = 'http://www.qceit.org.cn/kpzg/infolist.aspx'
    dataurl = 'http://www.qceit.org.cn/calldata/calldata.aspx?datatype=getreportdatainfolist'
    detailurl = 'http://www.qceit.org.cn/kpzg/content.aspx?news_uid='
    values = {
        'config_name': 'data_sql',
        'data_id': 'get_news_list',
        'wheres': '%3Cwheres%3E%3Cand%3E%3Cand%20field_name%3D%22sns_folder.full_folder_name%22%20field_symbol%3D%22like%22%20field_value%3D%22%E4%BF%A1%E6%81%AF%E5%88%86%E7%B1%BB%2F%E6%96%B0%E9%97%BB%E5%85%AC%E5%91%8A%22%20%2F%3E%3C%2Fand%3E%3C%2Fwheres%3E',
        'file_path': 'fileroot%2Fsqldatacfg',
        'cur_page': '1',
        'records_per_page': '50'
    }
    qceitspider = spider()

    notices_info = []
    # 处理动态请求新闻列表
    print(u'正在处理页面：', dataurl)
    htmldata = qceitspider.postsource(dataurl,values)
    # 获取本次更新的日期
    responsejson = json.loads(htmldata)
    newsdate = responsejson['date']
    newscount = responsejson['count']
    print(u'在',newsdate,u'获取到',newscount,u'条数据')

    # 设置分页采集过程略
    # ......

    # 对每个新闻，分解其通知的标题、日期、链接，并临时保存
    thisdata = responsejson['data']
    for each in thisdata:
        info = {}
        info['uid'] = each['news_uid']
        info['url'] = detailurl + each['news_uid']
        info['title'] = each['news_subject']
        info['brief'] = each['news_brief']
        info['date'] = each['release_time']
        notices_info.append(info)
    # 随机暂停0-1秒
    time.sleep(random.random())

    # 保存到文件中
    qceitspider.saveinfo(notices_info)
    print(u'处理完毕')
