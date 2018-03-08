#! /bin/bash

for file in data/several_obj_blend_files/*; do
	if [[ $file = *.blend ]]; then 
		blender $file --background --python several_object_rendering.py -- ~/Desktop/texture/ ~/Desktop/background/ ~/Desktop/GTimages/ $file
	fi
done	

