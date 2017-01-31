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
resnums=[]
for i in f:
	if "xaxis" in i:
		xl=i.split("\"")[-2]
	if "yaxis" in i:
		yl=i.split("\"")[-2]
	if "title" in i:
		title=i.split("\"")[-2]
	if "@" not in i and "#" not in i:
		resnums.append(int(i.split()[0]))
		yvals.append(float(i.split()[1]))
	
nsets=0
for i in resnums:
	if i == max(resnums):
		nsets+=1

y_plt=[]
for i in range(nsets):
	y_plt.append([])
	for j in range(max(resnums)):
		y_plt[-1].append(yvals[i*max(resnums)+j])


col=['#0000ff','#8080ff']

matplotlib.rcParams.update({'font.size':20})

plt.figure(1,figsize=(30,10))
plt.title(title)
plt.xlabel(xl)
plt.ylabel(yl)
plt.xticks(np.array(range(1,len(y_plt[0])+1,1))+0.5,range(1,len(y_plt[0])+1,1),rotation='vertical')
plt.axis([0.5,max(resnums)+1.5,0,max(yvals)+0.5])
plt.grid('on')
chns=[]
for i in range(nsets):
	chns.append(plt.bar(np.array(range(1,len(y_plt[0])+1))+0.1+i*0.4,y_plt[i],width=0.4,edgecolor='none',facecolor=col[i]))
plt.legend((chns[0][0],chns[1][0]),("Chain 1","Chain 2"))
plt.savefig(sys.argv[1][:-4]+".svg",format='svg',dpi=300)
