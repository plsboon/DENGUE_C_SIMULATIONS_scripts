#!/bin/bash

for i in DENV1.1_complex DENV2.1_complex DENV3.1_complex DENV4.1_complex
do
cd $i
echo "Now in "$i
	cat << EOF > chainA_dssp
ChainA
EOF
	gmx do_dssp -f dyn.xtc -s dyn.tpr -o ChainA_1_ms.xpm -n index.ndx -tu ns < chainA_dssp
	gmx xpm2ps -f ChainA_1_ms.xpm -o ChainA_1_ms.eps -bx 1 -by 10 -di ../dssp.m2p
	echo "Now converting ChainA_1_ms.eps"
	epstopdf --res 400 --nocompress ChainA_1_ms.eps

	cat << EOF > chainB_dssp
ChainB
EOF
	gmx do_dssp -f dyn.xtc -s dyn.tpr -o ChainB_1_ms.xpm -n index.ndx -tu ns < chainB_dssp
        gmx xpm2ps -f ChainB_1_ms.xpm -o ChainB_1_ms.eps -bx 1 -by 10 -di ../dssp.m2p
	echo "Now converting ChainB_1_ms.eps"
        epstopdf --res 400 --nocompress ChainB_1_ms.eps

	echo "Generating composite picture"
	convert ChainA_1_ms.pdf ChainB_1_ms.pdf -append ../figs/$i"_chainA_chainB.png"

echo "Finished "$i
cd ..
done

