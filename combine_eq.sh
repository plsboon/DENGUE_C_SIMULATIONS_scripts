#!/bin/bash


	# INPUT FOR TRJCAT
#	cat << EOF > inp
#0
#c
#c
#c
#c
#c
#EOF
#	gmx trjcat -f eq_1000.xtc eq_500.xtc eq_100.xtc eq_50.xtc eq_10.xtc eq_0.xtc -settime -o eq.xtc < inp

	# INPUT FOR TRJCONV 1 (PBC)
#	cat << EOF > inp
#0
#EOF
#	gmx trjconv -f eq.xtc -s eq_1000.tpr -pbc mol -o eq_pbc.xtc < inp

	#INPUT FOR TRJCONV 2 (CENTER & FIT)
	cat << EOF > inp
coreCA
coreCA
0
EOF
	gmx trjconv -f eq_pbc.xtc -s eq_1000.tpr -center -fit rot+trans -n index.ndx -o eq_alg.xtc < inp


