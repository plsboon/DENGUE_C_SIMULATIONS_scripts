#!/usr/bin/env python
import sys
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np
import os
import argparse

parser=argparse.ArgumentParser(description='''This program plots the Root Mean Square Deviations of trajectories and can plot more than trajectory in one figure''')

parser.add_argument("-f","--infiles",nargs='+',metavar="F",help="list of rmsf .xvg files", required=True)
parser.add_argument("-lab","--labels",nargs='+',metavar='L',help="list of legend labels",required=True)
parser.add_argument("-o","--outfile", nargs='?', default="RMSF_blockwise.svg", help="output file name .svg")
#parser.add_argument("-c", "--crystal",nargs=1, help="Radius of gyration for crystal structure .xvg format")
#parser.add_argument("-log", nargs="?", default="block_gyration.log", help="log file containing hopefully useful information")
parser.add_argument("-title", nargs=1, help="list of figure titles")
args=parser.parse_args()

if len(args.infiles) != len(args.labels):
        print "Number of labels do not match number of input files"
        exit()



chain1=[]
chain2=[]
resnums=[]
for name in args.infiles:
	f=np.genfromtxt(name, skip_header=16, usecols=(1))
	i=np.genfromtxt(name, skip_header=16, usecols=(0))
	g=np.split(f,2)
	chain1.append(g[0])
	chain2.append(g[1])
	resnums.append(i)

a=np.unique(np.concatenate(resnums))

col=["#e41a1c","#377eb8","#4daf4a","#984ea3","#ff7f00"]
#lbl=["0-20% of simulations time","0-40% of simulation time","0-60% of simulations time","0-80% of simulation time","0-100% of simulation time"]
ticks=[0,10,20,30,40,50,60,70,80,90,100]
fig, ax=plt.subplots(2, sharex=True, figsize=(20,20))
plt.suptitle(args.title[0], size=40)
ax[0].set_ylabel("RMSF (nm)",size=30)
ax[1].set_ylabel("RMSF (nm)",size=30)
ax[0].set_title("Chain A",size=38)
ax[1].set_title("Chain B",size=38)
ax[1].set_xlabel('C'+r'$\alpha$'+' atom',size=30)
ax[0].grid()
ax[1].grid()
ax[0].axis([0,max(a)+1,0,4.0])
ax[1].axis([0,max(a)+1,0,4.0])
ax[1].set_xticks(ticks)
ax[1].set_xticklabels(ticks)
for i in range(len(chain1)):
	ax[0].plot(a,chain1[i],color=col[i],marker="o",linestyle="solid",label=args.labels[i])
	ax[1].plot(a,chain2[i],color=col[i],marker="o",linestyle="solid",label=args.labels[i])
ax[0].tick_params(labelsize=28)
ax[1].tick_params(labelsize=28)
ax[0].legend(fontsize=26)
ax[1].legend(fontsize=26)
plt.savefig(args.outfile,format='svg',dpi=300)

exit()
