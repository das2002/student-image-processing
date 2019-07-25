import cv2
import numpy as np
from matplotlib import pyplot as plt


def analyzeimage(old_image):
	# analyze the image 'old_image' here
	img = cv2.imread(old_image)
	edges = cv2.Canny(img, 100,200)
	
	plt.subplot(121), plt.imshow(img, cmap = 'gray')
	plt.title('Original Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(122), plt.imshow(edges, cmap = 'gray')
	plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
	plt.show()
	# save the analyzed image to 'static/temp.jpg'
	# return the path of the new image file
	return "static/temp.jpg"
