#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
import time
import random
import shlex

ipath = '/home/pi/BusGo/image/'
vpath = '/home/pi/BusGo/video/'

filename = {}
filename['i1'] = ipath + '1.jpg' #정거장

filename['v1'] = vpath + '1.mp4' #공공캠페인 교통약자 배려
filename['v2'] = vpath + '2.mp4' #유재석
filename['v3'] = vpath + '3.mp4' #공공캪페인 일반 배려
filename['v4'] = vpath + '4.mp4' #기지개

#대기모드 : 정거장i,v
#교통약자 승차시
#교통약자 tag시
#일반인 착석시

#subprocess.Popen(["ls","-l"])

#omxplayer 강제종료
#tasklist =  subprocess.Popen(["sudo","killall","-q","omxplayer"])
#subprocess.Popen(["sudo","killall","-q","omxplayer"])


ord = str(random.randint(1,4))

proc1 = subprocess.Popen(["ps","axg"], stdout=subprocess.PIPE)
proc1.wait()
proc2 = subprocess.Popen(["grep","omxplayer"],stdin=proc1.stdout,stdout=subprocess.PIPE)
out, err = proc2.communicate()
out2 = out.splitlines()

for i in out2:
    out3 = i.split()
    if out3[4] != "grep":
        tasklist =  subprocess.Popen(["kill",out3[0]])   

proc2.wait()

showvideo = subprocess.Popen(["omxplayer",filename['v'+ord]])
#out, err = showvideo.communicate()
#print( out, err )


#if (out.index('omxplayer')>0) :
#    print(out)


#gpicview 강제종료
#tasklist =  subprocess.Popen(["killall","gpicview"])
#showimage =  subprocess.Popen(["gpicview",filename['jpg']])
#out, err = showimage.communicate()
#print( out, err )

#image실행
#showvideo = subprocess.Popen(path +'gpicview '+ filename['jpg'])
#out, err = showvideo.communicate()
#showvideo = subprocess.Popen([sys.executable, path + ' gpicview ' +  filename['jpg']])
#out, err = showvideo.communicate()



