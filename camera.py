#! /usr/bin/python
from picamera import PiCamera
from time import sleep
from subprocess import call
import picamera
import datetime
import os
import ftplib

os.chdir('/home/pi/Desktop/pics/')

camera = picamera.PiCamera()
#camera = PiCamera()
#iname =1
#myname=str(iname)+".jpg"

session = ftplib.FTP('50.62.188.189','pi@swim.tools','zain@pi1') #ftplib.FTP('ftp address', 'ftp_username', 'ftp_password' )
while True:
       ##camera.start_preview()
    name=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    camera.capture(name+".jpg")
    
    file = open('/home/pi/Desktop/pics/'+name+'.jpg','rb')
    session.storbinary('STOR '+name+'.jpg', file)
    file.close()
    sleep(40)    
    
    
