#!/bin/bash

for i in 1000 500 100 50 10 0; do 
	sed s/XXXX/$i/g eq_XXXX.mdp > eq_$i.mdp
done
