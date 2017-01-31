#!/bin/bash

PTH="/home/boonls/Projects/DENGUE_C_SIMULATIONS"
#for f in dyn_alg_0_200ns.xtc dyn_alg_0_400ns.xtc dyn_alg_0_600ns.xtc dyn_alg_0_800ns.xtc dyn_alg.xtc
for f in dyn_alg_0_200ns.xtc dyn_alg_0_400ns.xtc dyn_alg.xtc
do 
	echo $f
	b=`basename $f .xtc`
	#cat << EOF > rms_coreCA
#coreCA
#coreCA
#EOF
#	gmx rms -s dyn.tpr -f $f -tu ps -o "rmsd_"$b".xvg" -n index.ndx < rms_coreCA
#	$PTH/analyze_plot_rmsd.py "rmsd_"$b".xvg"

       	cat << EOF > rmsf_full
C-alpha
C-alpha
EOF
	gmx rmsf -s min_ionized.tpr -f $f -o "rmsf"_$b".xvg" -res < rmsf_full
	#$PTH/analyze_plot_rmsf.py "rmsf_"$b".xvg"
done

