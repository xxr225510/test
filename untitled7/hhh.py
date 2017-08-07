import urllib
import re
import json
import 
class hhh:
    def demo(self):
        def music(music_id):

            lrc_url='http://music.163.com/api/song/lyric?'+'id='+str(music_id)+'&lv=1&kv=1&tv=1'

            r=urllib.urlopen(lrc_url)
            json_object=r.read()

            j=json.loads(json_object)

            lrc=j['lrc']['lyric']
            pat=re.compile(r'\[.*\]')
            lrc=re.sub(pat,"",lrc)
            lrc=lrc.strip()
            return lrc
        print music(184408)




hhh().demo()