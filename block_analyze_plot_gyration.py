#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt 
import numpy as np
import argparse

col=['#ff7f00','#a6cee3','#e31a1c','#b2df8a','#33a02c','#fb9a99','#1f78b4','#fdbf6f','#cab2d6','#6a3d9a','#ffff99','#b15928']
 
parser=argparse.ArgumentParser(description='''This program take one or more radius of gyration files and plots the mean and standard deviation as a line with error bars''')

parser.add_argument("-f","--infiles", nargs='+',metavar='F', help="list of .xvg files", required=True)
parser.add_argument("-lab","--labels", nargs='+', metavar='L', help="list of labels for input files", required=True)
parser.add_argument("-o","--outfile", nargs='?', default="block_gyration.svg", help="output file name .svg")
parser.add_argument("-c", "--crystal",nargs=1, help="Radius of gyration for crystal structure .xvg format")
parser.add_argument("-log", nargs="?", default="block_gyration.log", help="log file containing hopefully useful information")
parser.add_argument("-title", nargs=1, help="list of figure titles")
args=parser.parse_args()

if len(args.infiles) != len(args.labels):
	print "Number of labels do not match number of input files"
	exit()

else:
	log_file=open(args.log,'w')
	log_file.write("#Input_Files"+'\t'+"Labels"+'\n')
	for n in range(len(args.infiles)):
		log_file.write(args.infiles[n]+'\t'+args.labels[n]+'\n')
	
	log_file.write("#Output file name"+'\n')	
	log_file.write(args.outfile+'\n')
	log_file.write("#Crystal structure input"+'\n')
	crys_rg=[]
	if args.crystal == None:
		crys_rg.append(0)
		log_file.write("No"+'\n')
	else :
		log_file.write("Yes"+'\n')
		with open(args.crystal[0]) as crys_in:
			for lin in crys_in:
				if "@" not in lin and "#" not in lin:
                                        lin=lin.split()
                                        crys_rg.append(float(lin[1]))
                                
	plt.figure(figsize=(10,10))
	plt.title(args.title[0], size=30) 
	plt.xlabel("Simulation Time (ns)", size=30)
	plt.ylabel("Radius of gyration (nm)",size=30)
	plt.tick_params(labelsize=24)	
	blocks=[100000.0,200000.0,300000.0,400000.0,500000.0,600000.0,700000.0,800000.0,900000.0,1000000.0]
	ticks=[100,200,300,400,500,600,700,800,900,1000]
	log_file.write("#Block_intervals_(ps)"+'\n')
	log_file.write(str(blocks)+'\n')
	log_file.write("#Label"+'\t'+"Mean"+'\t'+"Standard_Deviations"+'\n')
	if crys_rg[0] != 0:
		plt.axhline(y=crys_rg[0], xmin=0, xmax=1, hold=None, label="crystal structure", color='black', linestyle='dashed')
	else:
		pass
	for i in range(len(args.infiles)):
		rg=[]
		ts=[]
		with open(args.infiles[i]) as fd:
			for line in fd:
				if "@" not in line and "#" not in line:
					line=line.split()
					rg.append(float(line[1]))
					ts.append(float(line[0]))	
		rd=[]
		count=0
		for k in range(len(blocks)):
			for j in [j for j,x in enumerate(ts) if x == blocks[k]]:
				rd.append(rg[count:j+1])
				count=j+1
	
		means=[np.mean(x) for x in rd]
		sd=[np.std(x) for x in rd]
		if len(means) != len(blocks):
			ap_len=len(blocks)-len(means)
			count=1
			while (count <= ap_len):
				means.append(np.nan)
				sd.append(np.nan)
				count = count + 1
		log_file.write(str(args.labels[i])+'\t'+str(means)+'\t'+str(sd)+'\n')
		
		plt.errorbar(blocks,means,yerr=sd,label=str(args.labels[i]),color=str(col[i]),marker="o",linewidth=2)
		plt.axis([0,max(blocks)+200000,0,3])
		plt.legend(loc=4,fontsize=20)
		plt.xticks(blocks, ticks,size=20)
	plt.savefig(args.outfile, format='svg', dpi=300)
	log_file.close()
exit()
