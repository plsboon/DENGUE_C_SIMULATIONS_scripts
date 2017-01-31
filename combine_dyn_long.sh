#!/bin/bash


	#cat << EOF > inp
#System
#EOF

#	gmx trjconv -f dyn.xtc -s dyn.tpr -o dyn_skip.xtc -skip 2 < inp
	# INPUT FOR TRJCAT
#	cat << EOF > inp
#0
#c
#EOF
#	gmx trjcat -f dyn_skip.xtc dyn_long.xtc -settime -o dyn_combine.xtc < inp

	# INPUT FOR TRJCONV 1 (PBC)
	cat << EOF > inp
Halfcore
0
EOF
	gmx trjconv -f dyn_combine.xtc -s dyn.tpr -pbc mol -center -ur compact -o dyn_pbc.xtc -n index.ndx -skip 4 < inp

	#INPUT FOR TRJCONV 2 (CENTER & FIT)
	cat << EOF > inp
coreCA
Halfcore
0
EOF
	gmx trjconv -f dyn_pbc.xtc -s dyn.tpr -center -fit rot+trans -n index.ndx -o dyn_alg.xtc -tu ns < inp


