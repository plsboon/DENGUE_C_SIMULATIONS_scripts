#!/bin/bash

for i in DENV1 DENV2 DENV3 DENV4
do
echo $i
cat << EOF > inp
hydrophobic_res_inner_surface
EOF

trj_cavity -f $i/solv.gro -s $i/min.tpr -n $i/index.ndx -ov $i"_hydrophobic_surface_groove_volume.xvg" -ostat $i"_hydrophobic_surface_groove_stat.pdb" -o $i"_hydrophobic_surface_groove_cavity.pdb" -ot $i"_hydrophobic_surface_groove_traj.xtc" -tu ns -dim 3 < inp

./block_analyze_plot_SASA.py -f $i/hydrophobic_surface_groove_volume.xvg $i"a/hydrophobic_surface_groove_volume.xvg" $i"b/hydrophobic_surface_groove_volume.xvg" -l CHARMM36 AMBER14 GROMOS96 -c $i"_hydrophobic_surface_groove_volume.xvg" -log $i"_block_surface_groove.log" -o $i"_block_surface_groove.svg"

echo $i" Finished ......."
done

