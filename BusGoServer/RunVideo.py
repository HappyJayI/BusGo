#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import random

vpath = '/home/pi/BusGo/video/'

filename = {}
filename['v1'] = vpath + '1.mp4' #campaign 1
filename['v2'] = vpath + '2.mp4' #campaign 2
filename['v3'] = vpath + '3.mp4' #campaign 3
filename['busstop'] = vpath + 'busstop.mp4' #busstop information
filename['wait'] = vpath + 'wait.mp4' #handicapped user waiting

#강제종료
ord = str(random.randint(1,3))

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

#실행
showvideo = subprocess.Popen(["omxplayer",filename['v'+ord]])
out, err = showvideo.communicate()
showvideo.wait()

showvideo = subprocess.Popen(["omxplayer",filename['busstop']])

