#-*_coding:utf8-*-
'''
@date 2019年2月19日
@desc 处理http请求的基本处理方法
from http://www.cnblogs.com/goldd/p/5457229.html
@author frank
'''
import urllib.request
import urllib.parse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

if __name__ == '__main__':
    # url1 = 'http://www.redasen.com/'
    #1、最简单的获取网页数据, geturl(), info(), getcode()
    # response = urllib.request.urlopen(url1)
    # html = response.read()
    # print(response.info())

    #2、使用 Request获取网页数据
    # req = urllib.request.Request(url1)
    # response = urllib.request.urlopen(req)
    # the_page = response.read()
    # print(response.info())

    #3、发送数据
    # url = 'http://localhost/login.php'
    # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    # values = {
    #     'act' : 'login',
    #     'login[email]' : 'yzhang@i9i8.com',
    #     'login[password]' : '123456'
    # }
    # data = urllib.parse.urlencode(values)
    # req = urllib.request.Request(url, data)
    # req.add_header('Referer', 'http://www.python.org/')
    # response = urllib.request.urlopen(req)
    # the_page = response.read()
    # print(the_page.decode("utf8"))

    #4、发送数据和header
    # url = 'http://localhost/login.php'
    # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    # values = {
    #     'act' : 'login',
    #     'login[email]' : 'yzhang@i9i8.com',
    #     'login[password]' : '123456'
    # }
    # headers = { 'User-Agent' : user_agent }
    # data = urllib.parse.urlencode(values)
    # req = urllib.request.Request(url, data, headers)
    # response = urllib.request.urlopen(req)
    # the_page = response.read()
    # print(the_page.decode("utf8"))

    #5、http 错误
    # req = urllib.request.Request('http://www.111cn.net')
    # try:
    #     urllib.request.urlopen(req)
    # except urllib.error.HTTPError as e:
    #     print(e.code)
    #     print(e.read().decode("utf8"))

    #6、异常处理1
    # req = Request("http://www.111cn.net /")
    # try:
    #     response = urlopen(req)
    # except HTTPError as e:
    #     print('The server couldn\'t fulfill the request.')
    #     print('Error code: ', e.code)
    # except URLError as e:
    #     print('We failed to reach a server.')
    #     print('Reason: ', e.reason)
    # else:
    #     print("good!")
    #     print(response.read().decode("utf8"))

    #7、异常处理2
    # req = Request("http://www.111cn.net /")
    # try:
    #     response = urlopen(req)
    # except URLError as e:
    #     if hasattr(e, 'reason'):
    #         print('We failed to reach a server.')
    #         print('Reason: ', e.reason)
    #     elif hasattr(e, 'code'):
    #         print('The server couldn\'t fulfill the request.')
    #         print('Error code: ', e.code)
    #     else:
    #         print("good!")
    #         print(response.read().decode("utf8"))

    #8、HTTP 认证
    # # create a password manager
    # password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    # # Add the username and password.
    # # If we knew the realm, we could use it instead of None.
    # top_level_url = "https://www.111cn.net/"
    # password_mgr.add_password(None, top_level_url, 'rekfan', 'xxxxxx')
    # handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    # # create "opener" (OpenerDirector instance)
    # opener = urllib.request.build_opener(handler)
    # # use the opener to fetch a URL
    # a_url = "https://www.111cn.net/"
    # x = opener.open(a_url)
    # print(x.read())
    # # Install the opener.
    # # Now all calls to urllib.request.urlopen use our opener.
    # urllib.request.install_opener(opener)
    # a = urllib.request.urlopen(a_url).read().decode('utf8')
    # print(a)

    #9、使用代理
    # proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})
    # opener = urllib.request.build_opener(proxy_support)
    # urllib.request.install_opener(opener)
    # a = urllib.request.urlopen("http://www.111cn.net").read().decode("utf8")
    # print(a)

    #10、超时
    import socket
    # timeout in seconds
    timeout = 2
    socket.setdefaulttimeout(timeout)
    # this call to urllib.request.urlopen now uses the default timeout
    # we have set in the socket module
    req = urllib.request.Request('http://google.com/')
    a = urllib.request.urlopen(req).read()
    print(a)

