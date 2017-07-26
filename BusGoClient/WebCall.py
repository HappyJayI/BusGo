#!/usr/bin/env python
# -*- coding: utf8 -*-

#BusGo 용

import signal
import subprocess
import sys
import os
import time
from urllib2 import urlopen
import RPi.GPIO as GPIO
import MFRC522

OldCardUID = "" 
NewCardUID = ""

OKCardUID = "53.148.134.171" #handicapped user
NOCardUID = "32.216.140.124" #general user
WaitCardUID = "117.87.172.165" #busstop waiting handicapped user

logtime = time.time()

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

#showvideo = subprocess.Popen(["omxplayer","--loop","--no-osd","/home/pi/BusGo/video/4.mp4"])

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        NewCardUID = str(uid[0])+"."+str(uid[1])+"."+str(uid[2])+"."+str(uid[3])

        #print(NewCardUID," -  ",OKCardUID)
        print "Card UID: " + NewCardUID

        try:
            #3Secs delay limitation with same rfid card
            if ( time.time() - logtime < 3 ) & ( NewCardUID == OldCardUID ):
                time.sleep(0)
            elif (NewCardUID == OKCardUID):
                #time.sleep(0)
                f = urlopen("http://192.168.1.39:8080/" + NewCardUID)
            elif (NewCardUID == WaitCardUID):       
                f2 = urlopen("http://192.168.1.39:8080/" + NewCardUID)
            else:
                time.sleep(0)
                #f2 = urlopen("http://192.168.1.39:8080/" + NewCardUID)  
        except ValueError:
            time.sleep(0)
        finally:
            OldCardUID = NewCardUID
            logtime = time.time()        

#SDA --> 24 : SPICEO
#SCK --> 23 : SPISCLK
#MOSI --> 19 : SPIMOSI
#MISO --> 21 : SPIMISO
#GND --> 6 : GND
#RST --> 22 : GPIO25
#3.3V --> 1 : 3.3



