#!/bin/bash
for i in DENV1c DENV2c DENV3c DENV4c 
do
cd $i 

#	cat << EOF > pdb2gmx_inp
#2
#1
#EOF
#	gmx pdb2gmx -f *.pdb < pdb2gmx_inp
#	gmx editconf -f conf.gro -bt cubic -d 1.0 -o box.gro
#	gmx solvate -cp box.gro -cs /usr/local/gromacs/share/gromacs/top/amber03ws.ff/tip4p2005.gro -p topol.top -o solv.gro
#	gmx grompp -f min.mdp -c solv.gro -p topol.top -o min.tpr
#	gmx mdrun -deffnm min
	gmx mdrun -deffnm min_ionized
cd ..
done

