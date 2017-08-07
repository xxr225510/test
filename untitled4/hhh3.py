from Tkinter import *
import tkMessageBox
# -*- coding:utf-8 -*-

class hhh3:
    def demo(self):
        def get_imgae():
            name=nameent.get().encode('utf-8')
            if not name:
                tkMessageBox.showinfo('notice','please type your name!')
                return
            html=urllib2.urlopen('http://www/uustv.com/',data='word={}&sizes=609fonts=jfcs.ttf&fontcolor=%23000000'.format(name)).read()
            reg=r'<div class="tu"><img src="(.*?)"/><?div'
            imgurl=reg.findall(reg,html)[0]
            imgurl='http:/www.uustv.com/'+imgurl
            urllib.urlretrieve(imgurl,'`%s.gif'%name.decode('utf-8').encode('gbk'))
            try:
                im=Image.open('%s.gif'%name.decode('utf-8').encode('gbk'))
                im.show()
                im.close()
            except:
                print 'open the image by yourself'





        root=Tk()
        root.title('name designing')
        root.geometry('+700+200')
        Label(root,text='name:',font=('SimSun',15)).grid()
        nameent=Entry(root,font=('SimSun',15))
        nameent.grid(row=0,column=1)
        Button(root,text='design',font=('Simsun',15),width='15' ,height='1',command=get_imgae()).grid(row=3,column=1)





        mainloop()



hhh3().demo()

