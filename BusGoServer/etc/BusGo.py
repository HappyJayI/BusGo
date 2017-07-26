#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import subprocess
import sys
import os
import time

OldCardUID = "" #카드번호 담기 중복 입력 방지용 3초내 재인식 방지
NewCardUID = ""

OKCardUID = "53.148.134.171" #교통약자
NOCardUID = "32.216.140.124" #일반인
WaitCardUID = "117.87.172.165" #정거장 대기 교통약자

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

        print(NewCardUID," -  ",OKCardUID)

        # Print UID
        if ( time.time() - logtime < 3 ) & ( NewCardUID == OldCardUID ):
            time.sleep(0)
        elif (NewCardUID == OKCardUID ):  #교통약자 탑승시 교통약자용 동영상
            #time.sleep(0)
            subprocess.Popen(["python","/home/pi/BusGo/RunOKCard.py"])     

        elif (NewCardUID == WaitCardUID ):  #교통약자 탑승시 교통약자용 동영상
            #time.sleep(0)
            subprocess.Popen(["python","/home/pi/BusGo/RunOKCard.py"])     
            
        else:  #일반인 탑승시 배려 동영상 
            #time.sleep(0)
            subprocess.Popen(["python","/home/pi/BusGo/RunVideo.py"])

        OldCardUID = NewCardUID

        logtime = time.time()
        print "Card UID: " + NewCardUID

#SDA --> 24 : SPICEO
#SCK --> 23 : SPISCLK
#MOSI --> 19 : SPIMOSI
#MISO --> 21 : SPIMISO
#GND --> 6 : GND
#RST --> 22 : GPIO25
#3.3V --> 1 : 3.3