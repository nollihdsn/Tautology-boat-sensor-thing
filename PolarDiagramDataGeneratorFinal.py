import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from math import *
from time import *
import time
from Tkinter import *
import random
import tkMessageBox
from gps3.agps3threaded import AGPS3mechanism

'''
agps_thread = AGPS3mechanism()  # Instantiate AGPS3 Mechanisms
agps_thread.stream_data()  # From localhost (), or other hosts, by example, (host='gps.ddns.net')
agps_thread.run_thread()  # Throttle time to sleep after an empty lookup, default '()' 0.2 two tenths of a second  

#Delay is in order to give time for the GPS to find a fix. If you get persistant errors in sensorQuery, increasing the sleep duration could help.
time.sleep(5)

def sensorQuery(agps_thread):
    SOG=agps_thread.data_stream.speed
    COG=agps_thread.data_stream.track
    COG=COG*pi/180.
    #Query sensors
    #Adjust values based on calibration factors
    AWS=random.uniform(0.,15.)
    AWO=(random.uniform(0.,180.)*pi/180.)
    AVH=(random.uniform(0.,360.)*pi/180.)
    h=(random.uniform(0.,360.)*pi/180.)
    return SOG,COG,AWO,h,AWS,AVH
'''

def sensorQuery():
    #Query sensors
    #Adjust values based on calibration factors
    SOG=random.uniform(0.,10.)
    COG=(random.uniform(0.,360.)*pi/180.)
    AWS=random.uniform(0.,15.)
    AWO=(random.uniform(0.,180.)*pi/180.)
    h=(random.uniform(0.,360.)*pi/180.)
    #Compass heading of anemometer device, used to true it to the heading of the boat without complex installation
    AVH=(random.uniform(0.,360.)*pi/180.)
    return SOG,COG,AWO,h,AWS,AVH

#Shunt boolean for proas! Tacking will take care of itself
SHUNT=0
RECORD=0

def degrees(a):
    if a>=2.*pi:
        a=a-(2.*pi)
    elif a<0.:
        a=a+(2.*pi)
    return a

def polarCorrect(COG,AWO,h,SHUNT,AVH):
    if SHUNT:
        AWO=pi-AWO
        h=h-pi
	AVH=AVH-pi
        AWO=AWO+(h-AVH)
    else:
        AWO=AWO-(h-AVH)
    #AWO: windward of heading=positive
    if AWO>pi:
        AWO=(2.*pi)-AWO
    COG=degrees(COG)
    AWO=degrees(AWO)
    h=degrees(h)
    COG2=COG
    AWO2=AWO
    h2=h
    return COG2,AWO2,h2

l=0

def pointCalc(SOG,COG2,AWS,AWO2,h2):
    if h2>COG2:
        h2=COG2-(h2-COG2)
    l=COG2-h2
    TWS=sqrt(AWS**2+SOG**2-(2*AWS*SOG*cos(AWO2)))
    TWO=acos((TWS**2+SOG**2-AWS**2)/(2*TWS*SOG))
    return TWS,TWO,l

def recordOnOff():
    global RECORD
    if RECORD:
	RECORD=0
        return RECORD
    else:
	RECORD=1
        return RECORD

def shuntOnOff():
    global SHUNT
    if SHUNT:
	SHUNT=0
        return SHUNT
    else:
	SHUNT=1
        return SHUNT

file = open("polarpoints.txt","w") 

try:
    root = Tk()
    var = StringVar()
    var12 = StringVar()
    SOGA = Label( root, textvariable=var, relief=RAISED )
    SOGB = Label( root, textvariable=var12, relief=RAISED )
    var.set("SOG: ")
    SOGA.pack()
    SOGB.pack()
    var1 = StringVar()
    var13 = StringVar()
    COGA = Label( root, textvariable=var1, relief=RAISED )
    COGB = Label( root, textvariable=var13, relief=RAISED )
    var1.set("COG: ")
    COGA.pack()
    COGB.pack()
    var3 = StringVar()
    var15 = StringVar()
    HDGA = Label( root, textvariable=var3, relief=RAISED )
    HDGB = Label( root, textvariable=var15, relief=RAISED )
    var3.set("HDG: ")
    HDGA.pack()
    HDGB.pack()
    var4 = StringVar()
    var16 = StringVar()
    LWYA = Label( root, textvariable=var4, relief=RAISED )
    LWYB = Label( root, textvariable=var16, relief=RAISED )
    var4.set("LWY: ")
    LWYA.pack()
    LWYB.pack()
    var5 = StringVar()
    var17 = StringVar()
    AWSA = Label( root, textvariable=var5, relief=RAISED )
    AWSB = Label( root, textvariable=var17, relief=RAISED )
    var5.set("AWS: ")
    AWSA.pack()
    AWSB.pack()
    var6 = StringVar()
    var18 = StringVar()
    AWDA = Label( root, textvariable=var6, relief=RAISED )
    AWDB = Label( root, textvariable=var18, relief=RAISED )
    var6.set("AWO: ")
    AWDA.pack()
    AWDB.pack()
    var9 = StringVar()
    var21 = StringVar()
    TWSA = Label( root, textvariable=var9, relief=RAISED )
    TWSB = Label( root, textvariable=var21, relief=RAISED )
    var9.set("TWS: ")
    TWSA.pack()
    TWSB.pack()
    var10 = StringVar()
    var22 = StringVar()
    TWOA = Label( root, textvariable=var10, relief=RAISED )
    TWOB = Label( root, textvariable=var22, relief=RAISED )
    var10.set("TWO: ")
    TWOA.pack()
    TWOB.pack()
    R = Button(root, text ="Record", command = recordOnOff)
    R.pack()
    var28 = StringVar()
    var29 = StringVar()
    Record = Label( root, textvariable=var28, relief=RAISED )
    Record.pack()
    S = Button(root, text ="Shunt", command = shuntOnOff)
    S.pack()
    Shunt = Label( root, textvariable=var29, relief=RAISED )
    Shunt.pack()
    while True:
        #SOG,COG,AWO,h,AWS,AVH=sensorQuery(agps_thread)
        SOG,COG,AWO,h,AWS,AVH=sensorQuery()
        COG2,AWO2,h2=polarCorrect(COG,AWO,h,SHUNT,AVH)
        TWS,TWO,l=pointCalc(SOG,COG2,AWS,AWO2,h2)
        if RECORD:
            file.write(str(SOG))
            file.write("\n")
            file.write(str(TWS))
            file.write("\n")
            file.write(str(TWO))
            file.write("\n")
        #dataList.append((TWS,SOG,COG2,AWS,SHUNT,h2,l))
	var12.set(str(round(SOG, 1)))
	var13.set(str(round(COG2*180./pi, 1)))
	var15.set(str(round(h2*180./pi, 1)))
	var17.set(str(round(AWS, 1)))
	var18.set(str(round(AWO2*180./pi, 1)))
	var21.set(str(round(TWS, 1)))
	var22.set(str(round(TWO*180./pi, 1)))
        var16.set(str(round(l*180./pi, 1)))
	var28.set(RECORD)
	var29.set(SHUNT)
        root.update()
        time.sleep(5)
        #print TWO

except KeyboardInterrupt:
    file.close()
    file=open ("polarpoints.txt", "r")
