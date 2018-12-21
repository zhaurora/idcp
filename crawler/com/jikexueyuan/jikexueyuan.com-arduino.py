#-*_coding:utf8-*-
##########################################################################
# 抓取极客学院的课程介绍和课程详情，但不下载视频文件
# https://www.jikexueyuan.com/course/arduino/
##########################################################################
import requests
import re, os
import sys

class blocktidu():
    '''
    title, image, desc, url
    '''
    def __init__(self, titlein, imagein, descin, urlin):
        self.__title = titlein
        self.__image = imagein
        self.__desc = descin
        self.__url = urlin
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self,titlein):
        self.__title = titlein
        
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self,imagein):
        self.__image = imagein
        
    @property
    def desc(self):
        return self.__desc
    
    @desc.setter
    def desc(self,descin):
        self.__desc = descin
        
    @property
    def url(self):
        return self.__url
    
    @url.setter
    def url(self,urlin):
        self.__url = urlin


class blocktd():
    '''
    title, desc, classlist(it is a dictonary)
    '''
    def __init__(self, titlein, descin, classlistin):
        self.__title = titlein
        self.__desc = descin
        self.__classlist = classlistin
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self,titlein):
        self.__title = titlein
        
    @property
    def desc(self):
        return self.__desc
    
    @desc.setter
    def desc(self,descin):
        self.__desc = descin
        
    @property
    def classlist(self):
        return self.__classlist
    
    @classlist.setter
    def classlist(self,classlistin):
        self.__classlist = classlistin
        

