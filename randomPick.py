import os, shutil, sys, math
from numpy import random

def main(sys):
	input_folder = os.path.abspath(sys.argv[1])
	#output_folder = os.path.abspath(sys.argv[2])
	#os.makedirs(output_folder, exist_ok=True)
	#how_many_percentage = float(sys.argv[3])
	how_many_percentage = 0.1
	for subdir in os.listdir(input_folder):
		if subdir != "randomHandel":
			continue
		#if subdir == "groundTruth":
		#	continue
		directory = os.path.join(input_folder, subdir)
		if os.path.isdir(directory):
			directory = directory + '/'
			filecount(os.path.abspath(directory))
			directory_full_path = os.path.abspath(directory)			
			number_of_files_to_move = math.ceil(filecount(directory_full_path)*how_many_percentage)
			tmp_list = os.listdir(directory_full_path)
			list_of_files = []
			for file in tmp_list:
				if file.endswith(".jpeg"):
					list_of_files.append(file)
			filenames = random.choice(list_of_files, number_of_files_to_move)		
			lst = []
			for name in filenames:
				if name.endswith(".jpeg"):
					lst.append(name)
			scrpath = os.path.join(directory_full_path,name)
			dstpath = os.path.join(os.path.abspath(output_folder) + '/' ,name)
			try:
				shutil.copyfile(scrpath, dstpath)
			except:
				continue
						

# counts files in a folder
def filecount(folder_path):
	numfiles = sum(1 for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)))
	return numfiles
"""
def move_copy_files(directory_full_path, name, output_folder):
	scrpath = os.path.join(directory_full_path,name)
	dstpath = os.path.join(os.path.abspath(output_folder) + '/' ,name)
	try:
		shutil.copyfile(scrpath, dstpath)
	except:
		continue
"""

if __name__ == "__main__":
    main(sys)