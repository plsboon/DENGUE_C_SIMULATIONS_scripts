#!/bin/bash

cat << EOF > inp
Protein
EOF
 
gmx mdmat -f dyn_alg.xtc -s min_ionized.tpr -n index.ndx -b 0 -e 200000 -mean dm_0_200.xpm < inp
gmx mdmat -f dyn_alg.xtc -s min_ionized.tpr -n index.ndx -b 200000 -e 400000 -mean dm_200_400.xpm < inp
gmx mdmat -f dyn_alg.xtc -s min_ionized.tpr -n index.ndx -b 400000 -e 600000 -mean dm_400_600.xpm < inp
#gmx mdmat -f dyn_alg.xtc -s min_ionized.tpr -n index.ndx -b 600000 -e 800000 -mean dm_600_800.xpm < inp
#gmx mdmat -f dyn_alg.xtc -s min_ionized.tpr -n index.ndx -b 800000 -e 1000000 -mean dm_800_1000.xpm < inp

gmx xpm2ps -f dm_0_200.xpm -o dm_0_200
gmx xpm2ps -f dm_200_400.xpm -o dm_200_400
gmx xpm2ps -f dm_400_600.xpm -o dm_400_600
#gmx xpm2ps -f dm_600_800.xpm -o dm_600_800
#gmx xpm2ps -f dm_800_1000.xpm -o dm_800_1000

#convert dm_0_200.eps dm_200_400.eps dm_400_600.eps dm_600_800.eps dm_800_1000.eps +append blockwise_contact_map.png

convert dm_0_200.eps dm_200_400.eps dm_400_600.eps +append blockwise_contact_map.png 
