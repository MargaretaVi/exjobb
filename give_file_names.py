import os, sys

def main(sys):
	folder = sys.argv[1]
	filename_path = sys.argv[2]

	textfile = open(filename_path, "w+")
	folder_full_path = os.path.abspath(folder)
	for f in os.listdir(folder_full_path):
		textfile.write(os.path.splitext(os.path.basename(f))[0])
		textfile.write('\n')
	textfile.close()	


if __name__ == '__main__':
	main(sys)