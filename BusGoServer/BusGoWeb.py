#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
import subprocess

OldCardUID = "" 
NewCardUID = ""

OKCardUID = "53.148.134.171" #handicapped user
NOCardUID = "32.216.140.124" #general user
WaitCardUID = "117.87.172.165" #busstop waiting handicapped user

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        #seat = subprocess.Popen(["python","/home/pi/BusGo/BusGoDistance.py"],stdout=subprocess.PIPE)
        #out, err = seat.communicate()
        #out2 = (out.splitlines())
        #seat.wait()
        
        #if (name == OKCardUID) & (out2[0] == "Full" ) :       
        if (name == OKCardUID) :      
            subprocess.Popen(["python","/home/pi/BusGo/RunVideo.py"]) 
        elif (name == WaitCardUID) :       
            subprocess.Popen(["python","/home/pi/BusGo/WaitVideo.py"]) 
        else:
            subprocess.Popen(["python","/home/pi/BusGo/KillVideo.py"]) 

        return name

if __name__ == "__main__":
    app.run()