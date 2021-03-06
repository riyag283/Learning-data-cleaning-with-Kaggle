# Below program loads an image in grayscale,
# displays it, save the image if you press ‘s’
# and exit, or simply exit without saving
# if you press ESC key.
import numpy as np
import cv2

img = cv2.imread('img2.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('newrose.png',img)
    cv2.destroyAllWindows()