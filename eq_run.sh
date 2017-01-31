#!/bin/bash

for i in DENV2.1_complex_pmf DENV3.1_complex_pmf DENV4.1_complex_pmf
do
echo $i
cd $i
gmx grompp -f eq_1000.mdp -c min_ions.gro -p topol.top -o eq_1000.tpr -n index.ndx
gmx mdrun -deffnm eq_1000
gmx grompp -f eq_500.mdp -c eq_1000.gro -p topol.top -o eq_500.tpr -n index.ndx
gmx mdrun -deffnm eq_500
gmx grompp -f eq_100.mdp -c eq_500.gro -p topol.top -o eq_100.tpr -n index.ndx
gmx mdrun -deffnm eq_100
gmx grompp -f eq_50.mdp -c eq_100.gro -p topol.top -o eq_50.tpr -n index.ndx
gmx mdrun -deffnm eq_50
gmx grompp -f eq_10.mdp -c eq_50.gro -p topol.top -o eq_10.tpr -n index.ndx
gmx mdrun -deffnm eq_10
gmx grompp -f eq_0.mdp -c eq_10.gro -p topol.top -o eq_0.tpr -n index.ndx
gmx mdrun -deffnm eq_0
cd ..
done
