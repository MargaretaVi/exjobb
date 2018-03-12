#! /bin/bash
start_time="$(date -u +%s)"

for file in /home/xmreality/Documents/exjobb/data/blendFiler/*; do
	if [[ $file = *.blend ]]; then 
		blender $file --background --python Rendering_v2.py -- real_img/background real_img/texture ~/Desktop/images $file
	fi
done	
end_time="$(date -u +%s)"
elapsed="$(($end_time-$start_time))"
echo "Total of $elapsed seconds elapsed for process"