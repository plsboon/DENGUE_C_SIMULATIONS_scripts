#!/bin/bash

for i in DENV1.1_complex DENV2.1_complex DENV3.1_complex DENV4.1_complex
do
echo $i
cd $i
cat << EOF > inp
hydrophobic_res_inner_surface
EOF

trj_cavity -f dyn_alg.xtc -s dyn.tpr -n index.ndx -ov hydrophobic_surface_groove_volume.xvg -ostat hydrophobic_surface_groove_stat.pdb -o hydrophobic_surface_groove_cavity.pdb -ot hydrophobic_surface_groove_traj.xtc -tu ns -dim 3 < inp

echo $i" Finished ......."

cd ..
done

