#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

vpath = '/home/pi/BusGo/video/'

filename = {}
filename['wait'] = vpath + 'wait.mp4' #busstop waiting

#kill playing video
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

#show video
showvideo = subprocess.Popen(["omxplayer",filename['wait']])


