import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr

img=cv2.imread('C://Users//nithe//OneDrive//Desktop//kavach_hackathon//Images//8.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray,cv2.COLOR_BGR2RGB))