import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from math import *
from time import *
import time
from matplotlib.colors import *

#Visibility toggle (boolean) for particular wind speed in polar
#ex.: vis01 means visibility for 0-1 kts of true wind
vis01=1
vis12=1
vis23=1
vis34=1
vis45=1
vis56=1
vis67=1
vis78=1
vis89=1
vis910=1
vis1011=1
vis1112=1
vis1213=1
vis1314=1
vis1415=1
vis1516=1
vis1617=1
vis1718=1
vis1819=1
vis1920=1
vis2021=1
vis2122=1
vis2223=1
vis2324=1
vis2425=1
vis2526=1
vis2627=1
vis2728=1
vis2829=1
vis29=1

def polarListSort(polarList):
    for i in range(len(polarList)/3):
	STW=polarList[(i*3)]
	HOW=polarList[(i*3)+2]
	CWS=polarList[(i*3)+1]
        print HOW,STW,CWS
	if CWS<1.:
            polarList01.append((HOW,STW,CWS))
        elif CWS<2.:
            polarList12.append((HOW,STW,CWS))
        elif CWS<3.:
            polarList23.append((HOW,STW,CWS))
        elif CWS<4.:
            polarList34.append((HOW,STW,CWS))
        elif CWS<5.:
            polarList45.append((HOW,STW,CWS))
        elif CWS<6.:
            polarList56.append((HOW,STW,CWS))
        elif CWS<7.:
            polarList67.append((HOW,STW,CWS))
        elif CWS<8.:
            polarList78.append((HOW,STW,CWS))
        elif CWS<9.:
            polarList89.append((HOW,STW,CWS))
        elif CWS<10.:
            polarList910.append((HOW,STW,CWS))
        elif CWS<11.:
            polarList1011.append((HOW,STW,CWS))
        elif CWS<12.:
            polarList1112.append((HOW,STW,CWS))
        elif CWS<13.:
            polarList1213.append((HOW,STW,CWS))
        elif CWS<14.:
            polarList1314.append((HOW,STW,CWS))
        elif CWS<15.:
            polarList1415.append((HOW,STW,CWS))
        elif CWS<16.:
            polarList1516.append((HOW,STW,CWS))
        elif CWS<17.:
            polarList1617.append((HOW,STW,CWS))
        elif CWS<18.:
            polarList1718.append((HOW,STW,CWS))
        elif CWS<19.:
            polarList1819.append((HOW,STW,CWS))
        elif CWS<20.:
            polarList1920.append((HOW,STW,CWS))
        elif CWS<21.:
            polarList2021.append((HOW,STW,CWS))
        elif CWS<22.:
            polarList2122.append((HOW,STW,CWS))
        elif CWS<23.:
            polarList2223.append((HOW,STW,CWS))
        elif CWS<24.:
            polarList2324.append((HOW,STW,CWS))
        elif CWS<25.:
            polarList2425.append((HOW,STW,CWS))
        elif CWS<26.:
            polarList2526.append((HOW,STW,CWS))
        elif CWS<27.:
            polarList2627.append((HOW,STW,CWS))
        elif CWS<28.:
            polarList2728.append((HOW,STW,CWS))
        elif CWS<29.:
            polarList2829.append((HOW,STW,CWS))
        elif CWS>29.:
            polarList29.append((HOW,STW,CWS))
    polarList01.sort()
    polarList12.sort()
    polarList23.sort()
    polarList34.sort()
    polarList45.sort()
    polarList56.sort()
    polarList67.sort()
    polarList78.sort()
    polarList89.sort()
    polarList910.sort()
    polarList1011.sort()
    polarList1112.sort()
    polarList1213.sort()
    polarList1314.sort()
    polarList1415.sort()
    polarList1516.sort()
    polarList1617.sort()
    polarList1718.sort()
    polarList1819.sort()
    polarList1920.sort()
    polarList2021.sort()
    polarList2122.sort()
    polarList2223.sort()
    polarList2324.sort()
    polarList2425.sort()
    polarList2526.sort()
    polarList2627.sort()
    polarList2728.sort()
    polarList2829.sort()
    polarList29.sort()
    for i in range(len(polarList01)):
	STW=polarList01[i][1]
	HOW=polarList01[i][0]
        CWS=1
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList12)):
	STW=polarList12[i][1]
	HOW=polarList12[i][0]
        CWS=2
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList23)):
	STW=polarList23[i][1]
	HOW=polarList23[i][0]
        CWS=3
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList34)):
	STW=polarList34[i][1]
	HOW=polarList34[i][0]
        CWS=4
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList45)):
	STW=polarList45[i][1]
	HOW=polarList45[i][0]
        CWS=5
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList56)):
	STW=polarList56[i][1]
	HOW=polarList56[i][0]
        CWS=6
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList67)):
	STW=polarList67[i][1]
	HOW=polarList67[i][0]
        CWS=7
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList78)):
	STW=polarList78[i][1]
	HOW=polarList78[i][0]
        CWS=8
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList89)):
	STW=polarList89[i][1]
	HOW=polarList89[i][0]
        CWS=9
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList910)):
	STW=polarList910[i][1]
	HOW=polarList910[i][0]
        CWS=10
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList1011)):
	STW=polarList1011[i][1]
	HOW=polarList1011[i][0]
        CWS=11
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList1112)):
	STW=polarList1112[i][1]
	HOW=polarList1112[i][0]
        CWS=12
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList1213)):
	STW=polarList1213[i][1]
	HOW=polarList1213[i][0]
        CWS=13
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList1314)):
	STW=polarList1314[i][1]
	HOW=polarList1314[i][0]
        CWS=14
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList1415)):
	STW=polarList1415[i][1]
	HOW=polarList1415[i][0]
        CWS=15
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList1516)):
	STW=polarList1516[i][1]
	HOW=polarList1516[i][0]
        CWS=16
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList1617)):
	STW=polarList1617[i][1]
	HOW=polarList1617[i][0]
        CWS=17
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList1718)):
	STW=polarList1718[i][1]
	HOW=polarList1718[i][0]
        CWS=18
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList1819)):
	STW=polarList1819[i][1]
	HOW=polarList1819[i][0]
        CWS=19
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList1920)):
	STW=polarList1920[i][1]
	HOW=polarList1920[i][0]
        CWS=20
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList2021)):
	STW=polarList2021[i][1]
	HOW=polarList2021[i][0]
        CWS=21
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList2122)):
	STW=polarList2122[i][1]
	HOW=polarList2122[i][0]
        CWS=22
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList2223)):
	STW=polarList2223[i][1]
	HOW=polarList2223[i][0]
        CWS=23
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList2324)):
	STW=polarList2324[i][1]
	HOW=polarList2324[i][0]
        CWS=24
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList2425)):
	STW=polarList2425[i][1]
	HOW=polarList2425[i][0]
        CWS=25
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList2526)):
	STW=polarList2526[i][1]
	HOW=polarList2526[i][0]
        CWS=26
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList2627)):
	STW=polarList2627[i][1]
	HOW=polarList2627[i][0]
        CWS=27
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList2728)):
	STW=polarList2728[i][1]
	HOW=polarList2728[i][0]
        CWS=28
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList2829)):
	STW=polarList2829[i][1]
	HOW=polarList2829[i][0]
        CWS=29
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)
    for i in range(len(polarList29)):
	STW=polarList29[i][1]
	HOW=polarList29[i][0]
        CWS=30
	polarListSpreadsheet.append(STW)
	polarListSpreadsheet.append(HOW)
	polarListSpreadsheet.append(CWS)

