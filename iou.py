import os


GROUND_TRUTH_BOUNDING_BOX_DIR = '/home/xmreality/Documents/Object_detection_rcnn/test_images/groundtruth'
NETWORK_BOUNDING_BOX_DIR = '/home/xmreality/Documents/Object_detection_rcnn/output/test_images/groundtruth'

# Calculates the Intersection over Union ratio. 
def bounding_box_intersection_over_union(boxA, boxB):
  # determine the (x, y)-coordinates of the intersection rectangle
  xA = max(boxA[0], boxB[0])
  yA = max(boxA[1], boxB[1])
  xB = min(boxA[2], boxB[2])
  yB = min(boxA[3], boxB[3])
 
  # compute the area of intersection rectangle, makes sure that if there is no intersection
  # answer is zero
  interArea = max(0,(xB - xA + 1)) * max(0,(yB - yA + 1))
 
  # compute the area of both the prediction and ground-truth
  # rectangles
  boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
  boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
 
  # compute the intersection over union by taking the intersection
  # area and dividing it by the sum of prediction + ground-truth
  # areas - the interesection area
  iou = interArea / float(boxAArea + boxBArea - interArea)
 
  # return the intersection over union value
  return iou


def main():
	lst_of_groundtruth_files = os.listdir(GROUND_TRUTH_BOUNDING_BOX_DIR)

	for network_file in os.listdir(NETWORK_BOUNDING_BOX_DIR):

		if network_file in lst_of_groundtruth_files:
			print('found file in gt')	
		else:
			print('Will not compute iou or precision/recall on file %s, no GT file exist' % (network_file))	
"""


if __name__ == '__main__':
  	main()