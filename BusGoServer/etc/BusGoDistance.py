#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

SW  = 23
GPIO.setup(SW, GPIO.IN)

while(True):
    if GPIO.input(SW) == True:
        print("Full")
        break
    else:
        print("Empty")
        break
