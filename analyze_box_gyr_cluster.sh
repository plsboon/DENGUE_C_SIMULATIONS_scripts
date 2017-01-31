#!/bin/bash

#Analyze box volume

#for i in DENV1c DENV2c DENV3c DENV4c
#do 
#cd $i

#Analyze box volume
#cat << EOF > inp
#0
#EOF

#	 gmx traj -f dyn_alg.xtc -s dyn.tpr -n index.ndx -ob dyn_box_volume.xvg -tu ns < inp

#Analyze radius of gyration of whole protein CA and coreCA
cat << EOF > inp
Protein
EOF
	gmx gyrate -f dyn_alg.xtc -s dyn.tpr -n index.ndx -o dyn_radius_gyration.xvg < inp

#cat << EOF > inp
#coreCA
#EOF
#	gmx gyrate -f dyn_alg.xtc -s dyn.tpr -n index.ndx -o dyn_radius_gyration_core.xvg < inp

#Analyze clustering of protein
#cat << EOF > inp
#coreCA
#Protein
#EOF

#	gmx cluster -f dyn_alg.xtc -s dyn.tpr -n index.ndx -g cluster_dyn.log -cl cluster_dyn.pdb -o cluster_rmsd_dyn.xpm -sz cluster_sizes.xvg -tu ns -method gromos < inp	
#cd ../
#done

