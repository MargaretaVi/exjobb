import os, shutil, sys, math
from numpy import random

def main(sys):
	input_folder = os.path.abspath(sys.argv[1])
	output_folder = os.path.abspath(sys.argv[2])
	os.makedirs(output_folder, exist_ok=True)
	how_many_percentage = float(sys.argv[3])

	for file in os.listdir(input_folder):
		if file == "groundTruth":
			continue
		directory = os.path.join(input_folder, file)
		if os.path.isdir(directory):
			directory = directory + '/'

			filecount(os.path.abspath(directory))
			directory_full_path = os.path.abspath(directory)			
			number_of_files_to_move = math.ceil(filecount(directory_full_path)*how_many_percentage)
			filenames = random.choice(os.listdir(directory_full_path), number_of_files_to_move)		
			for name in filenames:
				scrpath = os.path.join(directory_full_path,name)
				dstpath = os.path.join(os.path.abspath(output_folder),name)
				try:
					shutil.move(scrpath, dstpath)
				except:
					continue	

# counts files in a folder
def filecount(folder_path):
	numfiles = sum(1 for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)))
	return numfiles

if __name__ == "__main__":
    main(sys)