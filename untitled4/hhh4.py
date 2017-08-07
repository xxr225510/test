import urllib,re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')




class hhh4:
    def demo(self):
        def page(pg):
            url='http://www.pengfu.com/index_%s.html'%pg
            html=urllib.urlopen(url).read()
            #print html
            return html

        def title():
            html=page(1)
            reg=re.compile(r'<h1 class="dp-b"><a href=".*?" target="_blank">(.*?)</a>')
            item=re.findall(reg,html)
            #print item
            for t in item:
                print t
            return item

        def content(html):
            reg=r'<img src=".*?" width='
            item=re.findall(reg,html)
            print item
            return item

        def download(url,name):
            path='image%s.jpg'%name.decode('utf-8').encode('gbk')
            urllib.urlretrieve(url,path)


        for i in range(1,6):
            html=page(1)
            title_list=title()
            content_list=content(html)
            for i,z in zip(title_list,content_list):
                download(z,i)
                print i,z






hhh4().demo()