#!/bin/bash

for f in DENV1c DENV2c DENV3c DENV4c
do 
	echo $f
	cd $f/
	cat << EOF > rms_coreCA
coreCA
coreCA
EOF
	gmx rms -s eq_0.tpr -f dyn_alg.xtc -tu ns -o rmsd_dyn.xvg -n index.ndx < rms_coreCA
	../analyze_plot_rmsd.py rmsd_dyn.xvg

       	cat << EOF > rmsf_full
Protein
Protein
EOF
	gmx rmsf -s eq_0.tpr -f dyn_alg.xtc -o rmsf_dyn.xvg -res < rmsf_full
	../analyze_plot_rmsf.py rmsf_dyn.xvg
	cd ../
done

