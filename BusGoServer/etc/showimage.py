#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
import time

path = '/home/pi/workspace/'


filename = {}
filename['jpg'] = path + 'a.jpg'
filename['png'] = path + 'a.PNG'
filename['gif'] = path + 'a.gif'
filename['mp4'] = path + 'a.mp4'


#subprocess.Popen(["ls","-l"])

showvideo = subprocess.Popen(["omxplayer",filename['mp4']])
out, err = showvideo.communicate()
print( out, err )



showimage =  subprocess.Popen(["gpicview",filename['gif']])
out, err = showimage.communicate()
print( out, err )

#image실행
#showvideo = subprocess.Popen(path +'gpicview '+ filename['jpg'])
#out, err = showvideo.communicate()
#showvideo = subprocess.Popen([sys.executable, path + ' gpicview ' +  filename['jpg']])
#out, err = showvideo.communicate()



