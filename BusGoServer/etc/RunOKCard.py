#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
import time
import random
import shlex


vpath = '/home/pi/BusGo/video/'

filename = {}
filename['busstop'] = vpath + 'busstop.mp4' #정거장
filename['okcard'] = vpath + 'okcard.mp4' #정거장

#동영상강제종료
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
showvideo = subprocess.Popen(["omxplayer",filename['okcard']])
out, err = showvideo.communicate()
#showvideo.wait()

#showvideo = subprocess.Popen(["omxplayer",filename['busstop']])