polarListSpreadsheet=[]
polarList01=[]
polarList12=[]
polarList23=[]
polarList34=[]
polarList45=[]
polarList56=[]
polarList67=[]
polarList78=[]
polarList89=[]
polarList910=[]
polarList1011=[]
polarList1112=[]
polarList1213=[]
polarList1314=[]
polarList1415=[]
polarList1516=[]
polarList1617=[]
polarList1718=[]
polarList1819=[]
polarList1920=[]
polarList2021=[]
polarList2122=[]
polarList2223=[]
polarList2324=[]
polarList2425=[]
polarList2526=[]
polarList2627=[]
polarList2728=[]
polarList2829=[]
polarList29=[]

polarList=[]

file=open ("polarpoints.txt", "r")
for line in file: 
    polarList.append(line)

for i in range(len(polarList)):
    polarList[i]=polarList[i][:-1]
    polarList[i]=polarList[i][:-1]
    polarList[i]=float(polarList[i])

print polarList

polarListSort(polarList)

polarListReadable = open('polardatahuman_spreadsheet_readable.txt', 'w')

for i in range(len(polarListSpreadsheet)/3):
    var23 = polarListSpreadsheet[(i*3)]
    var24 = polarListSpreadsheet[(i*3)+1]
    var25 = polarListSpreadsheet[(i*3)+2]
    print>>polarListReadable,(var23,var24,var25)

if vis01:
    for i in range(len(polarList01)):
	r=polarList01[0][1]
	theta=polarList01[0][0]
	colors=(0.0, 0.0, 1.0)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList01[0]
if vis12:
    for i in range(len(polarList12)):
	r=polarList12[0][1]
	theta=polarList12[0][0]
	colors=(0.0, 0.1, 0.9)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList12[0]
if vis23:
    for i in range(len(polarList23)):
	r=polarList23[0][1]
	theta=polarList23[0][0]
	colors=(0.0, 0.2, 0.8)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList23[0]
if vis34:
    for i in range(len(polarList34)):
	r=polarList34[0][1]
	theta=polarList34[0][0]
	colors=(0.0, 0.3, 0.7)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList34[0]
if vis45:
    for i in range(len(polarList45)):
	r=polarList45[0][1]
	theta=polarList45[0][0]
	colors=(0.0, 0.4, 0.6)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList45[0]
if vis56:
    for i in range(len(polarList56)):
	r=polarList56[0][1]
	theta=polarList56[0][0]
	colors=(0.0, 0.5, 0.5)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList56[0]
