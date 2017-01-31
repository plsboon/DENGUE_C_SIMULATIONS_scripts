#!/usr/bin/env python
import sys
import os

if not os.path.isfile("eigenval_200_end.xvg"):
	print "eigenval_200_end.xvg does not exist!"
	exit(1)


f=open("eigenval_200_end.xvg").readlines()
g=open("eigenval_perc_200_end.xvg","w")
title=""
xl=""
yl=""
ty=""
eigenvals=[]
nmodes=[]
for i in f:
        if "xaxis" in i:
                xl=i.split("\"")[-2]
        if "yaxis" in i:
                yl=i.split("\"")[-2]
        if "title" in i:
                title=i.split("\"")[-2]
	if "TYPE" in i:
		ty=i.split(" ")[-1]
        if "@" not in i and "#" not in i:
                nmodes.append(int(i.split()[0]))
                eigenvals.append(float(i.split()[1]))
        

eigen_sum=sum(eigenvals)
eigen_perc=[]
for j in range(len(eigenvals)):
	k=(eigenvals[j]/eigen_sum)*100.0
	eigen_perc.append(k)

start=0.0
eigen_perc_sum=[]
for l in range(len(eigen_perc)):
	m=start+eigen_perc[l]
	eigen_perc_sum.append(m)
	start = m 	

g.write("@\tTitle\t"+'"'+title+'"'+"\n")
g.write("@\txaxis label\t"+'"'+xl+'"'+"\n")
g.write("@\tyaxis label\t"+'"'+yl+'"'+"\n")
g.write("@TYPE "+ty+"\n")

for row in zip(nmodes, eigenvals, eigen_perc,eigen_perc_sum):
	print1='{:5d}\t{:10.10f}\t{:10.7f}\t{:10.5f}'.format(*row)+ "\n" 
	g.write(print1)


g.close()
