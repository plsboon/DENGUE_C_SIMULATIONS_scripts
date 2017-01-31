#!/usr/bin/env python
import sys
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np

f=open(sys.argv[1]).readlines()
title=""
xl=""
yl=""
yvals=[]
time=[]
for i in f:
	if "xaxis" in i:
		xl=i.split("\"")[-2]
	if "yaxis" in i:
		yl=i.split("\"")[-2]
	if "title" in i:
		title=i.split("\"")[-2]
	if "@" not in i and "#" not in i:
		time.append(float(i.split()[0]))
		yvals.append(float(i.split()[1]))
	
matplotlib.rcParams.update({'font.size':20})

plt.figure(1,figsize=(30,10))
plt.title(title)
plt.xlabel(xl)
plt.ylabel(yl)
plt.plot(time,yvals,color='black',linewidth=2)
#plt.axis([0,max(time),0,max(yvals)+0.05])
plt.axis([min(time), max(time),0,max(yvals)+0.05])
plt.savefig(sys.argv[1][:-4]+".svg",format='svg',dpi=300)
