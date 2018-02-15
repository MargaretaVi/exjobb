#! /bin/bash

for file in blendFiler/*; do
	if [[ $file = *.blend ]]; then 
		blender $file --background --python sample_texture_background.py -- background/smaller/ texture/ images/
	fi
done	

