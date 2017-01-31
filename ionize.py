#!/usr/bin/env python
import sys
import random

f=open(sys.argv[1]).readlines()

rep_na=int(sys.argv[2])
rep_cl=int(sys.argv[3])

n_rep=rep_na+rep_cl
n_atoms=len(f)-3
n_new=n_atoms-n_rep*2

#print("adding %d Na+ and %d Cl- ions to file %s"%(rep_na,rep_cl,sys.argv[1]))

non_sol_atoms=[]
sol_atoms=[]
for i in f[2:-1]:
	if "SOL " not in i:
		non_sol_atoms.append(i)
	else:
		sol_atoms.append(i)

wat_mols=[]
if len(sol_atoms)%3 == 0:
	for i in range(len(sol_atoms)/3):
		w=[]
		for j in range(3):
			w.append(sol_atoms[i*3+j])
		wat_mols.append(w)
else:
	print "something's wrong with sol_atoms"

to_replace=[]
for i in range(n_rep):
	n=random.choice(wat_mols)
	wat_mols.remove(n)
	to_replace.append(n)

new_na=[]
for i in to_replace[0:rep_na]:
	new_na.append(i[0][0:5]+"NA      NA"+i[0][15:])
new_cl=[]
for i in to_replace[rep_na:]:
	new_cl.append(i[0][0:5]+"CL      CL"+i[0][15:])

print f[0], # copy first line 
print "%d"%(n_new) # write new Natoms
for i in non_sol_atoms:
	print i,
for i in wat_mols:
	for j in range(3):
		print i[j],
for i in new_na:
	print i,
for i in new_cl:
	print i,
print f[-1],
