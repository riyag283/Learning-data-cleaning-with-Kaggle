import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img2.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# to hide tick values on X and Y axes
plt.xticks([]),plt.yticks([]) 
plt.show()