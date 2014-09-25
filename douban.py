# coding = utf-8
import json
import urllib2
import string
import schedule
import time
import datetime
import os

log = 'log_douban'
data_douban = '../api/data_douban'
host = 'http://www.douban.com/'
main='doulist/1867090/'
sta1_patt='"title"'
sta2_patt='photo_wrap'
sta3_patt='data-total-page='

def parse(post_url):

    raw=urllib2.urlopen(post_url).readlines()
    n=len(raw)
    imgs=[]
    for x in range(n):
        if sta2_patt in raw[x]:
            l=raw[x+2].find('src=')
	    r=raw[x+2].find('/>')
            imgs.append(raw[x+2][l+5:r-2].replace("thumb", "photo"))
    return (len(imgs), imgs)

def go():
    posts={'number':0, 'posts':[]}
    open(log, 'ab').write(datetime.datetime.now().strftime('[%b/%d/%y %H:%M:%S] - go\n'))
    raw=urllib2.urlopen(host+main).readlines()
    n=len(raw)
    for x in range(n):
        if sta1_patt in raw[x]:
            l=raw[x+2].find('href=')
            r=raw[x+2].find('target=')
            name_str = raw[x+3]
            name = name_str.strip()
            print raw[x+2][l+6:r-2]
            raw2=urllib2.urlopen(raw[x+2][l+6:r-2]).readlines()
            m=len(raw2)
            for y in range(m):
                if sta3_patt in raw2[y]:
	    l1=raw2[y].find('page=')
 	    r1=raw2[y].find('</span>')
                    a=int(raw2[y][l1+6:r1-3])
            try:
                count = 0
  	while count <= a:
                    tup=parse(url1+'?start='+str(count*18))
            count = count + 1
                post={'title':name, 'img_number':0, 'imgs':[]}
                post['img_number']=tup[0]
                post['imgs']=tup[1]
                posts['posts'].append(post)
                posts['number']+=1
            except:
                print raw[x+2][l+6:r-2], '404 not found..'
    open(data_douban, 'w').write(json.dumps(posts, indent=4))

go()