if vis67:
    for i in range(len(polarList67)):
	r=polarList67[0][1]
	theta=polarList67[0][0]
	colors=(0.0, 0.6, 0.4)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList67[0]
if vis78:
    for i in range(len(polarList78)):
	r=polarList78[0][1]
	theta=polarList78[0][0]
	colors=(0.0, 0.7, 0.3)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList78[0]
if vis89:
    for i in range(len(polarList89)):
	r=polarList89[0][1]
	theta=polarList89[0][0]
	colors=(0.0, 0.8, 0.2)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList89[0]
if vis910:
    for i in range(len(polarList910)):
	r=polarList910[0][1]
	theta=polarList910[0][0]
	colors=(0.0, 0.9, 0.1)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList910[0]
if vis1011:
    for i in range(len(polarList1011)):
	r=polarList1011[0][1]
	theta=polarList1011[0][0]
	colors=(0.1, 0.0, 0.9)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList1011[0]
if vis1112:
    for i in range(len(polarList1112)):
	r=polarList1112[0][1]
	theta=polarList1112[0][0]
	colors=(0.2, 0.0, 0.8)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList1112[0]
if vis1213:
    for i in range(len(polarList1213)):
	r=polarList1213[0][1]
	theta=polarList1213[0][0]
	colors=(0.3, 0.0, 0.7)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList1213[0]
if vis1314:
    for i in range(len(polarList1314)):
	r=polarList1314[0][1]
	theta=polarList1314[0][0]
	colors=(0.4, 0.0, 0.6)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList1314[0]
if vis1415:
    for i in range(len(polarList1415)):
	r=polarList1415[0][1]
	theta=polarList1415[0][0]
	colors=(0.5, 0.0, 0.5)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList1415[0]
if vis1516:
    for i in range(len(polarList1516)):
	r=polarList1516[0][1]
	theta=polarList1516[0][0]
	colors=(0.6, 0.0, 0.4)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList1516[0]
if vis1617:
    for i in range(len(polarList1617)):
	r=polarList1617[0][1]
	theta=polarList1617[0][0]
	colors=(0.7, 0.0, 0.3)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList1617[0]
if vis1718:
    for i in range(len(polarList1718)):
	r=polarList1718[0][1]
	theta=polarList1718[0][0]
	colors=(0.8, 0.0, 0.2)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList1718[0]
if vis1819:
    for i in range(len(polarList1819)):
	r=polarList1819[0][1]
	theta=polarList1819[0][0]
	colors=(0.9, 0.0, 0.1)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList1819[0]
if vis1920:
    for i in range(len(polarList1920)):
	r=polarList1920[0][1]
	theta=polarList1920[0][0]
	colors=(1.0, 0.0, 0.0)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList1920[0]
if vis2021:
    for i in range(len(polarList2021)):
	r=polarList2021[0][1]
	theta=polarList2021[0][0]
	colors=(0.9, 0.1, 0.0)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList2021[0]
if vis2122:
    for i in range(len(polarList2122)):
	r=polarList2122[0][1]
	theta=polarList2122[0][0]
	colors=(0.8, 0.2, 0.0)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList2122[0]
if vis2223:
    for i in range(len(polarList2223)):
	r=polarList2223[0][1]
	theta=polarList2223[0][0]
	colors=(0.7, 0.3, 0.0)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList2223[0]
if vis2324:
    for i in range(len(polarList2324)):
	r=polarList2324[0][1]
	theta=polarList2324[0][0]
	colors=(0.6, 0.4, 0.0)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList2324[0]
if vis2425:
    for i in range(len(polarList2425)):
	r=polarList2425[0][1]
	theta=polarList2425[0][0]
	colors=(0.5, 0.5, 0.0)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList2425[0]
if vis2526:
    for i in range(len(polarList2526)):
	r=polarList2526[0][1]
	theta=polarList2526[0][0]
	colors=(0.4, 0.6, 0.0)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList2526[0]
if vis2627:
    for i in range(len(polarList2627)):
	r=polarList2627[0][1]
	theta=polarList2627[0][0]
	colors=(0.3, 0.7, 0.0)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList2627[0]
if vis2728:
    for i in range(len(polarList2728)):
	r=polarList2728[0][1]
	theta=polarList2728[0][0]
	colors=(0.2, 0.8, 0.0)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList2728[0]
if vis2829:
    for i in range(len(polarList2829)):
	r=polarList2829[0][1]
	theta=polarList2829[0][0]
	colors=(0.1, 0.9, 0.0)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList2829[0]
if vis29:
    for i in range(len(polarList29)):
	r=polarList29[0][1]
	theta=polarList29[0][0]
	colors=(0.0, 1.0, 0.0)
	size=20.
	ax = plt.subplot(111, projection='polar')
        c = plt.scatter(theta, r, c=colors, s=size, cmap=plt.cm.hsv)
        c.set_alpha(0.75)
	del polarList29[0]

plt.savefig('polar.png')
plt.show()
