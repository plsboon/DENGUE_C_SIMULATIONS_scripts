#!/usr/bin/env python
import os
import subprocess as sp
import sys
import string
from collections import defaultdict
import re

f=open(sys.argv[1]).readlines()
distance=float(sys.argv[2])
start=float(sys.argv[3])
end=float(sys.argv[4])

COM={}
for i in f:
	column=i.split()
	t_step=column[0]
	com_dist=column[1]
	COM.setdefault(float(com_dist),[]).append(t_step)

d=[]
i = start
while i <= end:
	d.append(i)
	i += distance


for i in range(len(d)):
	pmf_idx=i
	num=float(d[i])
	x= COM[num][0] if num in COM else COM[min(COM.keys(), key=lambda k: abs(k-num))][0]
	print str(pmf_idx) + "\t" + str(num) + "\t" + str(x)
	eq_mdp_in=open("/home/boonls/Projects/DENGUE_C_SIMULATIONS/mdp_files/pmf_pull_eq_XXXX.mdp").readlines()
	eq_mdp_out=open("pmf_pull_eq_%s.mdp" % pmf_idx, "w")
	prod_mdp_in=open("/home/boonls/Projects/DENGUE_C_SIMULATIONS/mdp_files/pmf_pull_prod_XXXX.mdp").readlines()
	prod_mdp_out=open("pmf_pull_prod_%s.mdp" % pmf_idx, "w")
	for line in eq_mdp_in:
		line=re.sub('XXXX',str(num), line)
		eq_mdp_out.write(line)
	for line in prod_mdp_in:
		line=re.sub('XXXX',str(num), line)
		prod_mdp_out.write(line)
	sp.call("ln -s conf'%s'.gro pmf_min_'%s'.gro" % (x, pmf_idx), shell=True)
	sp.call("gmx grompp -f /home/boonls/Projects/DENGUE_C_SIMULATIONS/mdp_files/pmf_pull_min.mdp -p ../topol.top -n ../index.ndx -c conf'%s'.gro -o pmf_min_'%s'.tpr" % (x, pmf_idx), shell=True)

exit() 



