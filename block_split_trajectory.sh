#!/bin/bash

cat << EOF > inp
System
EOF

#gmx trjconv -f dyn_alg.xtc -s dyn.tpr -b 0 -e 200 -tu ns -o dyn_alg_0_200ns.xtc < inp
#gmx trjconv -f dyn_alg.xtc -s dyn.tpr -b 200 -e 400 -tu ns -o dyn_alg_201_400ns.xtc < inp
#gmx trjconv -f dyn_alg.xtc -s dyn.tpr -b 400 -e 600 -tu ns -o dyn_alg_401_600ns.xtc < inp
#gmx trjconv -f dyn_alg.xtc -s dyn.tpr -b 600 -e 800 -tu ns -o dyn_alg_601_800ns.xtc < inp
#gmx trjconv -f dyn_alg.xtc -s dyn.tpr -b 800 -e 1000 -tu ns -o dyn_alg_801_1000ns.xtc < inp

gmx trjconv -f dyn_alg.xtc -s dyn.tpr -b 0 -e 200 -tu ns -o dyn_alg_0_200ns.xtc < inp
gmx trjconv -f dyn_alg.xtc -s dyn.tpr -b 0 -e 400 -tu ns -o dyn_alg_0_400ns.xtc < inp
#gmx trjconv -f dyn_alg.xtc -s dyn.tpr -b 0 -e 600 -tu ns -o dyn_alg_0_600ns.xtc < inp
#gmx trjconv -f dyn_alg.xtc -s dyn.tpr -b 0 -e 800 -tu ns -o dyn_alg_0_800ns.xtc < inp
#gmx trjconv -f dyn_alg.xtc -s dyn.tpr -b 0 -e 1000 -tu ns -o dyn_alg_0_1000ns.xtc < inp

##########################################
#splitting the DENVC and RNA trajectories#
##########################################

#gmx trjconv -f dyn_combine_alg.xtc -s dyn_long.tpr -b 0 -e 200 -tu ns -o dyn_alg_0_200ns.xtc < inp
#gmx trjconv -f dyn_combine_alg.xtc -s dyn_long.tpr -b 0 -e 400 -tu ns -o dyn_alg_0_400ns.xtc < inp

