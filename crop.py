import cv2, math, sys, os


# crop image to decenter object

def main(arg):
	"""
	image_folder_path = sys.argv[1]
	saving_folder_path =sys.argv[2]
	wanted_size = sys.argv[3]
	"""
	image_folder_path = "/home/xmreality/Documents/exjobb/preprocessing/"
	image_folder_path = os.path.abspath(image_folder_path)
	saving_folder_path = "/home/xmreality/Documents/exjobb/preprocessing/cropped"
	os.makedirs(saving_folder_path, exist_ok=True)
	wanted_size = 480
	for file in os.listdir(image_folder_path):
		file_full_name = os.path.join(image_folder_path, file)
		img = cv2.imread(os.path.abspath(file_full_name))

		# height and width should be the same
		height, width = img.shape[:2]
		diff = abs(wanted_size - height)

		for i in range(1,5):
			image_name = file + '_i'
			saving_path = os.path.join(saving_folder_path, image_name)
			if i == 1:
				crop_img = img[diff:height, diff:width]
				cv2.imwrite(saving_path, crop_img)
			elif i == 2:	
				crop_img = img[:height-diff, :width-diff]
				cv2.imwrite(saving_path, crop_img)
			elif i == 3:	
				crop_img = img[:height-diff, diff:width]
				cv2.imwrite(saving_path, crop_img)
			else: 	
				crop_img = img[diff:height, :width-diff]
				cv2.imwrite(saving_path, crop_img)	



if __name__ == "__main__":
    main(sys)
