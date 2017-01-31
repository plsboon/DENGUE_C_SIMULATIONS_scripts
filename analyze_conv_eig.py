#!/usr/bin/env python
import sys
import subprocess as sp
import os

if not os.path.isfile("dyn_alg.xtc"):
	print "dyn_alg.xtc missing"
	exit(1)
if not os.path.isfile("dyn.tpr"):
	print "dyn.tpr missing"
	exit(1)
if not os.path.isfile("index.ndx"):
	print "index.ndx missing"
	exit(1)

# CALCULATE EIGENVALS/EIGENVECS
f=open("inp","w")
f.write("coreCA\ncoreCA\n")
f.close()
sp.call("gmx covar -f dyn_alg.xtc -s dyn.tpr -n index.ndx -av average_200_end.gro -o eigenval_200_end.xvg -v eigenvec_200_end.trr -l covar_200_end.log -tu ns -b 200 < inp",shell=True)

# CONVERT EIGENVECS TO TEXT FORMAT
f=open("inp","w")
f.write("System\n")
f.close()
sp.call("gmx trjconv -f eigenvec_200_end.trr -s average_200_end.gro -o ev_200_end.gro < inp",shell=True)

# READ AVERAGE CRDS
averagecrd=[]
f=open("average_200_end.gro").readlines()
for i in f[2:-1]:
	averagecrd.append(float(i[20:28])*10.0)
	averagecrd.append(float(i[28:36])*10.0)
	averagecrd.append(float(i[36:44])*10.0)
blklen=len(f)

# READ MODE VECTORS
modes=[]
f=open("ev_200_end.gro").readlines()
nmodes=len(f)/blklen
for i in range(nmodes):
	modes.append([])
	for j in range(blklen-3):
		modes[i].append(float(f[blklen*i+2+j][20:28])*10.0)
		modes[i].append(float(f[blklen*i+2+j][28:36])*10.0)
		modes[i].append(float(f[blklen*i+2+j][36:44])*10.0)

# WRITE NMD FILE
f=open("nmodes_200_end.nmd","w")
f.write("coordinates ")
for i in averagecrd:
	f.write(" %8.4f"%(i))
f.write("\n")
for i,m in enumerate(modes):
	f.write("mode %5d 1.000 "%(i+1))
	for j in m:
		f.write(" %8.4f"%(j))
	f.write("\n")


f.close()
