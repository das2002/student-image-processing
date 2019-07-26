"""
Created on Fri Jul 26 06:58:04 2019

@author: PRAT
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def calc_algal_bloom_ndvi(nir, green, blue):
    '''Calculate ferrous iron from integer arrays'''
    nir = nir.astype('f4')
    #red = red.astype('f4')
    blue = blue.astype('f4')
    #swir2 = swir2.astype('f4')
    green = green.astype('f4')
    algal_bloom = (nir-green+blue)/(nir+green+blue)
    return algal_bloom
  

def analyzeimage(old_image):
	# analyze the image 'old_image' here
	# save the analyzed image to 'static/temp.jpg'
	# return the path of the new image file
    img = cv2.imread(old_image)
    edges =  cv2.Canny(img, 100, 200)

    b,g,r = cv2.split(img)
        

    plt.subplot(161), plt.imshow(img) #cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(162), plt.imshow(edges)#, cmap ='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(163), plt.imshow(b)#, cmap ='gray')
    plt.title('Blue Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(164), plt.imshow(g)#, cmap ='gray')
    plt.title('Green Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(165), plt.imshow(r)#, cmap ='gray')
    plt.title('Red Image'), plt.xticks([]), plt.yticks([])
    algal_bloom = calc_algal_bloom_ndvi(r, g , b)
    plt.subplot(166), plt.imshow(algal_bloom, cmap='RdYlGn')
    plt.title('Algal Bloom')
	
    plt.show()
    





	
	
	#return "static/temp.jpg"

analyzeimage('img013.jpg')