class spider(object):
    '''
    # 采集URL中指定的文本块，并将其按照格式化保存为文件
    '''
    
    def __init__(self):
        print(u'开始爬取内容。。。')

    def getsource(self,url):
        '''
        获取网页url的网页源代码
        '''
        html = requests.get(url)
        return html.text

    def getwebresc(self,url,name):
        '''
        获取url指定的web资源，本段保存为.jpg
        name为应保存的文件名
        '''
        print(u'正在下载文件：', url)
        r = requests.get( url )
        with open(name, "wb") as source:
            source.write(r.content)
        
    def generateurl(self,url,totalpage):
        '''
        用来生产不同页数的链接
        暂时不适用
        '''
        nowpage = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        pagegroup = []
        for i in range(nowpage,totalpage+1):
            link = re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)
            pagegroup.append(link)
        return pagegroup

    def parselist(self,source):
        '''
        从每个给定的source中，抽取指定的课程块的信息，即
        匹配 <li * id= * </li> 格式的内容，包括换行符和空格
        返回listcontent，列表页面的格式化数据,[blocktidu(title, image, desc, url)]
        '''
        listcontent = []
        # 匹配 <li * id= * </li> 格式的内容，包括换行符和空格
        everyclass = re.findall('(<li id=[\s\S]*?</li>)',source,re.S)
        for each in everyclass:
            ctitle = re.search('<h2 class=.*?target="_blank".*?>(.*?)</a>',each,re.S).group(1)
            ctitle = re.sub('\"', '', ctitle)
            ctitle = re.sub(':', '：', ctitle)
            ctitle = ctitle.strip()
            cimage = re.search('<img src=(.*?)class=.*?>',each,re.S).group(1)
            cimage = re.sub('\"', '', cimage)
            cimage = cimage.strip()
            cdesc = re.search('</h2>.*?<p .*?>(.*?)</p>',each,re.S).group(1)
            cdesc = cdesc.strip()
            curl = re.search('<a href=(.*?)target="_blank".*?>',each,re.S).group(1)
            curl = re.sub('\"', '', curl)
            curl = curl.strip()
            listcontent.append(blocktidu(ctitle,cimage,cdesc,curl))
        
        return listcontent

    def savelist(self,listcontent):
        '''
        从listcontent课程块中提取出需要的信息，并保存到指定的文件中
        listcontent的格式为：[blocktidu,blocktidu,...]
        '''
        filename = './info.txt'
        folder = './detail/'
        # 创建文件夹
        if not os.path.exists(folder):
            os.makedirs(folder)
            
        f = open(filename, 'w',encoding='utf-8')
        for each in listcontent:
            f.writelines('\n' +each.title + '\n')
            f.writelines('\t' + each.image + '\n')
            f.writelines('\t' + each.desc + '\n')
            f.writelines('\t' + each.url + '\n')
            # 顺便保存每张图片
            self.getwebresc(each.image, folder+each.title+'.jpg')
        f.close()

    def parsedetail(self,source):
        '''
        从每个给定的source中，抽取指定的课程块的信息，即
        返回detailcontent，列表页面的格式化数据,[blockti(title, image, classlist(title,image))]
        '''
        # detailcontent：详情页面的格式化数据，包括title, desc, classlist
        # classlist：课程数据，title, desc
        detailcontent = []
        classlist = ''
        
        # 匹配 <h2><a href=.*?>(.*?)</a></h2> 格式的内容，包括换行符和空格
        dtitle = re.search('<h2><a href=.*?>(.*?)</a></h2>',source,re.S).group(1)
        dtitle = re.sub(':', '：', dtitle)
        dtitle = dtitle.strip()
        ddesc = re.search('<div class="infor-content">(.*?)</div>.*?<div class="btn-box">',source,re.S).group(1)
        ddesc = re.sub(re.compile(r"<[^>]*>", re.S), "", ddesc)
        ddesc = re.sub('\n\n', '', ddesc)
        ddesc = ddesc.strip()
        
        dvideolist = re.findall('(<div class="text-box">[\s\S]*?</div>)',source,re.S)
        for dvideo in dvideolist:
            ctitle = re.search('<a href=.*?>(.*?)</a>',dvideo,re.S).group(1)
            ctitle = re.sub('\"', '', ctitle)
            ctitle = re.sub(':', '：', ctitle)
            ctitle = ctitle.strip()
            cdesc = re.search('<p>(.*?)</p>',dvideo,re.S).group(1)
            cdesc = cdesc.strip()
            classlist = classlist + ctitle + ': \n' + cdesc +'\n\n'

        detailcontent.append(blocktd(dtitle, ddesc, classlist))
        return detailcontent

    def savedetail(self,detailcontent):
        '''
        从detailcontent课程块中提取出需要的信息，并按照dc.title为名保存到指定的文件中
        detailcontent的格式为：[blocktd, blocktd,...]
        '''
        folder = './detail/'
        # 创建文件夹
        if not os.path.exists(folder):
            os.makedirs(folder)

        for each in detailcontent:
            f = open(folder+each.title+'.txt','w',encoding='utf-8')
            f.writelines(each.title + '\n\n')
            f.writelines(each.desc + '\n\n')
            f.writelines(str(each.classlist) + '\n\n')
            f.close()

# main()
if __name__ == '__main__':

    # 初始化
    url = 'https://www.jikexueyuan.com/course/arduino/'
    jikespider = spider()
    # all_links = jikespider.changepage(url,1)
    # all_links = []
    # all_links.append(url)
    
    # 开始处理列表页面的数据
    print(u'正在处理页面：', url)
    
    # html = <!doctype html><html>...</html>
    html = jikespider.getsource(url)
    # classblock  =  [blocktidu(title, image, desc, url)]
    classblock = jikespider.parselist(html)
    # 保存列表页数据
    jikespider.savelist(classblock)
    
    #url = ['http:'+'//www.jikexueyuan.com/course/2573.html']
    # 开始处理详情页面的数据
    for eachlink in classblock:
        print(u'正在处理详情页面：', 'http:'+eachlink.url)
        html2 = jikespider.getsource('http:'+eachlink.url)
        dc = jikespider.parsedetail(html2)
        # 保存详情页数据
        jikespider.savedetail(dc)
    
    # 结束
    print(u'抓取结束')
