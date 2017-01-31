#!/bin/bash


# INPUT FOR TRJCONV 1 (PBC)
	cat << EOF > inp
HalfCore
0
EOF
	gmx trjconv -f dyn.xtc -s dyn.tpr -n index.ndx -center -pbc mol -ur compact -o dyn_pbc.xtc -skip 4  < inp

#INPUT FOR TRJCONV 2 (CENTER & FIT)
	cat << EOF > inp
CoreCA
HalfCore
0
EOF
	gmx trjconv -f dyn_pbc.xtc -s dyn.tpr -n index.ndx -center -fit rot+trans -o dyn_alg.xtc -tu ns < inp
